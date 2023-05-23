from inter.expr import Expr

from lexer.Token import Token
from lexer.Tag import Tag

from exceptions import DLSemanticError


class Or(Expr):
    def __init__(self, e1: Expr, e2: Expr) -> None:
        super().__init__(
            _op=Token(Tag.OR, "|"),
            _type=Tag.BOOL
        )
        if not e1.get_type().is_bool() or not e2.get_type().is_bool():
            raise DLSemanticError("O operador lógico só pode ser aplicado entre tipos booleanos.")

        self._expr_1 = e1
        self._expr_2 = e2

        self._add_child(node=self._expr_1)
        self._add_child(node=self._expr_2)
