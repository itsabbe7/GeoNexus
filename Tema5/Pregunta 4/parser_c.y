%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void yyerror(const char *s);
int yylex(void);
%}
%union { char* str; }
%token NETWORKS_KEY COLON NEWLINE SPACE
%token <str> IDENTIFIER
%%
compose:
    NETWORKS_KEY NEWLINE network_list
    ;

network_list:
    SPACE IDENTIFIER COLON NEWLINE { printf("Red (C/Bison): %s\n", $2); }
    | network_list SPACE IDENTIFIER COLON NEWLINE { printf("Red (C/Bison): %s\n", $3); }
    ;
%%
void yyerror(const char *s) { }
int main(int argc, char **argv) {
    extern FILE *yyin;
    yyin = fopen(argv[1], "r");
    yyparse();
    return 0;
}