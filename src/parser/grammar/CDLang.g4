grammar CDLang;

// Parser Rules
start          : SEPARATOR* statement+;
statement      : (size | arrow | composition | label | style) (SEPARATOR+ | EOF);
size           : 'size' NUMBER ',' NUMBER;
arrow          : labelledID ':' labelledID '->' labelledID STYLE_LIST?;
composition    : path '=' (path | ID) labelText?;
label          : 'label' IDENTIFIER ':' labelText;
style          : 'style' IDENTIFIER ':' STYLE_LIST;
// impose         : 'impose ' IDENTIFIER ':' DIRECTION;
path           : IDENTIFIER ('.' IDENTIFIER)*;
labelledID     : IDENTIFIER labelText?;
labelText      : '[' TEXT ']' | '[]';


// Lexer Rules
TEXT           : {self._input.LA(-1) == ord('[')}? (~']' | '\\]')+;
COMMENT        : '//' ~('\n' | '\r')* NEWLINE? -> skip;
// DIRECTION      : ('vertical' | 'horizontal');
ID             : 'ID';
// MEASUREMENT    : NUMBER ('pt' | 'mm' | 'cm' | 'in' | 'ex' | 'em' | 'mu')?;
NUMBER         : [0-9]*'.'?[0-9]+;
IDENTIFIER     : [_a-zA-Z][_a-zA-Z0-9]*;
STYLE_LIST     : '(' [-='_ a-zA-Z0-9]+ (',' [-='_ a-zA-Z0-9]+)* ')';
SEPARATOR      : (NEWLINE | ';')+;
WHITESPACE     : (' ' | '\t') -> skip;
NEWLINE        : ('\r'? '\n' | '\r')+;

// character which failed to match any other token
ERROR_CHAR     : .;
