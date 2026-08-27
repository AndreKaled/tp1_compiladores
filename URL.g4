lexer grammar URL;

URL: PROTOCOLO DOMINIO PORTA? CAMINHO?;

PROTOCOLO: 'http://' | 'https://' | 'ftp://';

DOMINIO: [a-zA-Z]+ ('.' [a-zA-Z]+)+;

CAMINHO: ('/' [a-zA-Z0-9._-]+)+;

PORTA: ':' [0-9]+;

