from llist import sllist

from typing import Any


class Node:
    def __init__(self) -> None:
        self._children = sllist()

    def _add_child(self, node: Any) -> None:
        self._children.append(node)

    def _get_children(self) -> sllist:
        return self._children

    def str_tree(self) -> str:
        return self._str_tree(ident="")

    def _str_tree(self, ident: str) -> str:
        buffer = ""
        for node in self._children.itervalues():
            buffer += f"\n{ident}|--> {node}"
            buffer += node._str_tree(ident=f"{ident}    ")

        return buffer
