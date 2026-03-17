from __future__ import annotations

import ast
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class OperatorMutation:
    target_node: ast.AST
    replacement: str
    description: str


class MutationOperator(Protocol):
    name: str

    def mutations(self, node: ast.AST) -> list[OperatorMutation]:
        ...
