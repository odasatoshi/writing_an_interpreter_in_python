from mtoken import mtoken as token

class Lexer:
    def __init__(self, _input):
        self.input = _input
        self.position = 0
        self.readPosition = 0
        self.ch = ""
        self.readChar()
    
    def NextToken(self) -> token.Token:
        tok = token.Token()

        self.skipWhitespace()

        if self.ch == "=":
            if self.peekChar() == "=":
                ch = self.ch
                self.readChar()
                literal = ch + self.ch
                tok = self.newToken(token.EQ, literal)
            else:
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
        elif self.ch == "-":
            tok = self.newToken(token.MINUS, self.ch)
        elif self.ch == "!":
            if self.peekChar() == "=":
                ch = self.ch
                self.readChar()
                literal = ch + self.ch
                tok = self.newToken(token.NOT_EQ, literal)
            else:
                tok = self.newToken(token.BANG, self.ch)
        elif self.ch == "/":
            tok = self.newToken(token.SLASH, self.ch)
        elif self.ch == "*":
            tok = self.newToken(token.ASTERISK, self.ch)
        elif self.ch == "<":
            tok = self.newToken(token.LT, self.ch)
        elif self.ch == ">":
            tok = self.newToken(token.GT, self.ch)
        elif self.ch == "{":
            tok = self.newToken(token.LBRACE, self.ch)
        elif self.ch == "}":
            tok = self.newToken(token.RBRACE, self.ch)
        else:
            if self.ch == "":
                tok = self.newToken(token.EOF, self.ch)
                return tok

            if self.isLetter(self.ch):
                tok.Literal = self.readIdentifier()
                tok.Type = tok.LookupIdent(tok.Literal)
                return tok
            elif self.isDigit(self.ch):
                tok.Type = token.INT
                tok.Literal = self.readNumber()
                return tok
            else:
                tok = self.newToken(token.ILLEGAL, self.ch)






        self.readChar()
        return tok

    def readChar(self) -> None:
        if self.readPosition >= len(self.input):
            self.ch = ""
        else:
            self.ch = self.input[self.readPosition]
        self.position = self.readPosition
        self.readPosition += 1

    def peekChar(self) -> None:
        if self.readPosition >= len(self.input):
            return ""
        else:
            return self.input[self.readPosition]


    def newToken(self, _Type, Literal):
        self.Type = _Type
        self.Literal = Literal
        return self

    def readIdentifier(self) -> str:
        position = self.position
        while self.isLetter(self.ch):
            self.readChar()
        return self.input[position:self.position]

    def readNumber(self) -> str:
        position = self.position
        while self.isDigit(self.ch):
            self.readChar()
        return self.input[position:self.position]

    def isLetter(self, ch) -> bool:
        return (str(ch).isalpha() or ch == '_')

    def isDigit(self, ch) -> bool:
        return str(ch).isdigit()

    def skipWhitespace(self):
        while self.ch == ' ' or self.ch == '\t' or self.ch == '\n' or self.ch == '\r':
            self.readChar() 