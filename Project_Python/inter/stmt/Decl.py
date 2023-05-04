from inter import Node
from inter.expr import Id


class Decl(Node):
    def __init__(self, _id: Id) -> None:
        super().__init__()
        self._id = _id

        self._add_child(node=self._id)

    def __str__(self) -> str:
        return "DECL"
