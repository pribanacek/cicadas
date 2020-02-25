grammar CDLang;

// Parser Rules
start          : statement+ EOF;
statement      : (size | arrow | composition | label | style | impose)? SEPARATOR; // TODO allow no new line at end of file
size          : 'size' MEASUREMENT ',' MEASUREMENT;
arrow          : labelledID ':' labelledID '->' labelledID STYLE_LIST?;
composition    : path '=' (path | IDENTITY) labelText?;
label          : 'label' ID ':' labelText;
style          : 'style' ID ':' STYLE_LIST;
impose         : 'impose' ID ':' DIRECTION;
path           : ID ('.' ID)*;
labelledID     : ID labelText?;
labelText      : '[' TEXT ']' | '[]';


// Lexer Rules
TEXT           : {self._input.LA(-1) == ord('[')}? (~']' | '\\]')+;
COMMENT        : '//' ~('\n' | '\r')* NEWLINE? -> skip;
DIRECTION      : ('vertical' | 'horizontal');
IDENTITY       : 'ID';
MEASUREMENT    : NUMBER ('pt' | 'mm' | 'cm' | 'in' | 'ex' | 'em' | 'mu')?;
NUMBER         : [0-9]*'.'?[0-9]+;
ID             : [_a-zA-Z0-9]+;
STYLE_LIST     : '(' [-='_ a-zA-Z0-9]+ (',' [-='_ a-zA-Z0-9]+)* ')';
SEPARATOR      : (NEWLINE | ';' | EOF);
WHITESPACE     : (' ' | '\t') -> skip;
NEWLINE        : ('\r'? '\n' | '\r')+;
