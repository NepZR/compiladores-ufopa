import os.path

from lexer import Tag, Token, Lexer

if __name__ == "__main__":
    lexer = Lexer(file=os.path.abspath("../../Projeto/prog.dl"))
    t = lexer.next_token()

    while t.get_tag() != Tag.EOF:
        print(t)
        t = lexer.next_token()
