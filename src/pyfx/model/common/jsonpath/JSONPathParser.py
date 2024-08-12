# Generated from JSONPath.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 20, 159, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13,
        2, 14, 7, 14, 2, 15, 7, 15, 1, 0, 1, 0, 5, 0, 35, 8, 0, 10, 0, 12, 0, 38, 9, 0, 1, 0, 1, 0,
        1, 1, 1, 1, 3, 1, 44, 8, 1, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 50, 8, 2, 1, 3, 1, 3, 1, 3, 1, 3, 3,
        3, 56, 8, 3, 1, 3, 1, 3, 3, 3, 60, 8, 3, 1, 3, 1, 3, 3, 3, 64, 8, 3, 1, 3, 1, 3, 3, 3, 68, 8,
        3, 1, 3, 3, 3, 71, 8, 3, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4,
        1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 3, 4, 94, 8, 4, 1, 5, 1, 5, 1, 5, 1, 5, 1,
        5, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 7, 1, 7, 1, 7, 1, 8, 1, 8, 1, 8, 1, 8, 4, 8, 113, 8, 8, 11,
        8, 12, 8, 114, 1, 8, 1, 8, 1, 9, 1, 9, 3, 9, 121, 8, 9, 1, 9, 1, 9, 3, 9, 125, 8, 9, 1, 9, 1,
        9, 3, 9, 129, 8, 9, 1, 9, 1, 9, 1, 10, 1, 10, 1, 10, 3, 10, 136, 8, 10, 1, 10, 1, 10, 3, 10,
        140, 8, 10, 1, 10, 3, 10, 143, 8, 10, 1, 11, 1, 11, 1, 12, 1, 12, 1, 12, 1, 12, 1, 13, 1,
        13, 1, 13, 1, 13, 1, 14, 1, 14, 1, 15, 1, 15, 1, 15, 0, 0, 16, 0, 2, 4, 6, 8, 10, 12, 14,
        16, 18, 20, 22, 24, 26, 28, 30, 0, 2, 1, 0, 6, 8, 1, 0, 17, 18, 164, 0, 32, 1, 0, 0, 0, 2,
        43, 1, 0, 0, 0, 4, 49, 1, 0, 0, 0, 6, 70, 1, 0, 0, 0, 8, 93, 1, 0, 0, 0, 10, 95, 1, 0, 0, 0,
        12, 100, 1, 0, 0, 0, 14, 105, 1, 0, 0, 0, 16, 108, 1, 0, 0, 0, 18, 118, 1, 0, 0, 0, 20, 142,
        1, 0, 0, 0, 22, 144, 1, 0, 0, 0, 24, 146, 1, 0, 0, 0, 26, 150, 1, 0, 0, 0, 28, 154, 1, 0,
        0, 0, 30, 156, 1, 0, 0, 0, 32, 36, 5, 13, 0, 0, 33, 35, 3, 2, 1, 0, 34, 33, 1, 0, 0, 0, 35,
        38, 1, 0, 0, 0, 36, 34, 1, 0, 0, 0, 36, 37, 1, 0, 0, 0, 37, 39, 1, 0, 0, 0, 38, 36, 1, 0, 0,
        0, 39, 40, 5, 0, 0, 1, 40, 1, 1, 0, 0, 0, 41, 44, 3, 6, 3, 0, 42, 44, 3, 4, 2, 0, 43, 41, 1,
        0, 0, 0, 43, 42, 1, 0, 0, 0, 44, 3, 1, 0, 0, 0, 45, 46, 5, 16, 0, 0, 46, 50, 3, 22, 11, 0,
        47, 48, 5, 16, 0, 0, 48, 50, 3, 24, 12, 0, 49, 45, 1, 0, 0, 0, 49, 47, 1, 0, 0, 0, 50, 5,
        1, 0, 0, 0, 51, 71, 3, 20, 10, 0, 52, 53, 5, 15, 0, 0, 53, 71, 3, 28, 14, 0, 54, 56, 5, 15,
        0, 0, 55, 54, 1, 0, 0, 0, 55, 56, 1, 0, 0, 0, 56, 57, 1, 0, 0, 0, 57, 71, 3, 30, 15, 0, 58,
        60, 5, 15, 0, 0, 59, 58, 1, 0, 0, 0, 59, 60, 1, 0, 0, 0, 60, 61, 1, 0, 0, 0, 61, 71, 3, 8,
        4, 0, 62, 64, 5, 15, 0, 0, 63, 62, 1, 0, 0, 0, 63, 64, 1, 0, 0, 0, 64, 65, 1, 0, 0, 0, 65,
        71, 3, 18, 9, 0, 66, 68, 5, 15, 0, 0, 67, 66, 1, 0, 0, 0, 67, 68, 1, 0, 0, 0, 68, 69, 1, 0,
        0, 0, 69, 71, 3, 16, 8, 0, 70, 51, 1, 0, 0, 0, 70, 52, 1, 0, 0, 0, 70, 55, 1, 0, 0, 0, 70,
        59, 1, 0, 0, 0, 70, 63, 1, 0, 0, 0, 70, 67, 1, 0, 0, 0, 71, 7, 1, 0, 0, 0, 72, 73, 5, 1, 0,
        0, 73, 74, 5, 2, 0, 0, 74, 75, 5, 3, 0, 0, 75, 76, 3, 10, 5, 0, 76, 77, 5, 4, 0, 0, 77, 78,
        5, 5, 0, 0, 78, 94, 1, 0, 0, 0, 79, 80, 5, 1, 0, 0, 80, 81, 5, 2, 0, 0, 81, 82, 5, 3, 0, 0,
        82, 83, 3, 12, 6, 0, 83, 84, 5, 4, 0, 0, 84, 85, 5, 5, 0, 0, 85, 94, 1, 0, 0, 0, 86, 87, 5,
        1, 0, 0, 87, 88, 5, 2, 0, 0, 88, 89, 5, 3, 0, 0, 89, 90, 3, 14, 7, 0, 90, 91, 5, 4, 0, 0, 91,
        92, 5, 5, 0, 0, 92, 94, 1, 0, 0, 0, 93, 72, 1, 0, 0, 0, 93, 79, 1, 0, 0, 0, 93, 86, 1, 0, 0,
        0, 94, 9, 1, 0, 0, 0, 95, 96, 5, 14, 0, 0, 96, 97, 3, 20, 10, 0, 97, 98, 7, 0, 0, 0, 98, 99,
        5, 19, 0, 0, 99, 11, 1, 0, 0, 0, 100, 101, 5, 14, 0, 0, 101, 102, 3, 20, 10, 0, 102, 103,
        5, 8, 0, 0, 103, 104, 5, 18, 0, 0, 104, 13, 1, 0, 0, 0, 105, 106, 5, 14, 0, 0, 106, 107,
        3, 20, 10, 0, 107, 15, 1, 0, 0, 0, 108, 109, 5, 1, 0, 0, 109, 112, 7, 1, 0, 0, 110, 111,
        5, 9, 0, 0, 111, 113, 7, 1, 0, 0, 112, 110, 1, 0, 0, 0, 113, 114, 1, 0, 0, 0, 114, 112,
        1, 0, 0, 0, 114, 115, 1, 0, 0, 0, 115, 116, 1, 0, 0, 0, 116, 117, 5, 5, 0, 0, 117, 17, 1,
        0, 0, 0, 118, 120, 5, 1, 0, 0, 119, 121, 5, 19, 0, 0, 120, 119, 1, 0, 0, 0, 120, 121, 1,
        0, 0, 0, 121, 122, 1, 0, 0, 0, 122, 124, 5, 10, 0, 0, 123, 125, 5, 19, 0, 0, 124, 123,
        1, 0, 0, 0, 124, 125, 1, 0, 0, 0, 125, 128, 1, 0, 0, 0, 126, 127, 5, 10, 0, 0, 127, 129,
        5, 19, 0, 0, 128, 126, 1, 0, 0, 0, 128, 129, 1, 0, 0, 0, 129, 130, 1, 0, 0, 0, 130, 131,
        5, 5, 0, 0, 131, 19, 1, 0, 0, 0, 132, 133, 5, 15, 0, 0, 133, 143, 3, 22, 11, 0, 134, 136,
        5, 15, 0, 0, 135, 134, 1, 0, 0, 0, 135, 136, 1, 0, 0, 0, 136, 137, 1, 0, 0, 0, 137, 143,
        3, 24, 12, 0, 138, 140, 5, 15, 0, 0, 139, 138, 1, 0, 0, 0, 139, 140, 1, 0, 0, 0, 140, 141,
        1, 0, 0, 0, 141, 143, 3, 26, 13, 0, 142, 132, 1, 0, 0, 0, 142, 135, 1, 0, 0, 0, 142, 139,
        1, 0, 0, 0, 143, 21, 1, 0, 0, 0, 144, 145, 5, 17, 0, 0, 145, 23, 1, 0, 0, 0, 146, 147, 5,
        1, 0, 0, 147, 148, 7, 1, 0, 0, 148, 149, 5, 5, 0, 0, 149, 25, 1, 0, 0, 0, 150, 151, 5, 1,
        0, 0, 151, 152, 5, 19, 0, 0, 152, 153, 5, 5, 0, 0, 153, 27, 1, 0, 0, 0, 154, 155, 5, 11,
        0, 0, 155, 29, 1, 0, 0, 0, 156, 157, 5, 12, 0, 0, 157, 31, 1, 0, 0, 0, 16, 36, 43, 49, 55,
        59, 63, 67, 70, 93, 114, 120, 124, 128, 135, 139, 142
    ]


