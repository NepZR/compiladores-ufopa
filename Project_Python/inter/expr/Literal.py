from inter.expr import Expr

from lexer.Token import Token
from lexer.Tag import Tag


class Literal(Expr):
    def __init__(self, _op: Token, _type: Tag) -> None:
        super().__init__(_op=_op, _type=_type)

    def __str__(self) -> str:
        if self._op.tag == Tag.TRUE:
            return "true"
        elif self._op.tag == Tag.FALSE:
            return "false"
        else:
            return self._op.lexeme()
