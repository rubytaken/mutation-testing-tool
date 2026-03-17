from __future__ import annotations

import ast
import copy

from mutation_tool.operators.base import OperatorMutation

COMPARISON_MUTATIONS: dict[type[ast.cmpop], type[ast.cmpop]] = {
    ast.Lt: ast.LtE,
    ast.Gt: ast.GtE,
    ast.Eq: ast.NotEq,
    ast.In: ast.NotIn,
    ast.Is: ast.IsNot,
}


class ComparisonOperator:
    name = "comparison"

    def mutations(self, node: ast.AST) -> list[OperatorMutation]:
        if not isinstance(node, ast.Compare):
            return []

        mutations: list[OperatorMutation] = []
        for index, operator in enumerate(node.ops):
            replacement_type = COMPARISON_MUTATIONS.get(type(operator))
            if replacement_type is None:
                continue
            clone = copy.deepcopy(node)
            clone.ops[index] = replacement_type()
            mutations.append(
                OperatorMutation(
                    target_node=node,
                    replacement=ast.unparse(clone),
                    description=f"swap comparison operator at position {index}",
                )
            )
        return mutations