class JSONPathParser (Parser):

    grammarFileName = "JSONPath.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'['", "'?'", "'('", "')'", "']'", "'>'",
                    "'<'", "'=='", "','", "':'", "'*'", "'[*]'", "'$'",
                    "'@'", "'.'", "'..'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "ROOT", "CURRENT", "SINGLE_DOT", "DOUBLE_DOT",
                     "LETTER", "STRING", "INT", "WS"]

    RULE_jsonpath = 0
    RULE_expression = 1
    RULE_doubleDotExpression = 2
    RULE_singleDotExpression = 3
    RULE_filters = 4
    RULE_numericFilter = 5
    RULE_stringFilter = 6
    RULE_booleanFilter = 7
    RULE_union = 8
    RULE_arraySlice = 9
    RULE_fieldAccessor = 10
    RULE_field = 11
    RULE_bracketField = 12
    RULE_arrayIndex = 13
    RULE_wildcard = 14
    RULE_bracketWildcard = 15

    ruleNames = ["jsonpath", "expression", "doubleDotExpression", "singleDotExpression",
                 "filters", "numericFilter", "stringFilter", "booleanFilter",
                 "union", "arraySlice", "fieldAccessor", "field", "bracketField",
                 "arrayIndex", "wildcard", "bracketWildcard"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    ROOT = 13
    CURRENT = 14
    SINGLE_DOT = 15
    DOUBLE_DOT = 16
    LETTER = 17
    STRING = 18
    INT = 19
    WS = 20

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class JsonpathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROOT(self):
            return self.getToken(JSONPathParser.ROOT, 0)

        def EOF(self):
            return self.getToken(JSONPathParser.EOF, 0)

        def expression(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(JSONPathParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JSONPathParser.ExpressionContext, i)

        def getRuleIndex(self):
            return JSONPathParser.RULE_jsonpath

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterJsonpath"):
                listener.enterJsonpath(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitJsonpath"):
                listener.exitJsonpath(self)

    def jsonpath(self):

        localctx = JSONPathParser.JsonpathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_jsonpath)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(JSONPathParser.ROOT)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 102402) != 0):
                self.state = 33
                self.expression()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(JSONPathParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleDotExpression(self):
            return self.getTypedRuleContext(JSONPathParser.SingleDotExpressionContext, 0)

        def doubleDotExpression(self):
            return self.getTypedRuleContext(JSONPathParser.DoubleDotExpressionContext, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_expression

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpression"):
                listener.enterExpression(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpression"):
                listener.exitExpression(self)

    def expression(self):

        localctx = JSONPathParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 12, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.singleDotExpression()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.doubleDotExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DoubleDotExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_DOT(self):
            return self.getToken(JSONPathParser.DOUBLE_DOT, 0)

        def field(self):
            return self.getTypedRuleContext(JSONPathParser.FieldContext, 0)

        def bracketField(self):
            return self.getTypedRuleContext(JSONPathParser.BracketFieldContext, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_doubleDotExpression

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDoubleDotExpression"):
                listener.enterDoubleDotExpression(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDoubleDotExpression"):
                listener.exitDoubleDotExpression(self)

    def doubleDotExpression(self):

        localctx = JSONPathParser.DoubleDotExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_doubleDotExpression)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 2, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(JSONPathParser.DOUBLE_DOT)
                self.state = 46
                self.field()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(JSONPathParser.DOUBLE_DOT)
                self.state = 48
                self.bracketField()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SingleDotExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldAccessor(self):
            return self.getTypedRuleContext(JSONPathParser.FieldAccessorContext, 0)

        def SINGLE_DOT(self):
            return self.getToken(JSONPathParser.SINGLE_DOT, 0)

        def wildcard(self):
            return self.getTypedRuleContext(JSONPathParser.WildcardContext, 0)

        def bracketWildcard(self):
            return self.getTypedRuleContext(JSONPathParser.BracketWildcardContext, 0)

        def filters(self):
            return self.getTypedRuleContext(JSONPathParser.FiltersContext, 0)

        def arraySlice(self):
            return self.getTypedRuleContext(JSONPathParser.ArraySliceContext, 0)

        def union(self):
            return self.getTypedRuleContext(JSONPathParser.UnionContext, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_singleDotExpression

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSingleDotExpression"):
                listener.enterSingleDotExpression(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSingleDotExpression"):
                listener.exitSingleDotExpression(self)

    def singleDotExpression(self):

        localctx = JSONPathParser.SingleDotExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_singleDotExpression)
        self._la = 0  # Token type
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 7, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.fieldAccessor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(JSONPathParser.SINGLE_DOT)
                self.state = 53
                self.wildcard()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 15:
                    self.state = 54
                    self.match(JSONPathParser.SINGLE_DOT)

                self.state = 57
                self.bracketWildcard()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 15:
                    self.state = 58
                    self.match(JSONPathParser.SINGLE_DOT)

                self.state = 61
                self.filters()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 15:
                    self.state = 62
                    self.match(JSONPathParser.SINGLE_DOT)

                self.state = 65
                self.arraySlice()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 15:
                    self.state = 66
                    self.match(JSONPathParser.SINGLE_DOT)

                self.state = 69
                self.union()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FiltersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericFilter(self):
            return self.getTypedRuleContext(JSONPathParser.NumericFilterContext, 0)

        def stringFilter(self):
            return self.getTypedRuleContext(JSONPathParser.StringFilterContext, 0)

        def booleanFilter(self):
            return self.getTypedRuleContext(JSONPathParser.BooleanFilterContext, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_filters

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFilters"):
                listener.enterFilters(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFilters"):
                listener.exitFilters(self)

    def filters(self):

        localctx = JSONPathParser.FiltersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_filters)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 8, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(JSONPathParser.T__0)
                self.state = 73
                self.match(JSONPathParser.T__1)
                self.state = 74
                self.match(JSONPathParser.T__2)
                self.state = 75
                self.numericFilter()
                self.state = 76
                self.match(JSONPathParser.T__3)
                self.state = 77
                self.match(JSONPathParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(JSONPathParser.T__0)
                self.state = 80
                self.match(JSONPathParser.T__1)
                self.state = 81
                self.match(JSONPathParser.T__2)
                self.state = 82
                self.stringFilter()
                self.state = 83
                self.match(JSONPathParser.T__3)
                self.state = 84
                self.match(JSONPathParser.T__4)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.match(JSONPathParser.T__0)
                self.state = 87
                self.match(JSONPathParser.T__1)
                self.state = 88
                self.match(JSONPathParser.T__2)
                self.state = 89
                self.booleanFilter()
                self.state = 90
                self.match(JSONPathParser.T__3)
                self.state = 91
                self.match(JSONPathParser.T__4)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericFilterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CURRENT(self):
            return self.getToken(JSONPathParser.CURRENT, 0)

        def fieldAccessor(self):
            return self.getTypedRuleContext(JSONPathParser.FieldAccessorContext, 0)

        def INT(self):
            return self.getToken(JSONPathParser.INT, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_numericFilter

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNumericFilter"):
                listener.enterNumericFilter(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNumericFilter"):
                listener.exitNumericFilter(self)

    def numericFilter(self):

        localctx = JSONPathParser.NumericFilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_numericFilter)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(JSONPathParser.CURRENT)
            self.state = 96
            self.fieldAccessor()
            self.state = 97
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 98
            self.match(JSONPathParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringFilterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CURRENT(self):
            return self.getToken(JSONPathParser.CURRENT, 0)

        def fieldAccessor(self):
            return self.getTypedRuleContext(JSONPathParser.FieldAccessorContext, 0)

        def STRING(self):
            return self.getToken(JSONPathParser.STRING, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_stringFilter

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStringFilter"):
                listener.enterStringFilter(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStringFilter"):
                listener.exitStringFilter(self)

    def stringFilter(self):

        localctx = JSONPathParser.StringFilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stringFilter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(JSONPathParser.CURRENT)
            self.state = 101
            self.fieldAccessor()
            self.state = 102
            self.match(JSONPathParser.T__7)
            self.state = 103
            self.match(JSONPathParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BooleanFilterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CURRENT(self):
            return self.getToken(JSONPathParser.CURRENT, 0)

        def fieldAccessor(self):
            return self.getTypedRuleContext(JSONPathParser.FieldAccessorContext, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_booleanFilter

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBooleanFilter"):
                listener.enterBooleanFilter(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBooleanFilter"):
                listener.exitBooleanFilter(self)

    def booleanFilter(self):

        localctx = JSONPathParser.BooleanFilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_booleanFilter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(JSONPathParser.CURRENT)
            self.state = 106
            self.fieldAccessor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i: int = None):
            if i is None:
                return self.getTokens(JSONPathParser.STRING)
            else:
                return self.getToken(JSONPathParser.STRING, i)

        def LETTER(self, i: int = None):
            if i is None:
                return self.getTokens(JSONPathParser.LETTER)
            else:
                return self.getToken(JSONPathParser.LETTER, i)

        def getRuleIndex(self):
            return JSONPathParser.RULE_union

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterUnion"):
                listener.enterUnion(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitUnion"):
                listener.exitUnion(self)

    def union(self):

        localctx = JSONPathParser.UnionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_union)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(JSONPathParser.T__0)
            self.state = 109
            _la = self._input.LA(1)
            if not (_la == 17 or _la == 18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 110
                self.match(JSONPathParser.T__8)
                self.state = 111
                _la = self._input.LA(1)
                if not (_la == 17 or _la == 18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == 9):
                    break

            self.state = 116
            self.match(JSONPathParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArraySliceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i: int = None):
            if i is None:
                return self.getTokens(JSONPathParser.INT)
            else:
                return self.getToken(JSONPathParser.INT, i)

        def getRuleIndex(self):
            return JSONPathParser.RULE_arraySlice

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArraySlice"):
                listener.enterArraySlice(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArraySlice"):
                listener.exitArraySlice(self)

    def arraySlice(self):

        localctx = JSONPathParser.ArraySliceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arraySlice)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(JSONPathParser.T__0)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 19:
                self.state = 119
                self.match(JSONPathParser.INT)

            self.state = 122
            self.match(JSONPathParser.T__9)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 19:
                self.state = 123
                self.match(JSONPathParser.INT)

            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 10:
                self.state = 126
                self.match(JSONPathParser.T__9)
                self.state = 127
                self.match(JSONPathParser.INT)

            self.state = 130
            self.match(JSONPathParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FieldAccessorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_DOT(self):
            return self.getToken(JSONPathParser.SINGLE_DOT, 0)

        def field(self):
            return self.getTypedRuleContext(JSONPathParser.FieldContext, 0)

        def bracketField(self):
            return self.getTypedRuleContext(JSONPathParser.BracketFieldContext, 0)

        def arrayIndex(self):
            return self.getTypedRuleContext(JSONPathParser.ArrayIndexContext, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_fieldAccessor

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFieldAccessor"):
                listener.enterFieldAccessor(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFieldAccessor"):
                listener.exitFieldAccessor(self)

    def fieldAccessor(self):

        localctx = JSONPathParser.FieldAccessorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_fieldAccessor)
        self._la = 0  # Token type
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 15, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(JSONPathParser.SINGLE_DOT)
                self.state = 133
                self.field()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 15:
                    self.state = 134
                    self.match(JSONPathParser.SINGLE_DOT)

                self.state = 137
                self.bracketField()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 15:
                    self.state = 138
                    self.match(JSONPathParser.SINGLE_DOT)

                self.state = 141
                self.arrayIndex()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self):
            return self.getToken(JSONPathParser.LETTER, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_field

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterField"):
                listener.enterField(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitField"):
                listener.exitField(self)

    def field(self):

        localctx = JSONPathParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(JSONPathParser.LETTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BracketFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONPathParser.STRING, 0)

        def LETTER(self):
            return self.getToken(JSONPathParser.LETTER, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_bracketField

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBracketField"):
                listener.enterBracketField(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBracketField"):
                listener.exitBracketField(self)

    def bracketField(self):

        localctx = JSONPathParser.BracketFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_bracketField)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(JSONPathParser.T__0)
            self.state = 147
            _la = self._input.LA(1)
            if not (_la == 17 or _la == 18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 148
            self.match(JSONPathParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayIndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(JSONPathParser.INT, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_arrayIndex

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArrayIndex"):
                listener.enterArrayIndex(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArrayIndex"):
                listener.exitArrayIndex(self)

    def arrayIndex(self):

        localctx = JSONPathParser.ArrayIndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arrayIndex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(JSONPathParser.T__0)
            self.state = 151
            self.match(JSONPathParser.INT)
            self.state = 152
            self.match(JSONPathParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WildcardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return JSONPathParser.RULE_wildcard

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterWildcard"):
                listener.enterWildcard(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitWildcard"):
                listener.exitWildcard(self)

    def wildcard(self):

        localctx = JSONPathParser.WildcardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_wildcard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(JSONPathParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BracketWildcardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return JSONPathParser.RULE_bracketWildcard

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBracketWildcard"):
                listener.enterBracketWildcard(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBracketWildcard"):
                listener.exitBracketWildcard(self)

    def bracketWildcard(self):

        localctx = JSONPathParser.BracketWildcardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_bracketWildcard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(JSONPathParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
