import os.path
from datetime import datetime

from parser.Parser import Parser

if __name__ == "__main__":
    file_path = os.path.abspath("programs/prog_apr26_2023.dl")
    parser = Parser(file=file_path)

    parser.parse()
    print(f"{datetime.utcnow()} - Execução finalizada.")
