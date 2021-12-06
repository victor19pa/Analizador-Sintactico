import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = [
				
				'IF',
				'THEN',
				'FOR',
				'TO',
				'ELSE',
				'IMP'
			]

tokens = reservadas+[
						'ID',
						'ENTERO',
						'DECIMAL',
						'SUMA',
						'RESTA',
						'MULTIPLICADO',
						'DIVIDIDO',
						'ASIGNAR',
						'NOIGUAL',
						'IGUAL',
						'MENORQ',
						'MENORIGUALQ',
						'MAYORQ',
						'MAYORIGUALQ',
						'IPARENT',
						'DPARENT',
						'COMA',
						'PUNTOCOMA',
						'STR',
						'ILLAVE',
						'DLLAVE',
						'ICOR',
						'DCOR',
						'CONCAT'
					]

t_ignore = '\r \t'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICADO = r'\*'
t_DIVIDIDO = r'/'
t_ASIGNAR = r'='
t_NOIGUAL = r'<>'
t_IGUAL = r'=='
t_MENORQ = r'<'
t_MENORIGUALQ = r'<='
t_MAYORQ = r'>'
t_MAYORIGUALQ = r'>='
t_IPARENT = r'\('
t_DPARENT = r'\)'
t_COMA = r','
t_PUNTOCOMA = r';'
t_ILLAVE = r'{'
t_DLLAVE = r'}'
t_ICOR = r'\['
t_DCOR = r'\]'
t_CONCAT = r'\&'


def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		#reservadas.get(t.value,'ID')
		t.type = t.value

	return t

def t_STR(t):
	r'".*"'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value
		
	t.value = t.value[1:-1]
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print(f"valor decimal muy largo {t.value}")
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f"valor entero muy largo {t.value}")
        t.value = 0
    return t

#dsfjksdlgjklsdgjsdgslxcvjlk-,.
def t_COMMENT(t):
	r'\#.*'
	pass

def t_error(t):
	print(f"caracter inesperado {t.value[0]}")
	t.lexer.skip(1)

# def buscarFicheros(directorio):
# 	ficheros = []
# 	numArchivo = ''
# 	respuesta = False
# 	cont = 1

# 	for base, dirs, files in os.walk(directorio):
# 		ficheros.append(files)

# 	for file in files:
# 		print(str(cont)+". "+file)
# 		cont = cont+1

# 	while respuesta == False:
# 		numArchivo = input('\nseleccionar una prueba: ')
# 		for file in files:
# 			if file == files[int(numArchivo)-1]:
# 				respuesta = True
# 				break

# 	print ("Ha seleccinado \"%s\" \n" %files[int(numArchivo)-1])

# 	return files[int(numArchivo)-1]

# directorio = './pruebas/'
# archivo = buscarFicheros(directorio)
# test = directorio+archivo
# fp = codecs.open(test,"r","utf-8")
# cadena = fp.read()
# fp.close()

analizador = lex.lex()

# analizador.input(cadena)

# while True:
# 	tok = analizador.token()
# 	if not tok : break
# 	print(tok)



	
