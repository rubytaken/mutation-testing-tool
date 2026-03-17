from __future__ import annotations

import ast
import copy

from mutation_tool.operators.base import OperatorMutation

LOGICAL_MUTATIONS: dict[type[ast.boolop], type[ast.boolop]] = {
    ast.And: ast.Or,
    ast.Or: ast.And,
}


class LogicalOperator:
    name = "logical"

    def mutations(self, node: ast.AST) -> list[OperatorMutation]:
        if not isinstance(node, ast.BoolOp):
            return []

        replacement_type = LOGICAL_MUTATIONS.get(type(node.op))
        if replacement_type is None:
            return []

        clone = copy.deepcopy(node)
        clone.op = replacement_type()
        return [
            OperatorMutation(
                target_node=node,
                replacement=ast.unparse(clone),
                description="swap logical operator",
            )
        ]
