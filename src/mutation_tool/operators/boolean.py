from __future__ import annotations

import ast

from mutation_tool.operators.base import OperatorMutation


class BooleanLiteralOperator:
    name = "boolean_literal"

    def mutations(self, node: ast.AST) -> list[OperatorMutation]:
        if not isinstance(node, ast.Constant) or not isinstance(node.value, bool):
            return []
        return [
            OperatorMutation(
                target_node=node,
                replacement="False" if node.value is True else "True",
                description="flip boolean literal",
            )
        ]


class ConditionNegationOperator:
    name = "condition_negation"

    def mutations(self, node: ast.AST) -> list[OperatorMutation]:
        if isinstance(node, (ast.If, ast.While, ast.Assert, ast.IfExp)):
            return self._negate_nodes([node.test])
        if isinstance(node, ast.comprehension):
            return self._negate_nodes(node.ifs)
        return []

    def _negate_nodes(self, tests: list[ast.expr]) -> list[OperatorMutation]:
        mutations: list[OperatorMutation] = []
        for test in tests:
            if isinstance(test, ast.UnaryOp) and isinstance(test.op, ast.Not):
                continue
            mutations.append(
                OperatorMutation(
                    target_node=test,
                    replacement=f"not ({ast.unparse(test)})",
                    description="negate boolean condition",
                )
            )
        return mutations


class NotRemovalOperator:
    name = "not_removal"

    def mutations(self, node: ast.AST) -> list[OperatorMutation]:
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            return [
                OperatorMutation(
                    target_node=node,
                    replacement=ast.unparse(node.operand),
                    description="remove not operator",
                )
            ]
        return []
