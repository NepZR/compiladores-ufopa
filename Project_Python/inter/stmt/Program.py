from inter import Node
from inter.stmt import Block

from lexer import Token, Tag


class Program(Node):
    def __init__(self, _id: Token, _block: Block | Node) -> None:
        super().__init__()
        self._id = _id
        self._block = _block

        self._add_child(node=self._block)

    def __str__(self) -> str:
        return Tag.PROGRAM.__str__()
