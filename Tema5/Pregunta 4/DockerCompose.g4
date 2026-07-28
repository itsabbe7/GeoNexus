grammar DockerCompose;

// REGLAS SINTÁCTICAS PARSER
compose : ignore_tokens NETWORKS_KEY NEWLINE network_list ;

network_list : (SPACE IDENTIFIER COLON NEWLINE)+ ;

ignore_tokens : (~NETWORKS_KEY)* ;

// REGLAS LÉXICAS LEXER
NETWORKS_KEY : 'networks:' ;
IDENTIFIER   : [a-zA-Z0-9_-]+ ;
COLON        : ':' ;
NEWLINE      : '\r'? '\n' ;
SPACE        : [ \t]+ ;

// LA SOLUCIÓN: Cualquier otro carácter que no coincida arriba, se ignora silenciosamente
UNKNOWN_CHAR : . -> skip ;