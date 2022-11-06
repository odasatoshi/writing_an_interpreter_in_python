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
            self.ch = ""
        else:
            self.ch = self.input[self.readPosition]
        self.position = self.readPosition
        self.readPosition += 1

    def NextToken(self):
        tok = token.Token()

        self.skipWhitespace()

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


    def newToken(self, _Type, Literal):
        self.Type = _Type
        self.Literal = Literal
        return self

    def readIdentifier(self):
        position = self.position
        while self.isLetter(self.ch):
            self.readChar()
        return self.input[position:self.position]

    def readNumber(self):
        position = self.position
        while self.isDigit(self.ch):
            self.readChar()
        return self.input[position:self.position]

    def isLetter(self, ch):
        return (str(ch).isalpha() or ch == '_')

    def isDigit(self, ch):
        return str(ch).isdigit()

    def skipWhitespace(self):
        while self.ch == ' ' or self.ch == '\t' or self.ch == '\n' or self.ch == '\r':
            self.readChar() 