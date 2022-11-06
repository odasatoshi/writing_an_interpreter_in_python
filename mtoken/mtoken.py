TokenType = str

class Token:
	def __init__(self, Type="", Literal=""):
		self.Type = Type
		self.Literal = Literal


ILLEGAL = "ILLEGAL"
EOF = "EOF"

IDENT = "IDENT"
INT = "INT"

ASSIGN = "="
PLUS = "+"

COMMA = ","
SEMICOLON = ";"

LPAREN = "("
RPAREN = ")"
LBRACE ="{"
RBRACE ="}"


FUNCTION = "FUNCTION"
LET = "LET"