FROM python:3.12-slim

ARG ANTLR_VERSION=4.13.2

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        default-jre-headless \
        curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL \
    "https://www.antlr.org/download/antlr-${ANTLR_VERSION}-complete.jar" \
    -o /opt/antlr.jar

RUN pip install --no-cache-dir \
    "antlr4-python3-runtime==${ANTLR_VERSION}"

RUN printf '#!/bin/sh\nexec java -jar /opt/antlr.jar "$@"\n' \
    > /usr/local/bin/antlr4 \
    && chmod +x /usr/local/bin/antlr4

WORKDIR /app

RUN printf '#!/bin/sh\n\
set -e\n\
echo "==> Gerando lexer..." \n\
rm -rf /tmp/antlr-generated\n\
antlr4 -Dlanguage=Python3 -o /tmp/antlr-generated URL.g4\n\
echo "==> Executando..." \n\
PYTHONPATH=/tmp/antlr-generated python3 main.py "$@"\n' \
    > /usr/local/bin/run-url \
    && chmod +x /usr/local/bin/run-url

ENTRYPOINT ["run-url"]