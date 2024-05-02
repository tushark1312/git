%{
#include "y.tab.h"
%}

%%

[a-z]   { yylval.c = yytext[0] - 32; return LETTER; }
[A-Z]   { yylval.c = yytext[0] + 32; return LETTER; }
\n      { return NEWLINE; }
.       { return yytext[0]; }

%%

int yywrap() {
    return 1;
}