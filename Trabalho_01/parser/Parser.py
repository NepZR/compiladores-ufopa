from sys import exit

from parser.IParser import IParser


class Parser(IParser):
    def __init__(self, file: str) -> None:
        super().__init__()
        with open(file, "rb") as f:
            self.reader = f.read().decode("UTF-8")

        self.line_idx = 1
        self.col_idx = 0
        self.chr_idx = 0
        self.peek = " "

    def lookahead(self) -> str:
        try:
            self.peek = str(self.reader[self.chr_idx])
            return self.peek
        except IndexError:
            self.peek = self.EOF
            return self.EOF

    def next(self) -> str:
        whitespaces = (" ", "\n", "\t", "\r")
        self.chr_idx += 1
        self.col_idx += 1

        while self.lookahead() in whitespaces:
            if self.peek == "\n":
                self.line_idx += 1
                self.col_idx = 0

            self.chr_idx += 1
            self.col_idx += 1
            continue

        return self.lookahead()

    def match(self, c: str) -> None:
        if self.lookahead() == c:
            self.next()
        else:
            self.error(msg="Símbolo inválido")

    def error(self, msg: str) -> None:
        print(f"Syntax Error on {self.line_idx}:{self.col_idx}: {msg}.")
        print(f"Lookahead Data >> {self.lookahead()}")
        exit(1)

    def parse(self) -> None:
        self.assign()

    def assign(self) -> None:
        self.left()
        self._assign()

    def _assign(self) -> None:
        if self.lookahead() == '>':
            self.match(">")
            self.match("(")
            self.expr()
            self.match(")")
        elif self.lookahead() == "<":
            self.match("<")
            self.match("(")
            self.expr()
            self.match(")")
        elif self.lookahead() == "=":
            self.match("=")
            self.rest()
        else:
            self.error(msg="Expressão inválida")

    def left(self) -> None:
        if self.lookahead().isalpha():
            self.match(self.lookahead())
            self._left()
        else:
            self.error(msg="Expressão inválida")

    def _left(self) -> None:
        if self.lookahead() == "[":
            self.match("[")
            self.expr()
            self.match("]")
        else:
            pass

    def rest(self) -> None:
        if self.lookahead() == "(":
            self.match("(")
            self.expr()
            self.match(")")
        else:
            self.left()
            self.match("=")
            self.rest()

    def expr(self) -> None:
        self.term()
        self._expr()

    def _expr(self) -> None:
        if self.lookahead() == "+":
            self.match("+")
            self.term()
            self._expr()
        elif self.lookahead() == "-":
            self.match("-")
            self.term()
            self._expr()
        else:
            pass

    def term(self) -> None:
        self.unary()
        self._term()

    def _term(self) -> None:
        if self.lookahead() == "*":
            self.match("*")
            self.unary()
            self._term()
        elif self.lookahead() == "/":
            self.match("/")
            self.unary()
            self._term()
        else:
            pass

    def unary(self) -> None:
        if self.lookahead() == "+":
            self.match("+")
            self.unary()
        elif self.lookahead() == "-":
            self.match("-")
            self.unary()
        else:
            self.factor()

    def factor(self) -> None:
        if self.lookahead() == "(":
            self.match("(")
            self.expr()
            self.match(")")
        elif self.lookahead().isdigit():
            self.match(self.lookahead())
        else:
            self.left()


if __name__ == "__main__":
    import os
    from datetime import datetime

    file_path = os.path.abspath("../programs/prog.dl")
    parser = Parser(file=file_path)

    parser.parse()
    print(f"{datetime.utcnow()} - Execução finalizada.")
