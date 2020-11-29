/*
  JSONPath grammar
*/
grammar JSONPath;

jsonpath: ROOT (expression)* EOF
        ;

expression: singleDotExpression
          | doubleDotExpression
          ;

// only limited double dot expression supported
doubleDotExpression: DOUBLE_DOT field
                   | DOUBLE_DOT bracketField
                   ;

singleDotExpression: fieldAccessor
                   | SINGLE_DOT wildcard
                   | (SINGLE_DOT)? bracketWildcard
                   | (SINGLE_DOT)? filters
                   | (SINGLE_DOT)? arraySlice
                   | (SINGLE_DOT)? union
                   ;
// filters
// only support direct field comparison (with no more nested JSONPath)
filters: '[' '?' '(' numericFilter ')' ']'
       | '[' '?' '(' stringFilter ')' ']'
       | '[' '?' '(' booleanFilter ')' ']'
       ;

numericFilter: CURRENT fieldAccessor ('>'|'<'|'==') INT
             ;

stringFilter: CURRENT fieldAccessor '==' STRING
            ;

booleanFilter: CURRENT fieldAccessor
             ;

// union
union: '[' (STRING|LETTER) (',' (STRING|LETTER))+ ']'
     ;

// array slice
arraySlice: '[' INT? ':' INT? (':' INT)? ']'
          ;

// accessors
fieldAccessor: SINGLE_DOT field
             | (SINGLE_DOT)? bracketField
             | (SINGLE_DOT)? arrayIndex
             ;

field: LETTER
     ;

bracketField: '[' (STRING|LETTER) ']'
            ;

arrayIndex: '[' INT ']'
          ;

wildcard: '*'
        ;

bracketWildcard: '[*]'
        ;

// lexer
// JSONPath specific
ROOT       : '$' ;
CURRENT    : '@' ;
SINGLE_DOT : '.' ;
DOUBLE_DOT : '..' ;

// ascii letters
LETTER      : [a-zA-Z]+ ;

// string
// the potential EOF ending is for parsing incomplete (with only single sided quote as string)
STRING     : '\'' (QUOTE|.)*? ('\''|EOF) ;
fragment
QUOTE      : '\\\'' | '\\\\';

// integer
INT        : '0' | [1-9]([0-9])* ;

// skip white spaces
WS         : [ \t\r\n]+ -> skip ;
