from TS.Excepcion import Excepcion
import re
import os
from abstract.NodoAST import NodoAST
import tkinter as tk




errores = []
reservadas = {
    'int'   : 'RINT',
    'double' : 'RDOUBLE',
    'string': 'RSTRING',
    'char'  : 'RCHAR',
    'boolean' : 'RBOOL',
    'print' : 'RPRINT',
    'var'   : 'RVAR',
    'null'  : 'RNULL',
    'if'    : 'RIF',
    'else'  : 'RELSE',
    'true'  : 'RTRUE',
    'false' : 'RFALSE',
    'switch': 'RSWITCH',
    'case'  : 'RCASE',
    'break' : 'RBREAK',
    'default' : 'RDEFAULT',
    'while' : 'RWHILE',
    'for'   : 'RFOR',
    'main'  : 'RMAIN',
    'func'  : 'RFUNC',
    'return': 'RRETURN',
    'continue' : 'RCONTINUE',
    'read'  : 'RREAD',
    'new'   : 'RNEW',
}

tokens  = [
    'PUNTOCOMA',
    'PARA',
    'PARC',
    'LLAVEA',
    'LLAVEC',
    'COMA',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'POT',
    'MOD',
    'MENORQUE',
    'MAYORQUE',
    'IGUALIGUAL',
    'DIFERENTE',
    'MENORIGUAL',
    'MAYORIGUAL',
    'IGUAL',
    'AND',
    'OR',
    'NOT',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'CARACTER',
    'ID',
    'INC',
    'DEC',
    'DOSPUNTOS',
    'CORA',
    'CORC',
] + list(reservadas.values())

# Tokens
t_PUNTOCOMA     = r';'
t_PARA          = r'\('
t_PARC          = r'\)'
t_LLAVEA        = r'{'
t_LLAVEC        = r'}'
t_COMA          = r','
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_DIV           = r'/'
t_POT           = r'\*\*'
t_MOD           = r'%'
t_MENORQUE      = r'<'
t_MAYORQUE      = r'>'
t_DIFERENTE     = r'=!'
t_IGUALIGUAL    = r'=='
t_MENORIGUAL    = r'<='
t_MAYORIGUAL    = r'>='
t_IGUAL         = r'='
t_AND           = r'&&'
t_OR            = r'\|\|'
t_NOT           = r'!'
t_INC           = r'\+\+'
t_DEC           = r'--'
t_DOSPUNTOS     = r':'
t_CORA          = r'\['
t_CORC          = r'\]'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')
     return t

def t_CADENA(t):
    r'\"(\\[nN]|\\\\|\\\*|\\[tT]|\\\'|\\\"|[^\\\"\'])*?\"'
    t.value = t.value[1:-1]   # remuevo las comillas
    t.value = t.value.replace('\\t', "\t")
    t.value = t.value.replace('\\n', "\n")
    t.value = t.value.replace('\\"', "\"")
    t.value = t.value.replace("\\'","\'")
    t.value = t.value.replace('\\\\', "\\")
    return t

def t_CARACTER(t):
    r"\'(\\[nN]|\\\\|\\\*|\\[tT]|\\\'|\\\"|[^\\\"\'])?\'"
    t.value = t.value[1:-1] # remuevo las comillas simples
    t.value = t.value.replace('\\t', "\t")
    t.value = t.value.replace('\\n', "\n")
    t.value = t.value.replace('\\"', '"')
    t.value = t.value.replace('\\\\', "\\")
    t.value = t.value.replace("\\'", "\'")

    return t

def t_COMENTARIO_MULTILINEA(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1



# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    errores.append(Excepcion("Lexico","Error léxico - " + t.value[0] , t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('left','OR'),
    ('left','AND'),
    ('right','UNOT'),
    ('left','IGUALIGUAL','DIFERENTE','MENORQUE','MENORIGUAL','MAYORQUE','MAYORIGUAL'),
    ('left','MAS','MENOS'),
    ('left','DIV','POR','MOD'),
    ('left','POT'),
    ('right','UMENOS'),
    ('left','INC','DEC'),
    )

