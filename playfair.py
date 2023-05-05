#playfair
import os

#Variables
alfabeto=['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Funciones
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def limpiarLlave(llave,alfabeto):#Limpia la llave
	llave = llave.lower()
	llaveLimpia= []
	for c in llave:
		#Si el caracter no esta, lo descarta
		if c in alfabeto:
			#Si no esta anteriormente la agrega a la cadena limpia
			if not (c in llaveLimpia):	llaveLimpia.append(c)
	return llaveLimpia

def generarmatriz(llave,alfabeto):#Genera la matriz de encriptaccion
	matriz=[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
	tLlave = len(llave)
	contador = 0
	#Crear alfabeto sin elementos de la llave
	for c in llave:
		alfabeto.remove(c)
	#Crea la matriz
	for i in range(5):
		for j in range(5):
			if contador<tLlave:
				matriz[i][j] = llave[contador]
				contador += 1
			else: 
				matriz[i][j] = alfabeto.pop(0)
	#Retorna la matriz de encriptacion
	return matriz

def limpiarCadena(cadena,alfabeto):
	cadenaLimpia=[]
	cadena = cadena.replace('j','i')
	listaCadena = []
	for c in cadena:
		if c in alfabeto:
			listaCadena.append(c)
	#Genera las parejas
	while True:
		
		if len(listaCadena) == 0: break
		if len(listaCadena) == 1: listaCadena.append('x')

		if listaCadena[0] == listaCadena[1]:
			#Si es repetido
			c1 = listaCadena.pop(0)
			cadenaLimpia.append([c1,'x'])
		else:
			c1 = listaCadena.pop(0)
			c2 = listaCadena.pop(0)
			cadenaLimpia.append([c1,c2])
		
	return cadenaLimpia

def encriptarPlayFair():
	cadenaEncriptada = ''
	
	return cadenaEncriptada
#MAIN
clear()
llave=input('Ingrese llave:\n')
cadena=input('Ingrese cadena:\n')
llaveLimpia	= limpiarLlave(llave,alfabeto)
matriz		= generarmatriz(llaveLimpia, list(alfabeto))
cadenaLimpia= limpiarCadena(cadena,alfabeto)

#Print
clear()
print(llaveLimpia)
print()
print(cadenaLimpia)
print()
for a in matriz: print(a)
print()
print(llave)
print(cadena)