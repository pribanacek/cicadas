grammar CDLang;

// Parser Rules
start          : statement+;
statement      : (arrow | composition | label | style | impose) (SEPARATOR | EOF);
arrow          : ID ':' ID '->' ID;
composition    : path '=' path;
label          : 'label' ID ':' text;
style          : 'style' ID ':' text;
impose         : 'impose' ID ':' DIRECTION;
path           : ID ('.' ID)*;
text           : '(' TEXT ')' | '()';


// Lexer Rules
TEXT            : {self._input.LA(-1) == ord('(')}? (~')' | '\\)')+;
DIRECTION       : ('vertical' | 'horizontal');
ID              : [_a-zA-Z][_a-zA-Z0-9]*;
SEPARATOR       : (NEWLINE | ';')+;
WHITESPACE      : (' ' | '\t') -> skip;
NEWLINE         : ('\r'? '\n' | '\r')+;
