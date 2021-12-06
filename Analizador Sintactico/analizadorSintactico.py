import ply.yacc as yacc
import os
import codecs
import re
import analizadorLexico
from analizadorLexico import tokens

precedence = (
		('right', 'IF', 'FOR', 'TO', 'THEN', 'ELSE'),
		('right', 'ID','ASIGNAR'),
		('left', 'NOIGUAL','MENORQ', 'MENORIGUALQ', 'MAYORQ', 'MAYORIGUALQ'),
		('left', 'SUMA', 'RESTA'),
		('left', 'MULTIPLICADO', 'DIVIDIDO'),
		('left', 'IPARENT', 'DPARENT'),
		('left', 'ICOR', 'DCOR'),
		('right', 'URESTA')
	)

###################INICIO###########################

def p_programa(p):
	'''programa : listaSentencias'''
	print('programa')

###################LISTA DE SENTENCIAS###########################

def p_lista_sentencias1(p):
	'''listaSentencias : sentencia'''
	print('sentencia')

def p_lista_sentencias2(p):
	'''listaSentencias : listaSentencias sentencia'''
	print('lista Sentencia')

###################SENTENCIA###########################

def p_imprimir(p):
	'''sentencia : IMP IPARENT expresion DPARENT'''
	print('sent -> imprimir')

def p_asig_var(p):
	'''sentencia : ID ASIGNAR expresion'''
	print('sent -> asig_var ID =')

def p_sent_for(p):
	'''sentencia : FOR sentencia TO expresion THEN ILLAVE listaSentencias DLLAVE'''
	print('sent -> for')

def p_sent_if(p):
	'''sentencia : IF condicion THEN ILLAVE listaSentencias DLLAVE ELSE ILLAVE listaSentencias DLLAVE'''
	print('sent -> if')

###################EXPRESION###########################
def p_expresion1(p):
	'''expresion : term'''
	print('expresion -> term')

def p_expresion5(p):
        """
        expresion : expresion SUMA expresion
                  | expresion RESTA expresion
                  | expresion MULTIPLICADO expresion
                  | expresion DIVIDIDO expresion
        """

        if p[2] == '+':
            print('expresion -> suma')
        elif p[2] == '-':
            print('expresion -> resta')
        elif p[2] == '*':
            print('expresion -> mul')
        elif p[2] == '/':
            print('expresion -> div')

def p_expresion4(p):
	'''expresion : term concatenar term'''
	print('expresion -> concat')

###################CONCATENAR###########################

def p_concatenar(p):
	'''concatenar : CONCAT'''
	print('concat -> &')
###################CONDICION###########################

def p_condicion(p):
	'''condicion : expresion relacion expresion'''
	if p[2] == '==': print('expresoin-> expresion == expresion')
	elif p[2] == '<>': print('expresoin-> expresion <> expresion')
	elif p[2] == '>': print('expresoin-> expresion > expresion')
	elif p[2] == '<': print('expresoin-> expresion < expresion')

###################RELACION###########################

def p_relacion1(p):
	'''relacion : ASIGNAR'''
	print('relacion -> =')

def p_relacion2(p):
	'''relacion : NOIGUAL'''
	print('<>')

def p_relacion3(p):
	'''relacion : MENORQ'''
	print('<')

def p_relacion4(p):
	'''relacion : MAYORQ'''
	print('>')

def p_relacion5(p):
	'''relacion : MENORIGUALQ'''
	print('<=')

def p_relacion6(p):
	'''relacion : MAYORIGUALQ'''
	print('>=')

def p_relacion7(p):
	'''relacion : IGUAL'''
	print('==')

###################TERMINO###########################


def p_term1(p):
	'''term : factor'''
	print('term-> factor')

def p_term4(p):
	'''term : IPARENT expresion DPARENT'''
	print('term-> ( E )')

def p_term7(p):
	'''term : ICOR expresion DCOR'''
	print('term-> [ E ]')

###################FACTOR###########################


def p_factor1(p):
	'''factor : ID'''
	print('id')


def p_factor2(p):
	'''factor : RESTA ENTERO %prec URESTA
			  | RESTA DECIMAL %prec URESTA
			  | ENTERO
			  | DECIMAL'''
	if p[1]=='-':
		print('num_neg')
	else:
		print('num')


def p_factor6(p):
	'''factor : STR'''
	print('cadena')


def p_factorEmpty(p):
	'''factor : empty'''

###################VACIO###########################


def p_empty(p):
	'''empty :'''
	pass

###################ERROR###########################


def p_error(p):
	print( "Error en la linea "+str(p.lineno) )
	if p is not None:
		print ("Syntax error at line " + str(p.lexer.lineno) + " Unexpected token  " + str(p.value) )
	else:
		print ("Syntax error at line: " + str(analizadorLexico.lexer.lineno) )

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print( str(cont)+". "+file )
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nseleccionar una prueba: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print( "Has seleccinado \"%s\" \n" %files[int(numArchivo)-1] )

	return files[int(numArchivo)-1]

directorio = './pruebas/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)






