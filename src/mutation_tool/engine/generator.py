from __future__ import annotations

import ast
import hashlib
from pathlib import Path

from mutation_tool.models import MutationLocation, MutationSpec
from mutation_tool.operators import MutationOperator


def generate_mutations(
    file_paths: list[Path],
    project_root: Path,
    operators: list[MutationOperator],
) -> list[MutationSpec]:
    mutations: list[MutationSpec] = []
    for file_path in file_paths:
        mutations.extend(generate_mutations_for_file(file_path, project_root, operators))
    return mutations


def generate_mutations_for_file(
    file_path: Path,
    project_root: Path,
    operators: list[MutationOperator],
) -> list[MutationSpec]:
    source = file_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(file_path))
    relative_path = file_path.resolve().relative_to(project_root)
    protected_lines = _protected_lines(source)
    generated: list[MutationSpec] = []
    seen: set[tuple[int, int, int, int, str, str]] = set()

    for node in sorted(ast.walk(tree), key=_node_sort_key):
        for operator in operators:
            for candidate in operator.mutations(node):
                target = candidate.target_node
                location = _location_from_node(target)
                if location is None:
                    continue
                if _is_protected(location, protected_lines):
                    continue
                original_snippet = ast.get_source_segment(source, target)
                if original_snippet is None:
                    continue
                if original_snippet.strip() == candidate.replacement.strip():
                    continue

                dedupe_key = (
                    location.start_line,
                    location.start_col,
                    location.end_line,
                    location.end_col,
                    operator.name,
                    candidate.replacement,
                )
                if dedupe_key in seen:
                    continue
                seen.add(dedupe_key)

                generated.append(
                    MutationSpec(
                        mutant_id=_build_mutant_id(
                            relative_path,
                            location,
                            operator.name,
                            candidate.replacement,
                        ),
                        file_path=relative_path,
                        operator_name=operator.name,
                        location=location,
                        original_snippet=original_snippet,
                        mutated_snippet=candidate.replacement,
                        description=candidate.description,
                    )
                )
    return generated


def apply_mutation_to_source(source: str, spec: MutationSpec) -> str:
    start_offset = _position_to_offset(source, spec.location.start_line, spec.location.start_col)
    end_offset = _position_to_offset(source, spec.location.end_line, spec.location.end_col)
    return f"{source[:start_offset]}{spec.mutated_snippet}{source[end_offset:]}"


def _protected_lines(source: str) -> set[int]:
    return {
        index
        for index, line in enumerate(source.splitlines(), start=1)
        if "pragma: no mutate" in line
    }


def _is_protected(location: MutationLocation, protected_lines: set[int]) -> bool:
    return any(
        line in protected_lines for line in range(location.start_line, location.end_line + 1)
    )


def _location_from_node(node: ast.AST) -> MutationLocation | None:
    start_line = _read_int_attr(node, "lineno")
    start_col = _read_int_attr(node, "col_offset")
    end_line = _read_int_attr(node, "end_lineno")
    end_col = _read_int_attr(node, "end_col_offset")
    if start_line is None or start_col is None or end_line is None or end_col is None:
        return None
    return MutationLocation(start_line, start_col, end_line, end_col)


def _read_int_attr(node: ast.AST, attribute: str) -> int | None:
    value = getattr(node, attribute, None)
    if isinstance(value, int):
        return value
    return None


def _build_mutant_id(
    relative_path: Path,
    location: MutationLocation,
    operator_name: str,
    replacement: str,
) -> str:
    fingerprint = hashlib.sha1(
        f"{relative_path}:{location.start_line}:{location.start_col}:{operator_name}:{replacement}".encode()
    ).hexdigest()[:8]
    return (
        f"{relative_path.as_posix()}:"
        f"{location.start_line}:{location.start_col}:{operator_name}:{fingerprint}"
    )


def _position_to_offset(source: str, line: int, col: int) -> int:
    current_line = 1
    offset = 0
    for chunk in source.splitlines(keepends=True):
        if current_line == line:
            return offset + col
        offset += len(chunk)
        current_line += 1
    return len(source)


def _node_sort_key(node: ast.AST) -> tuple[int, int, int, int, str]:
    lineno = getattr(node, "lineno", 0)
    col_offset = getattr(node, "col_offset", 0)
    end_lineno = getattr(node, "end_lineno", lineno)
    end_col_offset = getattr(node, "end_col_offset", col_offset)
    return (lineno, col_offset, end_lineno, end_col_offset, type(node).__name__)
