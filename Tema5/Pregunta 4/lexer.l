%{
#include "parser.tab.h"
%}
%%
^"networks:"      { return NETWORKS_KEY; }
[a-zA-Z0-9_-]+    { yylval.str = strdup(yytext); return IDENTIFIER; }
":"               { return COLON; }
\n                { return NEWLINE; }
[ \t]+            { return SPACE; }
.                 { /* ignorar el resto */ }
%%
int yywrap() { return 1; }