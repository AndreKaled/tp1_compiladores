lexer grammar URL;

URL: PROTOCOLO DOMINIO PORTA? CAMINHO QUERY? FRAGMENTO?;

PROTOCOLO: 'http://' | 'https://' | 'ftp://';

DOMINIO: [a-zA-Z]+ ('.' [a-zA-Z]+)+;

CAMINHO: ('/' [a-zA-Z0-9._-]+)+;

PORTA: ':' [0-9]+;

QUERY: '?' PARAMETRO ('&' PARAMETRO)*;

fragment PARAMETRO: [a-zA-Z0-9]+ '=' [a-zA-Z0-9]+;

FRAGMENTO: '#' [a-zA-Z0-9]+;