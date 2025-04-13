import ply.lex as lex

# Define all possible token types
tokens = (
    'ACTOR', 'ACTOR_LIST', 'USECASE', 'USECASE_LIST', 'INHERITS', 'SYSTEM',
    'BY', 'PACKAGE', 'RELATIONSHIPS', 'EXT', 'INC', 'INH', 'AS', 'OF', 
    'IN', 'FROM', 'IDENTIFIER', 'LBRACE', 'RBRACE', 'COMMA', 'COLON'
)

# Ignore whitespace and tabs
t_ignore = " \t"

# Define simple tokens with exact patterns
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_COLON = r':'

# Reserved keywords map to token types
reserved = {
    'actor': 'ACTOR',
    'actor_list': 'ACTOR_LIST',
    'usecase': 'USECASE',
    'usecase_list': 'USECASE_LIST',
    'inherits': 'INHERITS',
    'system': 'SYSTEM',
    'by': 'BY',
    'package': 'PACKAGE',
    'relationships': 'RELATIONSHIPS',
    'ext': 'EXT',
    'inc': 'INC',
    'inh': 'INH',
    'as': 'AS',
    'of': 'OF',
    'in': 'IN',
    'from': 'FROM'
}

# Token rules for identifiers and keywords
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'IDENTIFIER')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comment(t):
    r'\#.*'
    pass

def t_error(t):
    print(f"Illegal character {t.value[0]} at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()