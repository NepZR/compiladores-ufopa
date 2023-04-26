from lexer.Tag import Tag
from lexer.Token import Token
from lexer.Lexer import Lexer


class Parser:
    def __init__(self, lex: Lexer) -> None:
        self._lexer = lex
        self._look = None
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

    def parse(self) -> None:
        self._program()

    def _program(self) -> None:
        self._match(Tag.PROGRAM)
        self._match(Tag.ID)
        self._block()
        self._match(Tag.DOT)
        self._match(Tag.EOF)

    def _block(self) -> None:
        self._match(Tag.BEGIN)
        while self._look.tag != Tag.END:
            self._stmt()
            self._match(Tag.SEMI)

        self._match(Tag.END)

    def _stmt(self) -> None:
        if self._look.tag == Tag.BEGIN:
            self._block()
        elif self._look.tag in (Tag.INT, Tag.REAL, Tag.BOOL):
            self._decl()
        elif self._look.tag == Tag.ID:
            self._assign()
        elif self._look.tag == Tag.IF:
            self._if_stmt()
        elif self._look.tag == Tag.WRITE:
            self._write_stmt()
        else:
            self._error(err="Comando inválido")

    def _decl(self) -> None:
        self._move()
        self._match(Tag.ID)

    def _assign(self) -> None:
        self._match(Tag.ID)
        self._match(Tag.ASSIGN)
        self._expr()

    def _expr(self) -> None:
        self._rel()
        while self._look.tag == Tag.OR:
            self._move()
            self._rel()

    def _rel(self) -> None:
        self._arith()
        while self._look.tag in (Tag.LT, Tag.LE, Tag.GT):
            self._move()
            self._arith()

    def _arith(self) -> None:
        self._term()
        while self._look.tag in (Tag.SUM, Tag.SUB):
            self._move()
            self._term()

    def _term(self) -> None:
        self._factor()
        while self._look.tag == Tag.MUL:
            self._move()
            self._factor()

    def _factor(self) -> None:
        if self._look.tag == Tag.LPAREN:
            self._move()
            self._expr()
            self._match(Tag.RPAREN)

        elif self._look.tag in (Tag.LIT_INT, Tag.LIT_REAL, Tag.TRUE, Tag.FALSE):
            self._move()
        elif self._look.tag == Tag.ID:
            self._match(Tag.ID)
        else:
            self._error(err="Expressão inválida")

    def _if_stmt(self) -> None:
        self._match(Tag.IF)
        self._match(Tag.LPAREN)
        self._expr()
        self._match(Tag.RPAREN)
        self._stmt()

    def _write_stmt(self) -> None:
        self._move()
        self._match(Tag.LPAREN)
        self._match(Tag.ID)
        self._match(Tag.RPAREN)
