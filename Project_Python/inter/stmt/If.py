from inter.expr import Expr
from inter import Node

from lexer import Tag


class If(Node):
    def __init__(self, _expr: Expr, _stmt: Node) -> None:
        super().__init__()
        self._expr = _expr
        self._stmt = _stmt

        self._add_child(node=self._expr)
        self._add_child(node=self._stmt)

    def __str__(self) -> str:
        return Tag.IF.__str__()
