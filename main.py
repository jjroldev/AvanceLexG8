import ply.yacc as yacc
import ply.lex as lex
from datetime import datetime
import os

# Palabras reservadas de Golang
reserved = {
    'break': 'BREAK',
    'default': 'DEFAULT',
    'func': 'FUNC',
    'interface': 'INTERFACE',
    'select': 'SELECT', 
    'case': 'CASE',
    'defer': 'DEFER',
    'go': 'GO',
    'else': 'ELSE',
    'goto': 'GOTO',
    'package': 'PACKAGE',
    'switch': 'SWITCH',
    'const': 'CONST',
    'fallthrough': 'FALLTHROUGH',
    'if': 'IF',
    'range': 'RANGE',
    'type': 'TYPE',
    'continue': 'CONTINUE',
    'for': 'FOR',
    'import': 'IMPORT', 
    'return': 'RETURN',
    'var': 'VAR',
    'float64':'FLOAT64',
    'float32':'FLOAT32',
    'Println':'PRINTLN',
    'Print':'PRINT',
    'Printf':'PRINTF',
    'Sprint':'SPRINT',
    'Sprintf':'SPRINTF',
    'Sprintln':'SPRINTLN',
    'main':'MAIN'
}


# Lista de nombres de tokens
tokens = (
    'VARIABLE',
    'BOOL',
    'STRING',
    'INT',
    'FLOAT',
    'PLUS', 'MINUS', 'TIMES', 'DIV', 'MOD',
    'EQ', 'NEQ', 'LT', 'GT', 'LTOEQ', 'GTOEQ',
    'AND', 'OR', 'NOT', 'ASSIGN', 'PLUSA',
    'MINUSA', 'TIMESA', 'DIVA', 'MODA',
    'RCORCHETE',
    'LCORCHETE',
    'RLLAVE',
    'LLLAVE',
    'RPARENTESIS',
    'LPARENTESIS',
    'COLON',
    'DOT',
    'SEMICOLON',
    'DECLARE_ASSIGN',
) + tuple(reserved.values())

# Expresiones regulares para operadores
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_GT = r'>'
t_LTOEQ = r'<='
t_GTOEQ = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_ASSIGN = r'='
t_PLUSA = r'\+='
t_MINUSA = r'-='
t_TIMESA = r'\*='
t_DIVA = r'/='
t_MODA = r'%='
t_RCORCHETE = r'\]'
t_LCORCHETE= r'\['
t_RLLAVE=r'}'
t_LLLAVE = r'{'
t_RPARENTESIS=r'\)'
t_LPARENTESIS = r'\('
t_COLON = r':'
t_DOT = r'\.'
t_SEMICOLON = r';'
t_DECLARE_ASSIGN = r':='

# Definición de tokens para tipos básicos
def t_BOOL(t):
    r'true|false'
    t.value = t.value == 'true'
    return t

def t_FLOAT(t):
    r'-?\d+\.\d+'
    t.value=float(t.value)
    return t

def t_INT(t):
    r'-?[0-9]+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^"\\]|\\["nt\\])*"'
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_]\w*'
    t.type=reserved.get(t.value,'VARIABLE')
    return t

# Salto de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres ignorados (espacios y tabulaciones)
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado.")
        return ""

def generar_log(tokens, usuario_git):
    fecha_hora = datetime.now().strftime("%d-%m-%Y-%Hh%M")
    if not os.path.exists("Logs"):
        os.makedirs("Logs")
    nombre_log = f"Logs/lexico-{usuario_git}-{fecha_hora}.txt"
    with open(nombre_log, 'w') as log:
        for token in tokens:
            log.write(f"{token}\n")
    print(f"Log generado: {nombre_log}")

def procesar_archivo(nombre_archivo, usuario_git):
    data = leer_archivo(nombre_archivo)
    if not data:
        return
    lexer.input(data)
    tokens = []
    #TOKENIZAR
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    generar_log(tokens, usuario_git)

procesar_archivo("algoritmo1.go", "jjroldev")