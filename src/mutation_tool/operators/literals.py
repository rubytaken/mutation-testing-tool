from __future__ import annotations

import ast

from mutation_tool.operators.base import OperatorMutation


class NumericLiteralOperator:
    name = "numeric_literal"

    def mutations(self, node: ast.AST) -> list[OperatorMutation]:
        if not isinstance(node, ast.Constant):
            return []
        if isinstance(node.value, bool):
            return []
        if not isinstance(node.value, int | float):
            return []
        return [
            OperatorMutation(
                target_node=node,
                replacement=repr(node.value + 1),
                description="nudge numeric literal by one",
            )
        ]