from abstract.instruccion import Instruccion
from Instrucciones.Imprimir import  Imprimir
from Instrucciones.Declaración import Declaracion
from Instrucciones.Incremento import Incremento
from Instrucciones.Decrecimiento import Decrecimiento
from Instrucciones.Asignacion import Asignacion
from Instrucciones.If import If
from Instrucciones.While import While
from Instrucciones.For import For
from Instrucciones.Break import Break
from Instrucciones.Main import Main
from Instrucciones.Case import Case
from Instrucciones.Default import Default
from Instrucciones.Switch import Switch
from Instrucciones.Funcion import Funcion
from Instrucciones.Llamada import Llamada
from Instrucciones.Return import Return
from Instrucciones.Continue import Continue
from Instrucciones.DeclaracionArr1 import DeclaracionArr1
from Instrucciones.ModificarArreglo import ModificarArreglo
from Expresiones.Primitivos import Primitivos
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
from Expresiones.Identificador import Identificador
from Expresiones.Read import Read
from Expresiones.Casteo import Casteo
from Expresiones.AccesoArreglo import AccesoArreglo
from Nativas.ToUpper import ToUpper
from Nativas.ToLower import ToLower
from Nativas.Length import Length
from Nativas.Truncate import Truncate
from Nativas.Round import Round
from Nativas.Typeof import Typeof
from TS.Tipo import TIPO, OperadorAritmetico, OperadorRelacional, OperadorLogico


