from inter.expr.Expr import Expr

from lexer.Token import Token


class Bin(Expr):
    def __init__(self, _op: Token, e1: Expr, e2: Expr) -> None:
        super().__init__(_op=_op, _type=None)
        self._expr_1 = e1
        self._expr_2 = e2

        self._add_child(node=self._expr_1)
        self._add_child(node=self._expr_2)
