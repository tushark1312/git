%{
int COMMENT = 0;
%}

%%
[\t]+;
; ;
{ ;
} ;
#.* {printf("\n%s is a preprocessor directive", yytext);}

int |
float |
char |
String {printf("\n%s is a datatype", yytext);}

if |
break |
continue |
goto {printf("\n%s is a keyword", yytext);}

\+ |
\- |
\* |
\\ |
\= {printf("\n%s is an operator", yytext);}

[a-zA-Z][a-zA-Z0-9]* {printf("\n%s is an identifier", yytext);}

%%

int yywrap(){
	return (1);
}

void main(){
	yylex();
	yywrap();
}



