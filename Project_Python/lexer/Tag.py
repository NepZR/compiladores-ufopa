from enum import Enum


class Tag(Enum):
    PROGRAM = "PROGRAM"
    BEGIN = "BEGIN"
    END = "END"
    ASSIGN = "ASSIGN"
    ID = "ID"
    SUM = "SUM"
    SUB = "SUB"
    MUL = "MUL"
    OR = "OR"
    LT = "LT"
    LE = "LE"
    GT = "GT"
    SEMI = "SEMI"
    LIT_INT = "LIT_INT"
    EOF = "EOF"
    UNK = "UNK"
