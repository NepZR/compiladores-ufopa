from inter.expr import Id, Expr
from inter import Node

from lexer import Tag


class Assign(Node):
    def __init__(self, _id: Id, _expr: Expr) -> None:
        super().__init__()
        self._id = _id
        self._expr = _expr

        self._add_child(node=self._id)
        self._add_child(node=self._expr)

    def __str__(self) -> str:
        return Tag.ASSIGN.__str__()
