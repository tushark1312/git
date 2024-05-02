%{ 
/*parts of speech recognizer*/
%}

%%
[\t]+;
is |
am |
are |
ran {printf("\n%s, is a verb", yytext);}

quickly |
slowly {printf("\n%s, is an adverb", yytext);}

Ram |
Shyam {printf("\n%s, is a noun", yytext);}

[a-zA-Z]+ {printf("\n%s, is an invalid token", yytext);}
%%

int yywrap(void){
	return 1;
}

void main(){
	yylex();
	yywrap();
}