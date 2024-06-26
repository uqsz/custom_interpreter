import Scanner
import ply.yacc
import AbstractSyntaxTree

tokens = Scanner.tokens

precedence = (
    ("left", 'ASSIGN', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ("left", 'MORE', 'LESS', 'MOREOREQ', 'LESSOREQ', 'EQUALS', 'NOTEQUALS'),
    ("left", 'PLUS', 'MINUS', 'DOTADD', 'DOTSUB'),
    ("left", 'TIMES', 'DIVIDE', 'DOTMUL', 'DOTDIV'),
    ("left", 'TRANSPOSE'),
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
        p[0] = AbstractSyntaxTree.Recursion(p[1], p[2], p.lexer.lineno)


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
            | CONTINUE '''
    if p.slice[1].type == "assign":
        p[0] = p[1]
    elif p.slice[1].type == "PRINT":
        p[0] = AbstractSyntaxTree.PrintExpr(p[2], p.lexer.lineno)
    else:
        p[0] = AbstractSyntaxTree.EndExpr(p.slice[1].type, p.lexer.lineno)


def p_assign(p):  # 4
    ''' assign : object ASSIGN operation 
            | object ADDASSIGN operation 
            | object SUBASSIGN operation 
            | object MULASSIGN operation 
            | object DIVASSIGN operation '''

    p[0] = AbstractSyntaxTree.BinExpr(p[2], p[1], p[3], p.lexer.lineno)


def p_operation(p):  # 5
    ''' operation : LPAREN operation RPAREN
                | operation PLUS operation
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
                | matrix'''

    if len(p) == 5:
        p[0] = AbstractSyntaxTree.UnaryExpr(p[1], p[3], p.lexer.lineno)

    elif len(p) == 4:
        if p.slice[1].type == "LPAREN":
            p[0] = p[2]
        else:
            p[0] = AbstractSyntaxTree.BinExpr(p[2], p[1], p[3], p.lexer.lineno)

    elif len(p) == 3:
        if p[1] == '-':
            p[0] = AbstractSyntaxTree.UnaryExpr("MINUS", p[2], p.lexer.lineno)

        elif p[2] == '\'':
            p[0] = AbstractSyntaxTree.UnaryExpr("TRANSPOSE", p[1], p.lexer.lineno)

    elif len(p) == 2:
        p[0] = p[1]


def p_bool(p):  # 6
    ''' bool : LPAREN bool RPAREN 
            | operation MORE operation 
            | operation LESS operation 
            | operation MOREOREQ operation 
            | operation LESSOREQ operation 
            | operation EQUALS operation
            | operation NOTEQUALS operation '''

    if p[2] in ['>', '<', '>=', '<=', '==', '!=']:
        p[0] = AbstractSyntaxTree.BinExpr(p[2], p[1], p[3], p.lexer.lineno)
    else:
        p[0] = p[2]


def p_print_state(p):  # 7
    ''' print_state : operation COMMA print_state 
                    | operation '''
    if len(p) == 2:
        p[0] = AbstractSyntaxTree.Recursion(p[1], None, p.lexer.lineno)
    else:
        p[0] = AbstractSyntaxTree.Recursion(p[1], p[3], p.lexer.lineno)


def p_object(p):  # 8
    ''' object : ID vector
            | ID '''

    if len(p) == 2:
        p[0] = AbstractSyntaxTree.Variable(p[1], p.lexer.lineno)
    else:
        p[0] = AbstractSyntaxTree.Reference(p[1], p[2], p.lexer.lineno)


def p_ifelse_state(p):  # 9
    ''' ifelse_state : IF LPAREN bool RPAREN instruction
                    | IF LPAREN bool RPAREN instruction ELSE instruction'''
    if len(p) == 6:
        p[0] = AbstractSyntaxTree.IfInstruction(p[3], p[5], p.lexer.lineno)
    else:
        p[0] = AbstractSyntaxTree.IfElseInstruction(p[3], p[5], p[7], p.lexer.lineno)


def p_while_state(p):  # 10
    ''' while_state : WHILE LPAREN bool RPAREN instruction'''
    p[0] = AbstractSyntaxTree.WhileInstruction(p[3], p[5], p.lexer.lineno)


def p_for_state(p):  # 11
    ''' for_state : FOR ID ASSIGN operation COLON operation instruction '''
    p[0] = AbstractSyntaxTree.ForInstruction(p[2], p[4], p[6], p[7], p.lexer.lineno)


def p_matrix(p):  # 12
    ''' matrix : LSQUAR row RSQUAR'''
    p[0] = AbstractSyntaxTree.Matrix(p[2], None, p.lexer.lineno)


def p_row(p):  # 13
    ''' row : row COMMA vector 
                | vector '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = AbstractSyntaxTree.Recursion(p[1], p[3], p.lexer.lineno)


def p_vector(p):  # 14
    ''' vector : LSQUAR elem RSQUAR '''
    p[0] = AbstractSyntaxTree.Vector(p[2], p.lexer.lineno)


def p_elem(p):  # 15
    ''' elem : number COMMA elem 
                | number'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = AbstractSyntaxTree.Recursion(p[1], p[3], p.lexer.lineno)


def p_number(p):  # 16
    ''' number : INT 
            | FLOAT
            | STRING'''
    if p.slice[1].type == "INT":
        p[0] = AbstractSyntaxTree.IntNum(p[1], p.lexer.lineno)
    elif p.slice[1].type == "FLOAT":
        p[0] = AbstractSyntaxTree.FloatNum(p[1], p.lexer.lineno)
    else:
        p[0] = AbstractSyntaxTree.String(p[1], p.lexer.lineno)


parser = ply.yacc.yacc(debug=False, write_tables=False)
