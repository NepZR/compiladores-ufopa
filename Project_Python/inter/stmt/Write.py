from inter.expr import Id
from inter import Node

from lexer import Tag


class Write(Node):
    def __init__(self, _id: Id) -> None:
        super().__init__()

        self._id = _id
        self._add_child(node=self._id)

    def __str__(self) -> str:
        return Tag.WRITE.__str__()
