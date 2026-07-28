import ply.lex as lex
import ply.yacc as yacc
import sys

# Lexer
tokens = ('NETWORKS_KEY', 'IDENTIFIER', 'COLON', 'NEWLINE', 'SPACE')

t_NETWORKS_KEY = r'^networks:'
t_COLON = r':'
t_SPACE = r'[ \t]+'

def t_IDENTIFIER(t):
    r'[a-zA-Z0-9_-]+'
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

# Parser (Simplificado para extraer indentaciones bajo networks)
def p_compose(p):
    '''compose : NETWORKS_KEY NEWLINE network_list'''
    print(f"Redes encontradas (Python/PLY): {p[3]}")

def p_network_list(p):
    '''network_list : SPACE IDENTIFIER COLON NEWLINE
                    | network_list SPACE IDENTIFIER COLON NEWLINE'''
    if len(p) == 5:
        p[0] = [p[2]]
    else:
        p[0] = p[1] + [p[3]]

def p_error(p):
    pass

parser = yacc.yacc()

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        data = f.read()
    # En un caso real, filtramos solo la sección networks para no confundir al parser
    start = data.find('networks:')
    if start != -1:
        parser.parse(data[start:])