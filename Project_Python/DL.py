import os.path

from lexer.Tag import Tag
from lexer.Lexer import Lexer

if __name__ == "__main__":
    lexer = Lexer(file=os.path.abspath("../programs/prog.dl"))
    t = lexer.next_token()

    while t.get_tag() != Tag.EOF:
        print(t)
        t = lexer.next_token()
