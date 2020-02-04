grammar CDLang;

// Parser Rules
start          : statement+ EOF;
statement      : (arrow | composition | label | style | impose)? SEPARATOR; // TODO allow no new line at end of file
arrow          : ID ':' ID '->' ID;
composition    : path '=' path;
label          : 'label' ID ':' text;
style          : 'style' ID ':' STYLE_LIST;
impose         : 'impose' ID ':' DIRECTION;
path           : ID ('.' ID)*;
text           : '[' TEXT ']' | '[]';


// Lexer Rules
TEXT           : {self._input.LA(-1) == ord('[')}? (~']' | '\\]')+;
COMMENT        : '//' ~('\n' | '\r')* NEWLINE? -> skip;
DIRECTION      : ('vertical' | 'horizontal');
ID             : [_a-zA-Z0-9]+;
STYLE_LIST     : '(' [-='_ a-zA-Z0-9]+ (',' [-='_ a-zA-Z0-9]+)* ')';
SEPARATOR      : (NEWLINE | ';' | EOF);
WHITESPACE     : (' ' | '\t') -> skip;
NEWLINE        : ('\r'? '\n' | '\r')+;
