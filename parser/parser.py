from mtoken import mtoken as token
from lexer import lexer
from mast import mast as ast

class Parser:
    def __init__(self):
        self.l = lexer.Lexer
        self.curToken = token.Token
        self.peekToken = token.Token

    def New(self, l):
        self.l = l
        self.nextToken()
        self.nextToken()

    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.l.NextToken()

    def parseStatement(self):
        if self.curToken.Type == token.LET:
            return self.parseLetStatement()
        else:
            return None


    def parseLetStatement(self):
        stmt = ast.LetStatement()
        stmt.Token = self.curToken

        if not self.expectPeek(token.IDENT):
            return None
        
        stmt.Name = ast.Identifier()
        stmt.Name.Token = self.curToken
        stmt.Name.Value = self.curToken.Literal

        if not self.expectPeek(token.ASSIGN):
            return None

        #TODO セミコロンまでを飛ばしているのであとで実装する

        while not self.curTokenIs(token.SEMICOLON):
            self.nextToken()

        return stmt

    def curTokenIs(self, t) -> bool:
        if self.curToken.Type == token.EOF:
            return True
        else:
            return self.curToken.Type == t

    def peekTokenIs(self, t) -> bool:
        return self.peekToken.Type == t

    def expectPeek(self, t) -> bool:
        if self.peekTokenIs(t):
            self.nextToken()
            return True
        else:
            return False


    def ParseProgram(self):

        program = ast.Program()
        program.Statements = []
        
        while self.curToken.Type != token.EOF:
            stmt = self.parseStatement()
            if stmt != None:
                program.Statements.append(stmt)
            self.nextToken()
        
        return program

