from mtoken import mtoken as token
from lexer import lexer

_input = "=+(){},;"

_input2 = """let five = 5;
let ten = 10;

let add = fn(x, y) {
    x + y;
};

let result = add(five, ten);
!-/*5;
5 < 10 > 5;

if (5 < 10) {
    return true;
} else {
    return false;
}

10 == 10;
10 != 9;
"""

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
            assert tok.Type == tt.Type
            assert tok.Literal == tt.Literal

    def test_input2(self):
        tests = [
            token.Token(token.LET , "let"),
            token.Token(token.IDENT , "five"),
            token.Token(token.ASSIGN , "="),
            token.Token(token.INT , "5"),
            token.Token(token.SEMICOLON , ";"),
            token.Token(token.LET , "let"),
            token.Token(token.IDENT , "ten"),
            token.Token(token.ASSIGN , "="),
            token.Token(token.INT , "10"),
            token.Token(token.SEMICOLON , ";"),
            token.Token(token.LET , "let"),
            token.Token(token.IDENT , "add"),
            token.Token(token.ASSIGN , "="),
            token.Token(token.FUNCTION , "fn"),
            token.Token(token.LPAREN , "("),
            token.Token(token.IDENT , "x"),
            token.Token(token.COMMA , ","),
            token.Token(token.IDENT , "y"),
            token.Token(token.RPAREN , ")"),
            token.Token(token.LBRACE , "{"),
            token.Token(token.IDENT , "x"),
            token.Token(token.PLUS , "+"),
            token.Token(token.IDENT , "y"),
            token.Token(token.SEMICOLON , ";"),
            token.Token(token.RBRACE , "}"),
            token.Token(token.SEMICOLON , ";"),
            token.Token(token.LET , "let"),
            token.Token(token.IDENT , "result"),
            token.Token(token.ASSIGN , "="),
            token.Token(token.IDENT , "add"),
            token.Token(token.LPAREN , "("),
            token.Token(token.IDENT , "five"),
            token.Token(token.COMMA , ","),
            token.Token(token.IDENT , "ten"),
            token.Token(token.RPAREN , ")"),
            token.Token(token.SEMICOLON , ";"),
            token.Token(token.BANG, "!"),
            token.Token(token.MINUS, "-"),
            token.Token(token.SLASH, "/"),
            token.Token(token.ASTERISK, "*"),
            token.Token(token.INT, "5"),
            token.Token(token.SEMICOLON , ";"),
            token.Token(token.INT, "5"),
            token.Token(token.LT, "<"),
            token.Token(token.INT, "10"),
            token.Token(token.GT, ">"),
            token.Token(token.INT, "5"),
            token.Token(token.SEMICOLON , ";"),
            token.Token(token.IF, "if"),
            token.Token(token.LPAREN , "("),
            token.Token(token.INT, "5"),
            token.Token(token.LT, "<"),
            token.Token(token.INT, "10"),
            token.Token(token.RPAREN , ")"),
            token.Token(token.LBRACE , "{"),
            token.Token(token.RETURN , "return"),
            token.Token(token.TRUE , "true"),
            token.Token(token.SEMICOLON , ";"),
            token.Token(token.RBRACE , "}"),
            token.Token(token.ELSE , "else"),
            token.Token(token.LBRACE , "{"),
            token.Token(token.RETURN , "return"),
            token.Token(token.FALSE , "false"),
            token.Token(token.SEMICOLON , ";"),
            token.Token(token.RBRACE , "}"),
            token.Token(token.INT, "10"),
            token.Token(token.EQ, "=="),
            token.Token(token.INT, "10"),
            token.Token(token.SEMICOLON , ";"),
            token.Token(token.INT, "10"),
            token.Token(token.NOT_EQ, "!="),
            token.Token(token.INT, "9"),
            token.Token(token.SEMICOLON , ";"),
            token.Token(token.EOF , "")]


        l = lexer.Lexer(_input2)

        for tt in tests:
            tok = l.NextToken()
            assert tok.Type == tt.Type
            assert tok.Literal == tt.Literal

