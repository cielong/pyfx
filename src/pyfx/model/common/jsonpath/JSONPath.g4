/*
  JSONPath grammar
*/
grammar JSONPath;

jsonpath: ROOT (expression)*
        ;

expression: singleDotExpression
          | doubleDotExpression
          ;

// limited double dot expression supported
doubleDotExpression: DOUBLE_DOT field
                   | DOUBLE_DOT bracketField
                   ;

singleDotExpression: fieldAccessor
                   | SINGLE_DOT wildcard
                   | (SINGLE_DOT)? bracketWildcard
                   | (SINGLE_DOT)? numericFilter
                   | (SINGLE_DOT)? stringFilter
                   | (SINGLE_DOT)? booleanFilter
                   | (SINGLE_DOT)? arraySlice
                   | (SINGLE_DOT)? union
                   | (SINGLE_DOT)? length
                   ;
// filters
// only support direct field comparison (with no more nested JSONPath)
numericFilter: '[?(' CURRENT fieldAccessor ('>'|'<'|'==') INT ')]'
             ;

stringFilter: '[?(' CURRENT fieldAccessor '==' STRING ')]'
            ;

booleanFilter: '[?(' CURRENT fieldAccessor ')]'
             ;

// union
union: '[' ((STRING (',' STRING)+)|(INT (',' INT)+)) ']'
     ;

// array slice
arraySlice: '[' INT? ':' INT? (':' INT)? ']'
          ;

// length
length: '[(' CURRENT '.length' '-' INT ')]'
      ;

// accessors
fieldAccessor: SINGLE_DOT field
             | (SINGLE_DOT)? bracketField
             | (SINGLE_DOT)? arrayIndex
             ;

field: LETTER
     ;

bracketField: '[' STRING ']'
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
STRING     : '\'' (QUOTE|.)*? '\'' ;
fragment
QUOTE      : '\\\'' | '\\\\';

// integer
INT        : '0' | [1-9]([0-9])* ;

// skip white spaces
WS         : [ \t\r\n]+ -> skip ;
