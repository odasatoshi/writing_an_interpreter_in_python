from collections import defaultdict
TokenType = str

class Token:
	def __init__(self, Type="", Literal=""):
		self.Type = Type
		self.Literal = Literal

	def LookupIdent(self, ident) -> str:
		if ident == "":
			return EOF
		keywords = defaultdict(str)
		keywords["fn"] = FUNCTION
		keywords["let"] = LET
		keywords["true"] = TRUE 
		keywords["false"] = FALSE  
		keywords["if"] = IF  
		keywords["else"] = ELSE 
		keywords["return"] = RETURN  

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

EQ = "=="
NOT_EQ = "!="

COMMA = ","
SEMICOLON = ";"

LPAREN = "("
RPAREN = ")"
LBRACE ="{"
RBRACE ="}"

# 予約語
FUNCTION = "FUNCTION"
LET = "LET"

TRUE = "TRUE"
FALSE = "FALSE"
IF = "IF"
ELSE = "ELSE"
RETURN = "RETURN"
