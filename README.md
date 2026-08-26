# TP1 — Análise Léxica: Reconhecimento de URLs

Trabalho 01 da disciplina de Compiladores, desenvolvido para implementar um analisador léxico capaz de reconhecer URLs utilizando **ANTLR** e **Python**.

## Sobre o trabalho

O analisador deve identificar URLs compostas pelas seguintes partes:

* Protocolo opcional: `http`, `https` ou `ftp`
* Domínio
* Porta opcional
* Caminho opcional
* Parâmetros de consulta (`query`) opcionais
* Fragmento opcional

O trabalho utiliza uma **lexer grammar** do ANTLR, com expressões regulares para reconhecer os componentes das URLs.

O programa Python recebe uma URL como argumento e informa os tokens reconhecidos. Quando o token principal não é reconhecido, os sub-tokens identificados devem ser apresentados, juntamente com uma mensagem de erro ou aviso.

## Tecnologias

* Python 3.12
* ANTLR 4.13.2
* Docker

## Como executar

É necessário ter o Docker e o Docker Compose instalados.

Primeiro, construa a imagem:

```bash
docker compose build
```

Depois, execute o programa passando a URL como argumento:

```bash
docker compose run --rm antlr "https://www.example.com/path?user=123#section"
```

A gramática `URL.g4` é automaticamente processada pelo ANTLR antes da execução do programa Python.

Não é necessário executar `docker compose build` novamente ao alterar `URL.g4` ou `main.py`. Basta executar o comando novamente.

## Estrutura

```text
.
├── Dockerfile
├── docker-compose.yml
├── URL.g4
├── main.py
└── README.md
```

Os arquivos `URL.g4` e `main.py` correspondem aos arquivos exigidos para a entrega do trabalho.
