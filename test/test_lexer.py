from mtoken import mtoken as token
from lexer import lexer

_input = "=+(){},;"

class TestNextToken():


    def test_input(self):
        tests = [
            token.Token(token.ASSIGN , "="),
            token.Token(token.PLUS , "+"),
            token.Token(token.LPAREN , "("),
            token.Token(token.RPAREN , ")"),
            token.Token(token.LBRACE , "{"),
            token.Token(token.RBRACE , "}"),
            token.Token(token.COMMA , ","),
            token.Token(token.SEMICOLON , ";"),
            token.Token(token.EOF , "")]
        l = lexer.Lexer(_input)

        for tt in tests:
            tok = l.NextToken()
            print(tok.Literal)
            assert tok.Type == tt.Type
            assert tok.Literal == tt.Literal


