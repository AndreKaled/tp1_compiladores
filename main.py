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

# isso filtra tokens ignorando o EOF
valid_tokens = [tk for tk in tokens.tokens if tk.type != -1] 

# ve se reconheceu o token principal, consumindo a entrada toda
full_url = (
    len(valid_tokens) == 1
    and lexer.symbolicNames[valid_tokens[0].type] == "URL"
    and valid_tokens[0].text == texto
)

if full_url:
    token = valid_tokens[0]
    nome = lexer.symbolicNames[token.type]
    print(f"TOKEN: {nome}")
    print(f"VALOR: {token.text}")
else:
    print("AVISO: URL completa E válida não foi reconhecida.")
    if not valid_tokens:
        print("Nenhum token reconhecido")
    else:
        print("Sub-tokens reconhecidos:")
        for token in valid_tokens:
            nome = lexer.symbolicNames[token.type]
            print(f"TOKEN: {nome}")
            print(f"VALOR: {token.text}")