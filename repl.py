import io
import sys
from mtoken import mtoken as token
from lexer import lexer

PROMPT = ">> "

def Start(_in, _out):
    scanner = _in
    output = _out
    print(PROMPT, file=output, end="", flush=True)
    
    while True:
        scanned = scanner.readline()
        while scanned:
            l = lexer.Lexer(scanned)
            tok = l.newToken("","")
            while tok.Type != token.EOF :
                tok = l.NextToken()
                print("{Type:%s, Literal:%s}" % (tok.Type, tok.Literal) , file=output )
            print(PROMPT, file=output, end="", flush=True)
            scanned = scanner.readline()
