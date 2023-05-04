from lexer.Tag import Tag


class Token:
    def __init__(self, t: Tag, lex: str) -> None:
        self.tag = t
        self._lexeme = lex

    def get_tag(self) -> Tag:
        return self.tag

    def lexeme(self) -> str:
        return self._lexeme

    def __str__(self) -> str:
        return "<" + self.tag.__str__() + ", '" + self._lexeme + "'>"
