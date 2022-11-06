from mtoken import mtoken as token

class Lexer:
    def __init__(self, _input):
        self.input = _input
        self.position = 0
        self.readPosition = 0
        self.ch = ""
        self.readChar()
    
    def readChar(self):
        if self.readPosition >= len(self.input):
            self.ch = 0
        else:
            self.ch = self.input[self.readPosition]
        self.position = self.readPosition
        self.readPosition += 1

    def NextToken(self):
        tok = token.Token()
        if self.ch == "=":
            tok = self.newToken(token.ASSIGN, self.ch)
        elif self.ch == ";":
            tok = self.newToken(token.SEMICOLON, self.ch)
        elif self.ch == "(":
            tok = self.newToken(token.LPAREN, self.ch)
        elif self.ch == ")":
            tok = self.newToken(token.RPAREN, self.ch)
        elif self.ch == ",":
            tok = self.newToken(token.COMMA, self.ch)
        elif self.ch == "+":
            tok = self.newToken(token.PLUS, self.ch)
        elif self.ch == "{":
            tok = self.newToken(token.LBRACE, self.ch)
        elif self.ch == "}":
            tok = self.newToken(token.RBRACE, self.ch)
        else:
            tok.Literal = ""
            tok.Type = token.EOF



        self.readChar()
        return tok

    def newToken(self, _Type, Literal):
        self.Type = _Type
        self.Literal = Literal
        return self