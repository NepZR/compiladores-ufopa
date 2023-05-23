from enum import Enum


class Tag(Enum):
    PROGRAM = "PROGRAM"
    BEGIN = "BEGIN"
    END = "END"
    ASSIGN = "ASSIGN"
    ID = "ID"
    IF = "IF"
    SUM = "SUM"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"
    OR = "OR"
    AND = "AND"
    NOT = "NOT"
    NE = "NE"
    LT = "LT"
    LE = "LE"
    GT = "GT"
    GE = "GE"
    COMMENT = "COMMENT"
    SEMI = "SEMI"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    COMMA = "COMMA"
    INT = "INT"
    REAL = "REAL"
    BOOL = "BOOL"
    TRUE = "TRUE"
    FALSE = "FALSE"
    READ = "READ"
    WRITE = "WRITE"
    LIT_INT = "LIT_INT"
    LIT_REAL = "LIT_REAL"
    EOF = "EOF"
    UNK = "UNK"
    DOT = "DOT"
    TEMP = "TEMP"

    def is_int(self) -> bool:
        return self == Tag.INT

    def is_real(self) -> bool:
        return self == Tag.REAL

    def is_bool(self) -> bool:
        return self == Tag.BOOL

    def is_num(self) -> bool:
        return self.is_int() or self.is_real()

    def is_type(self) -> bool:
        return self.is_num() or self.is_bool()
