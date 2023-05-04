from inter import Node

from lexer.Token import Token
from lexer.Tag import Tag


class Expr(Node):
    def __init__(self, _op: Token, _type: Tag | None) -> None:
        super().__init__()
        self._op = _op
        self._type = _type

    def get_op(self) -> Token:
        return self.__op

    def get_type(self) -> Tag:
        return self._type

    def __str__(self) -> str:
        return self._op.__str__()
