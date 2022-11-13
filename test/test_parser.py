from mtoken import mtoken as token
from lexer import lexer
from parser import parser

_input = """
let x = 5;
let y = 10;
let foobar = 838383;
"""

class TestLetStatements():
    def test_input(self):
        l = lexer.Lexer(_input)
        p = parser.Parser()
        p.New(l)

        program = p.ParseProgram()

        assert program != None
        assert len(program.Statements) == 3




        tests = [
            "x",
            "y",
            "foobar"
        ]

        for i in range(len(tests)):
            stmt = program.Statements[i]
            assert stmt.Name.Value == tests[i]
