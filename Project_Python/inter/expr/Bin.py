from inter.expr.Expr import Expr

from lexer.Token import Token, Tag

from exceptions import DLSemanticError


class Bin(Expr):
    def __init__(self, _op: Token, e1: Expr, e2: Expr) -> None:
        super().__init__(_op=_op, _type=None)
        self._type = self._max_type(t1=e1.get_type(), t2=e2.get_type())
        if self._type is None:
            raise DLSemanticError("Tipos incompatíveis.")

        self._expr_1 = e1
        self._expr_2 = e2

        self._add_child(node=self._expr_1)
        self._add_child(node=self._expr_2)

    @staticmethod
    def _max_type(t1: Tag, t2: Tag) -> Tag | None:
        if not t1.is_num() or not t2.is_num():
            return None
        elif t1.is_real() or t2.is_real():
            return Tag.REAL
        else:
            return Tag.INT
