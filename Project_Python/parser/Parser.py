from lexer.Tag import Tag
from lexer.Token import Token
from lexer.Lexer import Lexer

from inter.stmt import Stmt, Assign, Block, Decl, Program, Write, If
from inter.expr import Expr, Literal, Rel, Id, Bin, Or


class Parser:
    def __init__(self, lex: Lexer) -> None:
        self._lexer = lex
        self._look = None
        self._root = None
        self._move()

    def _move(self) -> Token:
        save = self._look
        self._look = self._lexer.next_token()
        return save

    def _error(self, err: str) -> None:
        print(f"Linha {self._lexer.line()}: {err}.")
        exit(0)

    def _match(self, t: Tag) -> Token | None:
        if self._look.tag == t:
            return self._move()

        self._error(err="Símbolo inesperado")
        return None

    def parse_tree(self) -> str:
        return self._root.str_tree()

    def parse(self) -> None:
        self._root = self._program()

    def _program(self) -> Program:
        self._match(Tag.PROGRAM)
        token_id = self._match(Tag.ID)
        block = self._block()

        self._match(Tag.DOT)
        self._match(Tag.EOF)

        return Program(_id=token_id, _block=block)

    def _block(self) -> Stmt:
        block = Block()

        self._match(Tag.BEGIN)
        while self._look.tag != Tag.END:
            block.add_stmt(self._stmt())
            self._match(Tag.SEMI)

        self._match(Tag.END)
        return block

    def _stmt(self) -> Stmt | None:
        if self._look.tag == Tag.BEGIN:
            return self._block()
        elif self._look.tag in (Tag.INT, Tag.REAL, Tag.BOOL):
            return self._decl()
        elif self._look.tag == Tag.ID:
            return self._assign()
        elif self._look.tag == Tag.IF:
            return self._if_stmt()
        elif self._look.tag == Tag.WRITE:
            return self._write_stmt()
        else:
            self._error(err="Comando inválido")

        return None

    def _decl(self) -> Stmt:
        _type = self._move()
        token_id = self._match(Tag.ID)

        _id = Id(_op=token_id, _type=_type.tag)
        return Decl(_id=_id)

    def _assign(self) -> Stmt:
        _token = self._match(Tag.ID)
        _id = Id(_op=_token, _type=None)

        self._match(Tag.ASSIGN)
        _expr = self._expr()
        return Assign(_id=_id, _expr=_expr)

    def _expr(self) -> Expr:
        _expr = self._rel()
        while self._look.tag == Tag.OR:
            self._move()
            _expr = Or(e1=_expr, e2=self._rel())

        return _expr

    def _rel(self) -> Expr:
        _expr = self._arith()
        while self._look.tag in (Tag.LT, Tag.LE, Tag.GT):
            _op = self._move()
            _expr = Rel(_op=_op, e1=_expr, e2=self._arith())

        return _expr

    def _arith(self) -> Expr:
        _expr = self._term()
        while self._look.tag in (Tag.SUM, Tag.SUB):
            _op = self._move()
            _expr = Bin(_op=_op, e1=_expr, e2=self._term())

        return _expr

    def _term(self) -> Expr:
        _expr = self._factor()
        while self._look.tag == Tag.MUL:
            _op = self._move()
            _expr = Bin(_op=_op, e1=_expr, e2=self._factor())

        return _expr

    def _factor(self) -> Expr | None:
        _expr = None

        if self._look.tag == Tag.LPAREN:
            self._move()
            _expr = self._expr()
            self._match(Tag.RPAREN)
        elif self._look.tag in (Tag.LIT_INT, Tag.LIT_REAL, Tag.TRUE, Tag.FALSE):
            _type = Tag(self._look.tag)
            _expr = Literal(_op=self._move(), _type=_type)
        elif self._look.tag == Tag.ID:
            _token = self._match(Tag.ID)
            _expr = Id(_op=_token, _type=None)
        else:
            self._error(err="Expressão inválida")

        return _expr

    def _if_stmt(self) -> Stmt:
        self._match(Tag.IF)
        self._match(Tag.LPAREN)

        _expr = self._expr()
        self._match(Tag.RPAREN)
        _stmt = self._stmt()

        return If(_expr=_expr, _stmt=_stmt)

    def _write_stmt(self) -> Stmt:
        self._move()
        self._match(Tag.LPAREN)

        _token = self._match(Tag.ID)
        _id = Id(_op=_token, _type=None)

        self._match(Tag.RPAREN)
        return Write(_id=_id)
