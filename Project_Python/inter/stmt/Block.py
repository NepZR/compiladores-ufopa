from inter import Node


class Block(Node):
    def __init__(self) -> None:
        super().__init__()

    def add_stmt(self, stmt: Node) -> None:
        self._add_child(node=stmt)

    def __str__(self) -> str:
        return "BLOCK"
