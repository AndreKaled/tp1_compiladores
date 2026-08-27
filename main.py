import sys

from antlr4 import InputStream, CommonTokenStream
from URL import URL

if len(sys.argv) != 2:
    print(f"Uso: python3 main.py <URL>")
    exit(1)

texto = sys.argv[1]

input_stream = InputStream(texto)
lexer = URL(input_stream)
tokens = CommonTokenStream(lexer)

tokens.fill()

for token in tokens.tokens:
    if token.type != -1: # EOF
        nome = lexer.symbolicNames[token.type]
        print(f"TOKEN: {nome}")
        print(f"VALOR: {token.text}")