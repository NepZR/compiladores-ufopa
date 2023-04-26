import os.path
from datetime import datetime

from parser.Parser import Parser
from lexer.Lexer import Lexer

if __name__ == "__main__":
    lexer = Lexer(file=os.path.abspath("../programs/prog_apr26_2023.dl"))
    parser = Parser(lex=lexer)

    parser.parse()
    print(f"{datetime.utcnow()} - Execução finalizada.")
