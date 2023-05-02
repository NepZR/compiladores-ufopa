import abc


class IParser(metaclass=abc.ABCMeta):
    EOF = chr(-1)

    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def lookahead(self) -> chr:
        """
        Faz o papel de lexer. A cada chamada retorna o próximo caractere (“token”) que não é um espaço em branco.
        """
        pass

    @abc.abstractmethod
    def next(self) -> chr:
        """
        Verifica se o lookahead combina com um dado char. Ele avança para o próximo caractere caso combine,
        caso contrário imprime um erro.
        """
        pass

    @abc.abstractmethod
    def match(self, c: chr) -> None:
        """
        Imprime uma mensagem de erro, indicando a coluna onde o erro ocorreu.
        """
        pass

    @abc.abstractmethod
    def error(self, msg: str) -> None:
        """
        Método que verifica a sintaxe de uma dada string, retornando true caso ela seja aceita. Esse chama o método
        que representa o não-terminal inicial da gramática.
        """
        pass

    @abc.abstractmethod
    def parse(self) -> None:
        pass
