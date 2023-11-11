
import scanner as scanner
import ply.yacc as yacc
import AST

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
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = AST.Recursion(p[1], p[2])


def p_instruction(p):  # 2
    '''instruction : LCURLY expression RCURLY
                  | line SEMICOLON
                  | for_state 
                  | ifelse_state 
                  | while_state '''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_line(p):  # 3
    ''' line : assign
            | PRINT print_state
            | BREAK
            | CONTINUE
            | RETURN print_state
            | RETURN '''
    
    if p[1] == "assign":
        p[0] = p[1]
    elif p[1] == "print":
        p[0] = AST.PrintExpr(p[2])
    elif p[1] == "return" and len(p) == 3:
        p[0] = AST.ReturnExpr(p[2])
    else:
        p[0] = p[1]


def p_print_state(p):  # 4
    ''' print_state : printable COMMA print_state 
                    | printable '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = AST.Recursion(p[1], p[3])


def p_printable(p):  # 5
    ''' printable : operation
                | STRING '''
    
    if isinstance(p[1], str):
        p[0] = AST.String(p[1])        
    else:
        p[0] = p[1]


def p_assign(p):  # 6
    ''' assign : object ASSIGN operation 
            | object ADDASSIGN operation 
            | object SUBASSIGN operation 
            | object MULASSIGN operation 
            | object DIVASSIGN operation '''

    p[0] = AST.BinExpr(p[2], p[1], p[3])


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

    if len(p) == 5:
        p[0] = AST.UnaryExpr(p[1], p[3])

    elif len(p) == 4:
        p[0] = AST.BinExpr(p[2], p[1], p[3])

    elif len(p) == 3:
        if p[1] == '-':
            p[0] = AST.UnaryExpr("MINUS", p[2])

        elif p[2] == '\'':
            p[0] = AST.UnaryExpr("TRANSPOSE", p[1])

    elif len(p) == 2:
        p[0] = p[1]


def p_bool(p):  # 8
    ''' bool : LPAREN bool RPAREN 
            | operation MORE operation 
            | operation LESS operation 
            | operation MOREOREQ operation 
            | operation LESSOREQ operation 
            | operation EQUALS operation
            | operation NOTEQUALS operation '''

    if p[2] in ['>', '<', '>=', '<=', '==', '!=']:
        p[0] = AST.BinExpr(p[2], p[1], p[3])
    else:
        p[0] = p[2]


def p_object(p):  # 9
    ''' object : ID vector
            | ID '''

    if len(p) == 2:
        p[0] = AST.Variable(p[1])
    else:
        p[0] = AST.Reference(p[1], p[2])


def p_ifelse_state(p):  # 10
    ''' ifelse_state : IF LPAREN bool RPAREN instruction
                    | IF LPAREN bool RPAREN instruction ELSE instruction'''
    if len(p) == 6:
        p[0] = AST.IfInstruction(p[3], p[5])
    else:
        p[0] = AST.IfElseInstruction(p[3], p[5], p[7])


def p_while_state(p):  # 11
    ''' while_state : WHILE LPAREN bool RPAREN instruction'''
    p[0] = AST.WhileInstruction(p[3], p[5])


def p_for_state(p):  # 12
    ''' for_state : FOR ID ASSIGN forable COLON forable instruction '''
    p[0] = AST.ForInstruction(p[2], p[4], p[6], p[7])


def p_forable(p):  # 13
    ''' forable : object 
                | INT '''
    if isinstance(p[1], int):
        p[0] = AST.IntNum(p[1])
    else:
        p[0] = p[1]


def p_matrix(p):  # 14
    ''' matrix : LSQUAR row RSQUAR'''
    p[0] = p[2]


def p_row(p):  # 15
    ''' row : row COMMA vector 
                | vector '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = AST.Recursion(p[1], p[3])


def p_vector(p):  # 16
    ''' vector : LSQUAR elem RSQUAR '''
    p[0] = AST.Vector(p[2])


def p_elem(p):  # 17
    ''' elem : elem COMMA number 
                | number'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = AST.Recursion(p[1], p[3])


def p_number(p):  # 18
    ''' number : INT 
            | FLOAT'''
    if p[0] == "INT":
        p[0] = AST.IntNum(p[1])
    else:
        p[0] = AST.FloatNum(p[1])


parser = yacc.yacc()
