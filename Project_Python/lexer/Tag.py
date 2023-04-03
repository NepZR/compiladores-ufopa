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
    AND = "LAND"
    NOT = "NOT"
    NE = "NE"
    LT = "LT"
    LE = "LE"
    GT = "GT"
    GE = "GE"
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