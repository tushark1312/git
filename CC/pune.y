%{
#include <stdio.h>
int yylex();
void yyerror(const char *);
%}

%union {
    char c;
}

%token <c> LETTER
%token NEWLINE

%%

input: /* empty */
    | input line

line: letters NEWLINE    { printf("\n"); }
    ;

letters: LETTER         { printf("%c", $1); }
       | letters LETTER { printf("%c", $2); }
       ;

%%

int main() {
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    printf("%s\n", s);
}