from collections import defaultdict
TokenType = str

class Token:
	def __init__(self, Type="", Literal=""):
		self.Type = Type
		self.Literal = Literal

	def LookupIdent(self, ident):
		if ident == "":
			return EOF
		keywords = defaultdict(str)
		keywords["fn"] = FUNCTION
		keywords["let"] = LET

		if keywords[ident] == "":
			return IDENT
		else:
			return keywords[ident]

ILLEGAL = "ILLEGAL"
EOF = "EOF"

IDENT = "IDENT"
INT = "INT"

# 演算子
ASSIGN = "="
PLUS = "+"
MINUS = "-"
BANG = "!"
ASTERISK = "*"
SLASH = "/"

LT = "<"
GT = ">"

COMMA = ","
SEMICOLON = ";"

LPAREN = "("
RPAREN = ")"
LBRACE ="{"
RBRACE ="}"


FUNCTION = "FUNCTION"
LET = "LET"