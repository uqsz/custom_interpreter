
import scanner as scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
    ("left", 'ASSIGN', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ("left", 'MORE', 'LESS', 'MOREOREQ', 'LESSOREQ', 'EQUALS', 'NOTEQUALS'),
    ("left", 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
     'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV'),
    ("left", 'TRANSPOSE')
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(
            p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_expression(p):  # 1
    '''expression : expression instruction
                  | instruction'''


def p_instruction(p):  # 2
    '''instruction : LCURLY expression RCURLY
                  | line SEMICOLON
                  | for_state 
                  | ifelse_state 
                  | while_state '''


def p_line(p):  # 3
    ''' line : assign
            | PRINT print_state
            | BREAK
            | CONTINUE
            | RETURN print_state
            | RETURN '''


def p_print_state(p):  # 4
    ''' print_state : printable COMMA print_state 
                    | printable '''


def p_printable(p):  # 5
    ''' printable : operation
                | STRING '''


def p_assign(p):  # 6
    ''' assign : object ASSIGN operation 
            | object ADDASSIGN operation 
            | object SUBASSIGN operation 
            | object MULASSIGN operation 
            | object DIVASSIGN operation '''


def p_operation(p):  # 7
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
                | number
                | matrix '''


def p_bool(p):  # 8
    ''' bool : LPAREN bool RPAREN 
            | operation MORE operation 
            | operation LESS operation 
            | operation MOREOREQ operation 
            | operation LESSOREQ operation 
            | operation EQUALS operation
            | operation NOTEQUALS operation '''


def p_object(p):  # 9
    ''' object : ID vector
            | ID '''


def p_ifelse_state(p):  # 10
    ''' ifelse_state : IF LPAREN bool RPAREN instruction
                    | IF LPAREN bool RPAREN instruction ELSE instruction'''


def p_while_state(p):  # 11
    ''' while_state : WHILE LPAREN bool RPAREN instruction'''


def p_for_state(p):  # 12
    ''' for_state : FOR ID ASSIGN forable COLON forable instruction '''


def p_forable(p):  # 13
    ''' forable : object 
                | INT '''


def p_matrix(p):  # 14
    ''' matrix : LSQUAR row RSQUAR'''


def p_row(p):  # 15
    ''' row : row COMMA vector 
                | vector '''


def p_vector(p):  # 16
    ''' vector : LSQUAR elem RSQUAR '''


def p_elem(p):  # 17
    ''' elem : elem COMMA number 
                | number'''


def p_number(p):  # 18
    ''' number : INT 
            | FLOAT'''


parser = yacc.yacc()
