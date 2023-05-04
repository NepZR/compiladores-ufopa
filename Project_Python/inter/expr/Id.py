from inter.expr import Expr

from lexer.Token import Token
from lexer.Tag import Tag


class Id(Expr):
    def __init__(self, _op: Token, _type: Tag | None) -> None:
        super().__init__(_op=_op, _type=_type)

    def __str__(self) -> str:
        return f"%{self._op.lexeme()}"
