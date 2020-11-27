# Generated from JSONPath.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JSONPathParser import JSONPathParser
else:
    from JSONPathParser import JSONPathParser

# This class defines a complete listener for a parse tree produced by JSONPathParser.
class JSONPathListener(ParseTreeListener):

    # Enter a parse tree produced by JSONPathParser#jsonpath.
    def enterJsonpath(self, ctx:JSONPathParser.JsonpathContext):
        pass

    # Exit a parse tree produced by JSONPathParser#jsonpath.
    def exitJsonpath(self, ctx:JSONPathParser.JsonpathContext):
        pass


    # Enter a parse tree produced by JSONPathParser#recursiveChild.
    def enterRecursiveChild(self, ctx:JSONPathParser.RecursiveChildContext):
        pass

    # Exit a parse tree produced by JSONPathParser#recursiveChild.
    def exitRecursiveChild(self, ctx:JSONPathParser.RecursiveChildContext):
        pass


    # Enter a parse tree produced by JSONPathParser#dotChild.
    def enterDotChild(self, ctx:JSONPathParser.DotChildContext):
        pass

    # Exit a parse tree produced by JSONPathParser#dotChild.
    def exitDotChild(self, ctx:JSONPathParser.DotChildContext):
        pass


    # Enter a parse tree produced by JSONPathParser#bracketChild.
    def enterBracketChild(self, ctx:JSONPathParser.BracketChildContext):
        pass

    # Exit a parse tree produced by JSONPathParser#bracketChild.
    def exitBracketChild(self, ctx:JSONPathParser.BracketChildContext):
        pass


    # Enter a parse tree produced by JSONPathParser#numericFilter.
    def enterNumericFilter(self, ctx:JSONPathParser.NumericFilterContext):
        pass

    # Exit a parse tree produced by JSONPathParser#numericFilter.
    def exitNumericFilter(self, ctx:JSONPathParser.NumericFilterContext):
        pass


    # Enter a parse tree produced by JSONPathParser#stringFilter.
    def enterStringFilter(self, ctx:JSONPathParser.StringFilterContext):
        pass

    # Exit a parse tree produced by JSONPathParser#stringFilter.
    def exitStringFilter(self, ctx:JSONPathParser.StringFilterContext):
        pass


    # Enter a parse tree produced by JSONPathParser#booleanFilter.
    def enterBooleanFilter(self, ctx:JSONPathParser.BooleanFilterContext):
        pass

    # Exit a parse tree produced by JSONPathParser#booleanFilter.
    def exitBooleanFilter(self, ctx:JSONPathParser.BooleanFilterContext):
        pass


    # Enter a parse tree produced by JSONPathParser#arraySlice.
    def enterArraySlice(self, ctx:JSONPathParser.ArraySliceContext):
        pass

    # Exit a parse tree produced by JSONPathParser#arraySlice.
    def exitArraySlice(self, ctx:JSONPathParser.ArraySliceContext):
        pass


    # Enter a parse tree produced by JSONPathParser#arrayIndex.
    def enterArrayIndex(self, ctx:JSONPathParser.ArrayIndexContext):
        pass

    # Exit a parse tree produced by JSONPathParser#arrayIndex.
    def exitArrayIndex(self, ctx:JSONPathParser.ArrayIndexContext):
        pass


    # Enter a parse tree produced by JSONPathParser#union.
    def enterUnion(self, ctx:JSONPathParser.UnionContext):
        pass

    # Exit a parse tree produced by JSONPathParser#union.
    def exitUnion(self, ctx:JSONPathParser.UnionContext):
        pass


    # Enter a parse tree produced by JSONPathParser#length.
    def enterLength(self, ctx:JSONPathParser.LengthContext):
        pass

    # Exit a parse tree produced by JSONPathParser#length.
    def exitLength(self, ctx:JSONPathParser.LengthContext):
        pass


    # Enter a parse tree produced by JSONPathParser#field.
    def enterField(self, ctx:JSONPathParser.FieldContext):
        pass

    # Exit a parse tree produced by JSONPathParser#field.
    def exitField(self, ctx:JSONPathParser.FieldContext):
        pass


    # Enter a parse tree produced by JSONPathParser#bracketField.
    def enterBracketField(self, ctx:JSONPathParser.BracketFieldContext):
        pass

    # Exit a parse tree produced by JSONPathParser#bracketField.
    def exitBracketField(self, ctx:JSONPathParser.BracketFieldContext):
        pass



del JSONPathParser