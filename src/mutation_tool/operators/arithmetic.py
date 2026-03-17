from __future__ import annotations

import ast
import copy

from mutation_tool.operators.base import OperatorMutation

ARITHMETIC_MUTATIONS: dict[type[ast.operator], type[ast.operator]] = {
    ast.Add: ast.Sub,
    ast.Sub: ast.Add,
    ast.Mult: ast.FloorDiv,
    ast.FloorDiv: ast.Mult,
}


class ArithmeticOperator:
    name = "arithmetic"

    def mutations(self, node: ast.AST) -> list[OperatorMutation]:
        if not isinstance(node, ast.BinOp):
            return []

        replacement_type = ARITHMETIC_MUTATIONS.get(type(node.op))
        if replacement_type is None:
            return []

        clone = copy.deepcopy(node)
        clone.op = replacement_type()
        return [
            OperatorMutation(
                target_node=node,
                replacement=ast.unparse(clone),
                description="swap arithmetic operator",
            )
        ]
