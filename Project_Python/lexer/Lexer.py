from .Tag import Tag
from .Token import Token


class Lexer:
    def __init__(self, file: str) -> None:
        self.EOF_CHAR = str(-1)
        self.line_index = 0
        self.peek = " "
        self.keywords = {
            "programa": Tag.PROGRAM,
            "inicio": Tag.BEGIN,
            "fim": Tag.END,
            "inteiro": Tag.INT,
            "real": Tag.REAL,
            "booleano": Tag.BOOL,
            "verdadeiro": Tag.TRUE,
            "falso": Tag.FALSE,
            "leia": Tag.READ,
            "escreva": Tag.WRITE
        }
        with open(file, "rb") as f:
            self.reader = f.read().decode("UTF-8")

    def line(self) -> int:
        return self.line_index

    def _next_char(self) -> str:
        try:
            self.peek = str(self.reader[self.line()])
            self.line_index += 1
            return self.peek
        except IndexError:
            self.peek = str(-1)
            return self.peek

    @staticmethod
    def _is_whitespace(character: str, parse_comment: bool = False) -> bool:
        whitespaces = ("\n", "\t", "\r") if parse_comment else (" ", "\n", "\t", "\r")
        if character in whitespaces:
            return True
        else:
            return False

    @staticmethod
    def _is_id_start(character: str) -> bool:
        return character.isalpha() or character == "_"

    def _is_id_part(self, character: str) -> bool:
        return self._is_id_start(character) or character.isdigit()

    def next_token(self) -> Token:
        while self._is_whitespace(self.peek):
            self._next_char()

        if self.peek == "!":
            self._next_char()
            if self.peek == "=":
                self._next_char()
                return Token(Tag.NE, "!=")
            return Token(Tag.NOT, "!")
        elif self.peek == "=":
            self._next_char()
            return Token(Tag.ASSIGN, "=")
        elif self.peek == "&":
            self._next_char()
            return Token(Tag.AND, "&")
        elif self.peek == "+":
            self._next_char()
            return Token(Tag.SUM, "+")
        elif self.peek == "-":
            self._next_char()
            return Token(Tag.SUB, "=")
        elif self.peek == "*":
            self._next_char()
            return Token(Tag.MUL, "=")
        elif self.peek == "/":
            self._next_char()
            if self.peek == "/":
                self._next_char()
                comment = "//"
                while not self._is_whitespace(self.peek, parse_comment=True):
                    comment += self.peek
                    self._next_char()

                return Token(Tag.COMMENT, comment)

            return Token(Tag.DIV, "/")
        elif self.peek == "|":
            self._next_char()
            return Token(Tag.OR, "|")
        elif self.peek == "<":
            self._next_char()
            if self.peek == "=":
                self._next_char()
                return Token(Tag.LE, "<=")
            return Token(Tag.LT, "<")
        elif self.peek == ">":
            self._next_char()
            if self.peek == "=":
                self._next_char()
                return Token(Tag.GE, ">=")
            return Token(Tag.GT, ">")
        elif self.peek == ",":
            self._next_char()
            return Token(Tag.COMMA, ",")
        elif self.peek == ";":
            self._next_char()
            return Token(Tag.SEMI, ";")
        elif self.peek == "(":
            self._next_char()
            return Token(Tag.LPAREN, "(")
        elif self.peek == ")":
            self._next_char()
            return Token(Tag.RPAREN, ")")
        elif self.peek == self.EOF_CHAR:
            self._next_char()
            return Token(Tag.EOF, "")
        else:
            if self.peek.isdigit():
                num = ""
                while self.peek.isdigit():
                    num += self.peek
                    self._next_char()

                if self.peek == ".":
                    num += self.peek
                    self._next_char()
                    if not self.peek.isdigit():
                        num += str(0)
                    else:
                        while self.peek.isdigit():
                            num += self.peek
                            self._next_char()

                    return Token(Tag.LIT_REAL, num)

                return Token(Tag.LIT_INT, num)
            elif self._is_id_start(self.peek):
                _id = ""
                while self._is_id_part(self.peek):
                    _id += self.peek
                    self._next_char()
                if _id in self.keywords.keys():
                    return Token(self.keywords[_id], _id)

                return Token(Tag.ID, _id)

        unk = str(self.peek)
        self._next_char()
        return Token(Tag.UNK, unk)
