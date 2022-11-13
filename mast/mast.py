from abc import ABCMeta, abstractmethod
from mtoken import mtoken as token

class Node:
    @abstractmethod
    def TokenLiteral(metaclass=ABCMeta) -> str:
        raise NotImplementedError()

class Statement:
    def __init__(self) -> None:
        self.Node = None
    @abstractmethod
    def statementNode(metaclass=ABCMeta):
        raise NotImplementedError()

class Expression:
    def __init__(self) -> None:
        self.Node = None
    @abstractmethod
    def expressionNode(metaclass=ABCMeta):
        raise NotImplementedError()



class Program:
    def __init__(self) -> None:
        self.Statements = []

    def TokenLiteral(self) -> str:
        if len(self.Statements) > 0:
            return self.Statements[0].TokenLiteral()
        else:
            return ""


class LetStatement:
    def __init__(self) -> None:
        self.Token = token.Token()
        self.Name = Identifier
        self.Value = Expression

    def statementNode(self):
        return None

    def TokenLiteral(self) -> str:
        return self.Token.Literal

class Identifier:
    def __init__(self) -> None:
        self.Token = token.Token()
        self.Value = str

    def expressionNode(self):
        return None

    def TokenLiteral(self) -> str:
        return self.Token.Literal
