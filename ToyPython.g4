grammar ToyPython;

@lexer::members {
    from collections import deque

    def __init__(self, input=None):
        super().__init__(input)
        self.indents = deque()
        self.last_indent = 0
        self.pending_dedents = 0
        self.dedent_tokens = []

    def emit(self):
        if self.dedent_tokens:
            return self.dedent_tokens.pop(0)
        return super().emit()

    def handle_indentation(self):
        current_indent = len(self.text.replace('\r', '').replace('\n', ''))

        if current_indent > self.last_indent:
            self.indents.append(self.last_indent)
            self.last_indent = current_indent
            self.type = self.INDENT
        elif current_indent < self.last_indent:
            while self.indents and self.indents[-1] > current_indent:
                self.indents.pop()
                dedent = self._factory.create(
                    self._tokenFactorySourcePair,
                    self.DEDENT,
                    "<DEDENT>",
                    self.DEFAULT_TOKEN_CHANNEL,
                    self.tokenStartCharIndex,
                    self.tokenStartCharIndex - 1,
                    self.tokenStartLine,
                    self.tokenStartColumn
                )
                self.dedent_tokens.append(dedent)
            self.last_indent = current_indent

    def nextToken(self):
        token = super().nextToken()

        if token.type == self.NEWLINE:
            self.handle_indentation()

        if self.dedent_tokens:
            return self.emit()

        return token
}

// Parser Rules

program
    : (statement | emptyStatement)+ EOF
    ;

statement
    : simpleStatement
    | compoundStatement
    ;

emptyStatement
    : NEWLINE
    ;

simpleStatement
    : 'print' '(' expression ')' NEWLINE
    | IDENTIFIER '=' expression NEWLINE
    ;

compoundStatement
    : 'if' comparison ':' NEWLINE INDENT (statement | emptyStatement)+ DEDENT
    ;

comparison
    : expression (('<' | '>' | '==' | '!=' | '<=' | '>=') expression)?
    ;

expression
    : term (('+' | '-') term)*
    ;

term
    : factor (('*' | '/') factor)*
    ;

factor
    : NUMBER
    | STRING
    | IDENTIFIER
    | '(' expression ')'
    ;

// Lexer Rules

NEWLINE: '\r'? '\n';
INDENT: '<INDENT>';
DEDENT: '<DEDENT>';
NUMBER: [0-9]+;
STRING: '"' (~["\\] | '\\' .)* '"';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;

WS: [ \t]+ -> skip;
COMMENT: '#' ~[\r\n]* -> channel(HIDDEN);