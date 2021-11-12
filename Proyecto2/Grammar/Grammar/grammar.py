# IMPORTS
# Instructions
from Instruction.Statement import *
from Instruction.Print import *
from Instruction.Conditional.If import *
from Instruction.Functions.Function import *
from Instruction.Functions.Param import *
from Instruction.Loops.While import *
from Instruction.Loops.Break import *
from Instruction.Loops.Continue import *
from Instruction.Variables.Declaration import *
from Instruction.Structs.CreateStruct import *
from Instruction.Structs.DeclareStruct import *
from Instruction.Structs.AssignAccess import *
from Instruction.Structs.StructAttr import *

# Expressions
from Expressions.Arithmetic import *
from Expressions.Literal import *
from Expressions.Relational import *
from Expressions.Access import *
from Expressions.CallFunc import *
from Instruction.Functions.ReturnST import *
from Expressions.AccessStruct import *
from Expressions.Logical import *

# LEXICAL ANALYSIS
rw = {
    # GENERAL RW
    "END" : "END",
    "TRUE" : "TRUE",
    "FALSE" : "FALSE",

    # TYPES
    "INT64": "INT64",
    "STRING": "STRING",
    "BOOL": "BOOL",

    # FUNCTIONS SENTENCE
    "FUNCTION" : "FUNCTION",
    "RETURN" : "RETURN",

    # IFELSE SENTENCE
    "IF" : "IF",
    "ELSE" : "ELSE",
    "ELSEIF" : "ELSEIF",

    # WHILE SENTENCE
    "WHILE" : "WHILE",
    "CONTINUE" : "CONTINUE",
    "BREAK": "BREAK",

    # STRUCTS
    "STRUCT" : "STRUCT",

    # NATIVES
    "PRINTLN" : "PRINTLN",
    "PRINT" : "PRINT",
}

tokens = [
    "ID",

    # NATIVE VALUES
    "INTLITERAL",
    "FLOATLITERAL",
    "STRINGLITERAL",

    # SYMBOLS
    # GENERAL SYMBOLS
    "EQUALS",
    "POINT",
    "COLON",
    "SEMICOLON",
    "COMMA",
    "LEPAR",
    "RIPAR",

    # ARITHMETIC SYMBOLS
    "PLUS",
    "MINUS",
    "TIMES",
    "DIV",
    "POT",

    # LOGICAL SYMBOLS
    "AND",
    "OR",
    "NOT",

    # RELATIONAL SYMBOLS
    "GREATER",
    "LESS",
    "GREATEREQUAL",
    "LESSEQUAL",
    "EQUALSEQUALS",
    "DISTINT"
] + list(rw.values())

# TOKENS

# SYMBOLS
# GENERAL SYMBOLS
t_EQUALS                = r'='
t_POINT                 = r'\.'
t_COLON                 = r':'
t_SEMICOLON             = r';'
t_COMMA                 = r','
t_LEPAR                 = r'\('
t_RIPAR                 = r'\)'

# ARITHMETIC SYMBOLS
t_PLUS                  = r'\+'
t_MINUS                 = r'-'
t_TIMES                 = r'\*'
t_DIV                   = r'/'
t_POT                   = r'\^'

# LOGICAL SYMBOLS
t_AND                   = r'&&'
t_OR                    = r'\|\|'
t_NOT                   = r'!'

# RELATIONAL SYMBOLS
t_GREATER               = r'>'
t_LESS                  = r'<'
t_GREATEREQUAL          = r'>='
t_LESSEQUAL             = r'<='
t_EQUALSEQUALS          = r'=='
t_DISTINT               = r'!='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = rw.get(t.value.upper(), 'ID')
    return t

def t_FLOATLITERAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("ERROR IN PARSE TO FLOAT")
        t.value = 0
    return t

