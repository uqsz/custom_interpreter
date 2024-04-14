import ply.lex

tokens = [
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',

    'TRANSPOSE',
    'SEMICOLON',
    'COLON',
    'COMMA',

    'DOTADD',
    'DOTSUB',
    'DOTMUL',
    'DOTDIV',

    'ASSIGN',
    'ADDASSIGN',
    'SUBASSIGN',
    'MULASSIGN',
    'DIVASSIGN',

    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'LSQUAR',
    'RSQUAR',

    'MORE',
    'LESS',
    'MOREOREQ',
    'LESSOREQ',
    'EQUALS',
    'NOTEQUALS',

    'INT',
    'FLOAT',
    'ID',
    'STRING'
]

reserved = {
    'if': 'IF',
    'for': 'FOR',
    'else': 'ELSE',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'print': 'PRINT',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES'
}

tokens = tokens + list(reserved.values())


t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_TRANSPOSE = r'\''
t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_COMMA = r'\,'

t_DOTADD = r'.\+'
t_DOTSUB = r'.-'
t_DOTMUL = r'.\*'
t_DOTDIV = r'./'

t_ASSIGN = r'='
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_LSQUAR = r'\['
t_RSQUAR = r'\]'

t_MORE = r'>'
t_LESS = r'<'
t_MOREOREQ = r'>='
t_LESSOREQ = r'<='
t_EQUALS = r'=='
t_NOTEQUALS = r'!='

t_ignore = ' \t'


def t_FLOAT(t):
    r'(\d+\.\d*(E[-+]?\d+)?\d*)|(\d*\.\d*(E[-+]?\d+)?\d+)'
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_STRING(t):
    r'"([^"]*)"'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_comment(t):
    r'\#.*'
    pass


def t_error(t):
    print("line %d: illegal character '%s'" % (t.lineno, t.value[0]))
    t.lexer.skip(1)


lexer = ply.lex.lex()
