from mutation_tool.operators.arithmetic import ArithmeticOperator
from mutation_tool.operators.base import MutationOperator, OperatorMutation
from mutation_tool.operators.boolean import (
    BooleanLiteralOperator,
    ConditionNegationOperator,
    NotRemovalOperator,
)
from mutation_tool.operators.comparison import ComparisonOperator
from mutation_tool.operators.literals import NumericLiteralOperator
from mutation_tool.operators.logical import LogicalOperator

__all__ = [
    "MutationOperator",
    "OperatorMutation",
    "ArithmeticOperator",
    "BooleanLiteralOperator",
    "ConditionNegationOperator",
    "ComparisonOperator",
    "LogicalOperator",
    "NotRemovalOperator",
    "NumericLiteralOperator",
    "build_default_operators",
]


def build_default_operators() -> list[MutationOperator]:
    return [
        ComparisonOperator(),
        BooleanLiteralOperator(),
        LogicalOperator(),
        ArithmeticOperator(),
        NumericLiteralOperator(),
        ConditionNegationOperator(),
        NotRemovalOperator(),
    ]
