/*
  JSONPath grammar
*/
grammar JSONPath;

jsonpath: ROOT (expression)*
        ;

expression: '..' (field | bracketField)                                      # recursiveChild
          | '.' (field | bracketField)                                       # dotChild
          | bracketField                                                     # bracketChild
          | ('.'|'..')? '[?(' CURRENT (expression)* ('<'|'>'|'==') INT ')]'  # numericFilter
          | ('.'|'..')? '[?(' CURRENT (expression)* '==' STRING ')]'         # stringFilter
          | ('.'|'..')? '[?(' CURRENT (expression)* ')]'                     # booleanFilter
          | ('.'|'..')? '[' INT? ':' INT? (':' INT)? ']'                     # arraySlice
          | ('.'|'..')? '[' INT ']'                                          # arrayIndex
          | ('.'|'..')? '[' ((STRING (',' STRING)+) | (INT (',' INT)+)) ']'  # union
          | ('.'|'..')? '[(' CURRENT '.length' '-' INT ')]'                  # length
          ;

field: ASCII
     | '*'
     ;

bracketField: '[' STRING ']'
                ;

// lexer
ROOT       : '$' ;
CURRENT    : '@' ;
ASCII      : [a-zA-Z]+ ;
STRING     : '\'' (QUOTE|.)*? '\'' ;
INT        : '0' | [1-9]([0-9])* ;
WS         : [ \t\r\n]+ -> skip ;

fragment
QUOTE      : '\\\'' | '\\\\';