def t_INTLITERAL(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("ERROR IN PARSE TO INT")
        t.value = 0
    return t

def t_STRINGLITERAL(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

t_ignore = " \t"

def t_MLCOMMENT(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count("\n")

def t_OLCOMMENT(t):
    r'\#.*\n'
    t.lexer.lineno += 1

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQUALSEQUALS', 'DISTINT'),
    ('left', 'GREATEREQUAL', 'LESSEQUAL', 'GREATER', 'LESS'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
    ('right', 'NOT'),
    ('right', 'UMINUS'),
)

# SYNTACTIC ANALYSIS

def p_start(t):
    'start : instructions'
    t[0] = t[1]
    return t[0]

def p_instructions(t):
    '''instructions : instructions instruction
                    | instruction'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_instruction(t):
    '''instruction  : printST SEMICOLON
                    | ifST SEMICOLON
                    | declarationST SEMICOLON
                    | whileST SEMICOLON
                    | callFunc SEMICOLON
                    | declareFunc SEMICOLON
                    | returnST SEMICOLON
                    | breakST SEMICOLON
                    | continueST SEMICOLON
                    | createStruct SEMICOLON
                    | declareStructST SEMICOLON
                    | assignAccessST SEMICOLON'''
    t[0] = t[1]

# TYPES
def p_type(t):
    '''types : INT64
            |  STRING
            |  BOOL'''
    if t[1] == "Int64":
        t[0] = Type.INT
    elif t[1] == "String":
        t[0] = Type.STRING
    else:
        t[0] = Type.BOOLEAN

# STATEMENT
def p_statement(t):
    '''statement : instructions'''
    t[0] = Statement(t[1], t.lineno(1), t.lexpos(0))

# FUNCTION ST
def p_function(t):
    '''declareFunc :  FUNCTION ID LEPAR RIPAR COLON COLON types statement END
                    | FUNCTION ID LEPAR decParams RIPAR COLON COLON types statement END'''
    if len(t) == 7:
        t[0] = Function(t[2], [], t[7], t[8], t.lineno(1), t.lexpos(1))
    else:
        t[0] = Function(t[2], t[4], t[8], t[9], t.lineno(1), t.lexpos(1))

def p_decParams(t):
    '''decParams :    decParams COMMA ID COLON COLON types
                    | ID COLON COLON types'''
    if len(t) == 5:
        t[0] = [Param(t[1], t[4], t.lineno(1), t.lexpos(1))]
    else:
        t[1].append(Param(t[3], t[6], t.lineno(3), t.lexpos(3)))
        t[0] = t[1]

# RETURN ST
def p_return(t):
    '''returnST : RETURN
                | RETURN expression'''
    if len(t) == 2:
        t[0] = ReturnST(None, t.lineno(1), t.lexpos(1))
    else:
        t[0] = ReturnST(t[2], t.lineno(1), t.lexpos(1))

# DECLARATION ST
def p_declaration(t):
    '''declarationST : ID EQUALS expression'''
    t[0] = Declaration(t[1], t[3], t.lineno(2), t.lexpos(2))

# PRINT ST
def p_printlnST(t):
    'printST  : PRINTLN LEPAR expression RIPAR'
    t[0] = Print(t[3], t.lineno(1), t.lexpos(0), True)

def p_printST(t):
    'printST  : PRINT LEPAR expression RIPAR'
    t[0] = Print(t[3], t.lineno(1), t.lexpos(0))

# IF ST
def p_ifST(t):
    '''ifST : IF expression statement END
            | IF expression statement ELSE statement END
            | IF expression statement elseIfList END'''
    if len(t) == 5:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0))
    elif len(t) == 7:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[5])
    elif len(t) == 6:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[4])

def p_elseIfList(t):
    '''elseIfList   : ELSEIF expression statement
                    | ELSEIF expression statement ELSE statement
                    | ELSEIF expression statement elseIfList'''
    if len(t) == 4:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0))
    elif len(t) == 6:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[5])
    elif len(t) == 5:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[4])

# STRUCTS
# CREATE STRUCT
def p_createStruct(t):
    'createStruct : STRUCT ID attList END'
    t[0] = CreateStruct(t[2], t[3], t.lineno(1), t.lexpos(1))

def p_attList(t):
    '''attList :  attList SEMICOLON ID COLON COLON types SEMICOLON
                | ID COLON COLON types'''
    if len(t) == 5:
        prueba = t[4]
        t[0] = [StructAttr(t[1], t[4], t.lineno(1), t.lexpos(1))]
    else:
        prueba = t[6]
        t[1].append(StructAttr(t[3], t[6], t.lineno(2), t.lexpos(2)))
        t[0] = t[1]

# DECLARE STRUCT
def p_declareStruct(t):
    'declareStructST : ID COLON COLON ID'
    t[0] = DeclareStruct(t[1], t[4], t.lineno(1), t.lexpos(1))

# ASSIGN ACCESS
def p_assignAccess(t):
    'assignAccessST : ID POINT ID EQUALS expression'
    t[0] = AssignAccess(t[1], t[3], t[5], t.lineno(1), t.lexpos(1))

# WHILE ST
def p_while(t):
    'whileST : WHILE expression statement END'
    t[0] = While(t[2], t[3], t.lineno(1), t.lexpos(1))

# BREAK ST
def p_break(t):
    'breakST : BREAK'
    t[0] = Break(t.lineno(1), t.lexpos(1))

# CONTINUE ST
def p_continue(t):
    'continueST : CONTINUE'
    t[0] = Continue(t.lineno(1), t.lexpos(1))

# CALL FUNCTION ST
def p_callfunc(t):
    '''callFunc : ID LEPAR RIPAR
                | ID LEPAR expList RIPAR'''
    if len(t) == 4:
        t[0] = CallFunc(t[1], [], t.lineno(1), t.lexpos(1))
    else:
        t[0] = CallFunc(t[1], t[3], t.lineno(1), t.lexpos(1))

# CALL PARAMS
def p_callparams(t):
    '''expList :  expList COMMA expression
                | expression'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]

# EXPRESSIONS
def p_expression(t):
    '''expression   : MINUS expression %prec UMINUS
                    | NOT expression %prec UMINUS
                    
                    | expression PLUS expression
                    | expression MINUS expression
                    | expression TIMES expression
                    | expression DIV expression
                    | expression POT expression

                    | expression GREATER expression
                    | expression LESS expression
                    | expression GREATEREQUAL expression
                    | expression LESSEQUAL expression
                    | expression EQUALSEQUALS expression
                    | expression DISTINT expression
                    
                    | expression OR expression
                    | expression AND expression
                    | finalExp'''
    if len(t) == 2: t[0] = t[1]
    elif len(t) == 3:
        # UMINUS
        t[0] = Arithmetic(Literal(0, Type.INT, t.lineno(1), t.lexpos(0)), t[2], ArithmeticOption.MINUS, t.lineno(1), t.lexpos(0))
    else:
        if t[2] == "+":
            t[0] = Arithmetic(t[1], t[3], ArithmeticOption.PLUS, t.lineno(2), t.lexpos(0))
        elif t[2] == "-":
            t[0] = Arithmetic(t[1], t[3], ArithmeticOption.MINUS, t.lineno(2), t.lexpos(0))
        elif t[2] == "*":
            t[0] = Arithmetic(t[1], t[3], ArithmeticOption.TIMES, t.lineno(2), t.lexpos(0))
        elif t[2] == "/":
            t[0] = Arithmetic(t[1], t[3], ArithmeticOption.DIV, t.lineno(2), t.lexpos(0))
        elif t[2] == "^":
            t[0] = Arithmetic(t[1], t[3], ArithmeticOption.POT, t.lineno(2), t.lexpos(0))
        elif t[2] == ">":
            t[0] = Relational(t[1], t[3], RelationalOption.GREATER, t.lineno(2), t.lexpos(2))
        elif t[2] == "<":
            t[0] = Relational(t[1], t[3], RelationalOption.LESS, t.lineno(2), t.lexpos(2))
        elif t[2] == ">=":
            t[0] = Relational(t[1], t[3], RelationalOption.GREATEREQUAL, t.lineno(2), t.lexpos(2))
        elif t[2] == "<=":
            t[0] = Relational(t[1], t[3], RelationalOption.LESSEQUAL, t.lineno(2), t.lexpos(2))
        elif t[2] == "==":
            t[0] = Relational(t[1], t[3], RelationalOption.EQUALSEQUALS, t.lineno(2), t.lexpos(2))
        elif t[2] == "!=":
            t[0] = Relational(t[1], t[3], RelationalOption.DISTINT, t.lineno(2), t.lexpos(2))
        elif t[2] == "||":
            t[0] = Logical(t[1], t[3], LogicalOption.OR, t.lineno(2), t.lexpos(2))
        elif t[2] == "&&":
            # AND
            t[0] = Logical(t[1], t[3], LogicalOption.AND, t.lineno(2), t.lexpos(2))

def p_finalExp(t):
    '''finalExp : LEPAR expression RIPAR
                | INTLITERAL
                | FLOATLITERAL
                | STRINGLITERAL
                | TRUE
                | FALSE
                | ID
                | callFunc
                | accessST'''
    if len(t) == 2:
        if t.slice[1].type == "INTLITERAL":
            t[0] = Literal(int(t[1]), Type.INT, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == "FLOATLITERAL":
            t[0] = Literal(float(t[1]), Type.FLOAT, t.lineno(1), t.lexpos(0))
        elif t.slice[1].type == "ID":
            t[0] = Access(t[1], t.lineno(1), t.lexpos(1))
        elif t.slice[1].type == "callFunc" or t.slice[1].type == "accessST":
            t[0] = t[1]
        elif isinstance(t[1], str):
            value = str(t[1])
            if "true" in value:
                t[0] = Literal(True, Type.BOOLEAN, t.lineno(1), t.lexpos(0))
            elif "false" in value:
                t[0] = Literal(False, Type.BOOLEAN, t.lineno(1), t.lexpos(0))
            else:
                t[0] = Literal(str(t[1]), Type.STRING, t.lineno(1), t.lexpos(0))
    else:
        t[0] = t[2]

def p_accessST(t):
    '''accessST : ID POINT ID'''
    t[0] = AccessStruct(t[1], t[3], t.lineno(1), t.lexpos(1))

def p_error(t):
    print(t)
    print("Syntactic error in '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    return parser.parse(input, lexer=lexer)