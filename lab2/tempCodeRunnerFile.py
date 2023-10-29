
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





def p_expression_exp(p):
    '''expression : line SEMICOLON
                  | expression expression
                  | LCURLY expression RCURLY
                  | ifelse
                  | while '''


def p_expression_pexp(p):
    '''pexpression : LCURLY pexpression RCURLY
                  | LCURLY expression RCURLY
                  | line SEMICOLON
                  | for '''

def p_expression_obj(p):
    ''' object : ID vector
                | ID'''

def p_expression_line(p):
    ''' line : assign
                | PRINT printable
                | BREAK
                | CONTINUE
                | RETURN'''


def p_expression_for(p):
    ''' for : FOR ID EQUALS forable COLON pexpression '''


def p_expression_printable(p):
    ''' printable : printable COMMA printable
                    | operation
                    | STRING '''


def p_expression_forable(p):
    ''' forable : object 
                | INT '''


def p_expression_bool(p):
    ''' bool : LPAREN bool RPAREN 
            | operation MORE operation 
            | operation LESS operation 
            | operation MOREOREQ operation 
            | operation LESSOREQ operation 
            | operation EQUALS operation '''


def p_expression_assign(p):
    ''' assign : object ASSIGN operation 
            | object ADDASSIGN operation 
            | object SUBASSIGN operation 
            | object MULASSIGN operation 
            | object DIVASSIGN operation '''


def p_expression_operation(p):
    ''' operation : operation PLUS operation
                | operation MINUS operation 
                | operation TIMES operation 
                | operation DIVIDE operation 
                | operation DOTADD operation 
                | operation DOTSUB operation 
                | operation DOTMUL operation 
                | operation DOTDIV operation
                | MINUS operation 
                | operation TRANSPOSE
                | EYE LPAREN operation RPAREN
                | ZEROS LPAREN operation RPAREN
                | ONES LPAREN operation RPAREN
                | object
                | FLOAT
                | INT 
                | matrix '''


def p_expression_ifelse(p):
    ''' ifelse : IF LPAREN bool RPAREN pexpression
                | IF LPAREN bool RPAREN pexpression ELSE pexpression'''


def p_expression_while(p):
    ''' while : WHILE LPAREN bool RPAREN pexpression'''


def p_expression_matrix(p):
    ''' matrix : LSQUAR row RSQUAR'''


def p_expression_row(p):
    ''' row : row COMMA vector 
                | vector '''


def p_expression_vector(p):
    ''' vector : LSQUAR elem RSQUAR '''


def p_expression_elem(p):
    ''' elem : elem COMMA num 
                | num'''


def p_expression_num(p):
    ''' num : INT 
            | FLOAT'''


parser = yacc.yacc()