def p_error(t):
    print('Error, Algo salio mal :(')

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_instrucciones_instruccion(t) :
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : imprimir_instr finins
                        | declaracion_instr finins
                        | asignacion_instr finins
                        | if_instr
                        | while_instr
                        | break_instr finins
                        | for_instr
                        | switch_instr
                        | main_instr
                        | funcion_instr
                        | llamada_instr finins
                        | return_instr finins
                        | continue_instr finins
                        | declArr_instr finins
                        | modArr_instr finins
    '''
    t[0] = t[1]

def p_finins(t) :
    '''finins       : PUNTOCOMA
                    | '''
    t[0] = None

def p_instruccion_error(t):
    'instruccion        : error PUNTOCOMA'
    errores.append(Excepcion("Sintáctico","Error Sintáctico." + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""

def p_imprimir(t) :
    'imprimir_instr     : RPRINT PARA expresion PARC'
    t[0] = Imprimir(t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_declaracion(t) :
    '''declaracion_instr     : RVAR ID IGUAL expresion
                             | RVAR ID
    '''
    if len(t)==3:
        t[0] = Declaracion(t[2], t.lineno(2), find_column(input, t.slice[2]))
        print()
    else:
        t[0] = Declaracion(t[2], t.lineno(2), find_column(input, t.slice[2]), t[4])
        print()

def p_declArr(t) :
    '''declArr_instr     : tipo1

    '''
    t[0] = t[1]

def p_tipo1(t) :
    '''tipo1     : tipo lista_Dim ID IGUAL RNEW tipo lista_expresiones'''
    t[0] = DeclaracionArr1(t[1], t[2], t[3], t[6], t[7], t.lineno(3), find_column(input, t.slice[3]))

def p_lista_Dim1(t) :
    'lista_Dim     : lista_Dim CORA CORC'
    t[0] = t[1] + 1

def p_lista_Dim2(t) :
    'lista_Dim    : CORA CORC'
    t[0] = 1

def p_lista_expresiones_1(t) :
    'lista_expresiones     : lista_expresiones CORA expresion CORC'
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_expresiones_2(t) :
    'lista_expresiones    : CORA expresion CORC'
    t[0] = [t[2]]

def p_modArr(t) :
    '''modArr_instr     :  ID lista_expresiones IGUAL expresion'''
    t[0] = ModificarArreglo(t[1], t[2], t[4], t.lineno(1), find_column(input, t.slice[1]))



def p_asignacion(t) :
    '''asignacion_instr     : ID IGUAL expresion
                             | ID INC
                             | ID DEC
    '''
    if len(t)==3 and t[2] == '++':
        t[0] = Incremento(t[1], t.lineno(1), find_column(input,t.slice[1]))
    elif len(t)==3 and t[2] == '--':
        t[0] = Decrecimiento(t[1], t.lineno(1), find_column(input, t.slice[1]))
    else:
        t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_Arreglo(t):
    '''expresion : ID lista_expresiones'''
    t[0] = AccesoArreglo(t[1], t[2], t.lineno(1), find_column(input, t.slice[1]))

def p_tipo(t) :
    '''tipo     : RINT
                | RDOUBLE
                | RSTRING
                | RCHAR
                | RBOOL
                '''
    if t[1].lower() == 'int':
        t[0] = TIPO.ENTERO
    elif t[1].lower() == 'double':
        t[0] = TIPO.DECIMAL
    elif t[1].lower() == 'string':
        t[0] = TIPO.CADENA
    elif t[1].lower() == 'char':
        t[0] = TIPO.CARACTER
    elif t[1].lower() == 'boolean':
        t[0] = TIPO.BOOLEANO

def p_if1(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], None, None, t.lineno(1), find_column(input, t.slice[1]))

def p_if2(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], t[10], None, t.lineno(1), find_column(input, t.slice[1]))

def p_if3(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instr'
    t[0] = If(t[3], t[6], None, t[9], t.lineno(1), find_column(input, t.slice[1]))

def p_while(t) :
    'while_instr     : RWHILE PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = While(t[3], t[6], t.lineno(1), find_column(input, t.slice[1]))

def p_for1(t) :
    'for_instr     : RFOR PARA declaracion_instr PUNTOCOMA expresion PUNTOCOMA asignacion_instr PARC LLAVEA instrucciones LLAVEC'
    t[0] = For(t[3], t[5], t[7],t[10],t.lineno(1), find_column(input, t.slice[1]))

def p_for2(t) :
    'for_instr     : RFOR PARA asignacion_instr PUNTOCOMA expresion PUNTOCOMA asignacion_instr PARC LLAVEA instrucciones LLAVEC'
    t[0] = For(t[3], t[5], t[7],t[10],t.lineno(1), find_column(input, t.slice[1]))

def p_break(t) :
    'break_instr     : RBREAK'
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))

def p_switch(t):
    'switch_instr      : RSWITCH PARA expresion PARC LLAVEA cases LLAVEC'
    t[0] = Switch(t[3], t[6],t.lineno(1), find_column(input, t.slice[1]))

def p_cases_cases_case(t) :
    'cases    : cases case'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_cases_case(t) :
    'cases    : case'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_case(t) :
    '''case      : RCASE expresion DOSPUNTOS instrucciones
                 | RDEFAULT DOSPUNTOS instrucciones
    '''
    if t[1] == "case":
        t[0] = Case(t[2],t[4],t.lineno(1), find_column(input, t.slice[1]))
    if t[1] == "default":
        t[0] = Default(t[3],t.lineno(1), find_column(input, t.slice[1]))


def p_expresion_binaria(t):
    '''
    expresion : expresion MAS expresion
            | expresion MENOS expresion
            | expresion POR expresion
            | expresion DIV expresion
            | expresion POT expresion
            | expresion MOD expresion
            | expresion MENORQUE expresion
            | expresion MAYORQUE expresion
            | expresion IGUALIGUAL expresion
            | expresion DIFERENTE expresion
            | expresion MENORIGUAL expresion
            | expresion MAYORIGUAL expresion
            | expresion AND expresion
            | expresion OR expresion
    '''
    if t[2] == '+':
        t[0] = Aritmetica(OperadorAritmetico.MAS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(OperadorAritmetico.MENOS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional(OperadorRelacional.MENORQUE, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional(OperadorRelacional.MAYORQUE, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '==':
        t[0] = Relacional(OperadorRelacional.IGUALIGUAL, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '&&':
        t[0] = Logica(OperadorLogico.AND, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Logica(OperadorLogico.OR, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*':
        t[0] = Aritmetica(OperadorAritmetico.POR, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/':
        t[0] = Aritmetica(OperadorAritmetico.DIV, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '**':
        t[0] = Aritmetica(OperadorAritmetico.POT, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%':
        t[0] = Aritmetica(OperadorAritmetico.MOD, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '=!':
        t[0] = Relacional(OperadorRelacional.DIFERENTE, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional(OperadorRelacional.MENORIGUAL, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional(OperadorRelacional.MAYORIGUAL, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))

def p_expresion_unaria(t):
    '''
    expresion : MENOS expresion %prec UMENOS
            | NOT expresion %prec UNOT
    '''
    if t[1] == '-':
        t[0] = Aritmetica(OperadorAritmetico.UMENOS, t[2],None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
        t[0] = Logica(OperadorLogico.NOT, t[2],None, t.lineno(1), find_column(input, t.slice[1]))


def p_expresion_agrupacion(t):
    '''
    expresion :   PARA expresion PARC
    '''
    t[0] = t[2]

def p_expresion_identificador(t):
    '''expresion : ID'''
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_llamada(t):
    '''expresion : llamada_instr'''
    t[0] = t[1]

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    t[0] = Primitivos(TIPO.ENTERO,t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_decimal(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivos(TIPO.DECIMAL, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_cadena(t):
    '''expresion : CADENA'''
    t[0] = Primitivos(TIPO.CADENA,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_caracter(t):
    '''expresion : CARACTER'''
    t[0] = Primitivos(TIPO.CARACTER,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_nulo(t):
    '''expresion : RNULL'''
    t[0] = Primitivos(TIPO.NULO,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))
def p_primitivo_true(t):
    '''expresion : RTRUE'''
    t[0] = Primitivos(TIPO.BOOLEANO, True, t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_false(t):
    '''expresion : RFALSE'''
    t[0] = Primitivos(TIPO.BOOLEANO, False, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_read(t):
    '''expresion : RREAD PARA PARC'''
    t[0] = Read(t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_cast(t):
    '''expresion : PARA tipo PARC expresion'''
    t[0] = Casteo(t[2], t[4], t.lineno(1), find_column(input, t.slice[1]))

def p_main(t) :
    'main_instr     : RMAIN PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Main(t[5], t.lineno(1), find_column(input, t.slice[1]))


def p_funcion_1(t):
    '''
    funcion_instr     : RFUNC ID PARA parametros PARC LLAVEA instrucciones LLAVEC
                      | RFUNC ID PARA PARC LLAVEA instrucciones LLAVEC
    '''
    if len(t) == 9:
        t[0] = Funcion(t[2], t[4], t[7], t.lineno(1), find_column(input, t.slice[1]))
    else:
        t[0] = Funcion(t[2], [], t[6], t.lineno(1), find_column(input, t.slice[1]))





# ///////////////////////////////////////PARAMETROS//////////////////////////////////////////////////

def p_parametros_1(t):
    'parametros     : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]


def p_parametros_2(t):
    'parametros    : parametro'
    t[0] = [t[1]]


# ///////////////////////////////////////PARAMETRO//////////////////////////////////////////////////

def p_parametro(t):
    'parametro     : tipo ID'
    t[0] = {'tipo': t[1], 'identificador': t[2]}


# ///////////////////////////////////////LLAMADA A FUNCION//////////////////////////////////////////////////

def p_llamada1(t):
    'llamada_instr     : ID PARA PARC'
    t[0] = Llamada(t[1], [], t.lineno(1), find_column(input, t.slice[1]))


def p_llamada2(t):
    'llamada_instr     : ID PARA parametros_llamada PARC'
    t[0] = Llamada(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))



# ///////////////////////////////////////PARAMETROS LLAMADA A FUNCION//////////////////////////////////////////////////

def p_parametrosLL_1(t):
    'parametros_llamada     : parametros_llamada COMA parametro_llamada'
    t[1].append(t[3])
    t[0] = t[1]


def p_parametrosLL_2(t):
    'parametros_llamada    : parametro_llamada'
    t[0] = [t[1]]


# ///////////////////////////////////////PARAMETRO LLAMADA A FUNCION//////////////////////////////////////////////////

def p_parametroLL(t):
    'parametro_llamada     : expresion'
    t[0] = t[1]

def p_return(t) :
    'return_instr     : RRETURN expresion'
    t[0] = Return(t[2], t.lineno(1), find_column(input, t.slice[1]))


def p_continue(t) :
    'continue_instr     : RCONTINUE'
    t[0] = Continue(t.lineno(1), find_column(input, t.slice[1]))

import ply.yacc as yacc
parser = yacc.yacc()

input = ''

def parse(inp) :
    global errores
    global lexer
    global parser
    errores = []
    lexer = lex.lex()
    lexer = lex.lex(reflags=re.IGNORECASE)
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)

def crearNativas(ast):          # CREACION Y DECLARACION DE LAS FUNCIONES NATIVAS
    nombre = "toupper"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'toUpper##Param1'}]
    instrucciones = []
    toUpper = ToUpper(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(toUpper)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    nombre = "tolower"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'toLower##Param1'}]
    instrucciones = []
    toLower = ToLower(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(toLower)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    nombre = "length"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'Length##Param1'}]
    instrucciones = []
    length = Length(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(length)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    nombre = "truncate"
    parametros = [{'tipo':TIPO.DECIMAL,'identificador':'Truncate##Param1'}]
    instrucciones = []
    truncate = Truncate(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(truncate)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    nombre = "round"
    parametros = [{'tipo': TIPO.DECIMAL, 'identificador': 'Round##Param1'}]
    instrucciones = []
    ro = Round(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(ro)  # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    nombre = "typeof"
    parametros = [{'tipo': TIPO.DECIMAL, 'identificador': 'Typeof##Param1'}]
    instrucciones = []
    typeof = Typeof(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(typeof)  # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)




rerror = []

consola = ""
reporterror = ""
reporttabla = ""
cont = 1.0
def run(entrada, texto):
    global consola
    global reporterror
    global cont
    global reporttabla

    from TS.Arbol import Arbol
    from TS.TablaSimbolos import TablaSimbolos

    #print(entrada5.lower())
    instrucciones = parse(entrada.lower()) #ARBOL AST
    ast = Arbol(instrucciones)
    ast.setTexto(texto)
    TSGlobal = TablaSimbolos()
    ast.setTSglobal(TSGlobal)
    crearNativas(ast)
    for error in errores:                   #CAPTURA DE ERRORES LEXICOS Y SINTACTICOS
        ast.getExcepciones().append(error)
        ast.updateConsola(error.toString())

    for instruccion in ast.getInstrucciones():      # 1ERA PASADA (DECLARACIONES Y ASIGNACIONES)
        if isinstance(instruccion, Funcion):
            ast.addFuncion(instruccion)
        if isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion) or isinstance(instruccion, DeclaracionArr1) or isinstance(instruccion, ModificarArreglo):
            value = instruccion.interpretar(ast,TSGlobal)
            if isinstance(value, Excepcion) :
                ast.getExcepciones().append(value)
                ast.getExcepciones()
                ast.updateConsola(value.toString())
                rerror.append(value.toString())
            if isinstance(value, Break):
                err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
                rerror.append(err.toString())

    for instruccion in ast.getInstrucciones():      # 2DA PASADA (MAIN)
        contador = 0
        if isinstance(instruccion, Main):
            contador += 1
            if contador == 2: # VERIFICAR LA DUPLICIDAD
                err = Excepcion("Semantico", "Existen 2 funciones Main", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
                rerror.append(err.toString())
                break
            value = instruccion.interpretar(ast,TSGlobal)
            if isinstance(value, Excepcion) :
                ast.getExcepciones().append(value)
                ast.updateConsola(value.toString())
            if isinstance(value, Break):
                err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
                rerror.append(err.toString())
            if isinstance(value, Return):
                err = Excepcion("Semantico", "Sentencia RETURN fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
            if isinstance(value, Imprimir):
                print('consola'+ast.getConsola())
                texto.insert(tk.END,ast.getConsola())
                ast.setConsola("")

    for instruccion in ast.getInstrucciones():
        if not (isinstance(instruccion, Main) or isinstance(instruccion, Declaracion) or isinstance(instruccion,Asignacion) or isinstance(instruccion, Funcion) or isinstance(instruccion, DeclaracionArr1) or isinstance(instruccion,ModificarArreglo)):
            print(type(instruccion))
            err = Excepcion("Semantico", "Sentencias fuera de Main", instruccion.fila, instruccion.columna)
            ast.getExcepciones().append(err)
            ast.updateConsola(err.toString())
            rerror.append(err.toString())
    for errr in ast.getExcepciones():
        rerror.append(errr.toString())

    init = NodoAST("RAIZ")
    instr = NodoAST("INSTRUCCIONES")

    for instruccion in ast.getInstrucciones():
        instr.agregarHijoNodo(instruccion.getNodo())

    init.agregarHijoNodo(instr)
    grafo = ast.getDot(init)  # DEVUELVE EL CODIGO GRAPHVIZ DEL AST

    dirname = os.path.dirname(__file__)
    direcc = os.path.join(dirname, 'ast.dot')
    arch = open(direcc, "w+")
    arch.write(grafo)
    arch.close()
    os.system('dot -T pdf -o ast.pdf ast.dot')

    consola = ast.getConsola()


    inarchivo = """ 
        <!DOCTYPE html>
    <html>
        <head>
            <title>Tablas</title>
        </head>
        <body>
            <table border="1px">
                <tr>
                    <td><b>Error</b></td>
                </tr>
        """
    for er in rerror:
        inarchivo = inarchivo + """
            <tr>
            <td>
            """+str(er)+"""</td>
            </tr>
            """
    inarchivo = inarchivo + """
        </table>
        </body>
        </html>
        """
    reporterror = inarchivo

    inarchivo = """ 
        <!DOCTYPE html>
    <html>
        <head>
            <title>Tablas</title>
        </head>
        <body>
            <table border="1px">
                <tr>
                    <td><b>Identificador</b></td>
                    <td><b>Expresion</b></td>
                    <td><b>Fila</b></td>
                    <td><b>Columna</b></td>
                    <td><b>Tipo</b></td>
                </tr>
        """
    for sim in ast.getSimbolos():
        inarchivo = inarchivo + """
            <tr>
            <td>
            """+str(sim.identificador)+"""</td>
            <td>
            """+str(sim.expresion)+"""</td>
            <td>
            """+str(sim.fila)+"""</td>
            <td>
            """+str(sim.columna)+"""</td>
            <td>
            """+str(sim.tipo)+"""</td>
            </tr>
            """
    inarchivo = inarchivo + """
        </table>
        </body>
        </html>
        """
    reporttabla = inarchivo


