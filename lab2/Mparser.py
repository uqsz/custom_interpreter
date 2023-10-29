
import scanner as scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
    ("left", 'ASSIGN', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ("left", 'MORE', 'LESS', 'MOREOREQ', 'LESSOREQ', 'EQUALS'),
    ("left", 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
     'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV'),
    ("left", 'TRANSPOSE')


    # to fill ...
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(
            p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_expression(p):
    '''expression : LPAREN expression RPAREN
                  | LCURLY expression RCURLY
                  | ID
                  | INT 
                  | FLOAT
                  | STRING 
                  | BREAK
                  | CONTINUE
                  | RETURN
                  | expression SEMICOLON expression SEMICOLON
                  | expression SEMICOLON'''


def p_expression_binop(p):
    '''expression  : expression PLUS expression 
                    | expression MINUS expression
                    | expression TIMES expression
                    | expression DIVIDE expression'''


def p_expression_binop_dot(p):
    '''expression  : expression DOTADD expression 
                    | expression DOTSUB expression
                    | expression DOTMUL expression
                    | expression DOTDIV expression'''


def p_expression_assign(p):
    '''expression  : expression ASSIGN expression 
                    | expression ADDASSIGN expression
                    | expression SUBASSIGN expression
                    | expression MULASSIGN expression
                    | expression DIVASSIGN expression'''


def p_expression_relative(p):
    '''expression  : expression MORE expression 
                    | expression LESS expression
                    | expression MOREOREQ expression
                    | expression LESSOREQ expression
                    | expression EQUALS expression'''


def p_expression_neg(p):
    'expression  : MINUS expression'


def p_expression_trans(p):
    'expression  : expression TRANSPOSE'


def p_expression_specials(p):
    '''expression  : ZEROS LPAREN expression RPAREN SEMICOLON
                    | EYE LPAREN expression RPAREN SEMICOLON
                    | ONES LPAREN expression RPAREN SEMICOLON'''


def p_expression_if(p):
    '''expression : IF LPAREN expression RPAREN expression
                    | IF LPAREN expression RPAREN expression ELSE expression
    '''


def p_expression_while(p):
    '''expression : WHILE LPAREN expression RPAREN expression
    '''


def p_expression_for(p):
    '''expression : FOR ID EQUALS expression COLON expression LCURLY expression expression
    '''


def p_expression_read(p):
    '''expression : LSQUAR expression RSQUAR
                    | LSQUAR expression COMMA expression RSQUAR
    '''


def p_expression_print(p):
    """expression : PRINT expression"""


parser = yacc.yacc()
