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

def limpiarLlave(llave,alfabeto):	#Limpia la llave
	llave = llave.lower()
	llaveLimpia= []
	for c in llave:
		#Si el caracter no esta, lo descarta
		if c in alfabeto:
			#Si no esta anteriormente la agrega a la cadena limpia
			if not (c in llaveLimpia):	llaveLimpia.append(c)
	return llaveLimpia

def generarmatriz(llave,alfabeto):	#Genera la matriz de encriptaccion
	matriz=[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
	mapa = {} #Diccionario
	tLlave = len(llave)
	contador = 0
	#Crear alfabeto sin elementos de la llave
	for c in llave:
		alfabeto.remove(c)
	#Crea la matriz
	for i in range(5):
		for j in range(5):
			valor=''
			if contador<tLlave:
				valor = llave[contador]
				matriz[i][j] = valor
				contador += 1
			else:
				valor = alfabeto.pop(0)
				matriz[i][j] = valor
			mapa[valor] = [i,j]
	#Retorna la matriz de encriptacion
	return matriz,mapa

def limpiarCadena(cadena,alfabeto):	#Limpia la cadena
	cadenaLimpia=[]
	cadena = cadena.replace('j','i')
	cadena = cadena.lower()
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

def encriptarPlayFair(cadena,mapa,matriz,modo=1):
	crip = ''
	if abs(modo) != 1: return 'Modo no valido\n[1] para encriptar\n[-1] para desencriptar'
	for par in cadena:
		#Obtenemos la pocicion de los caracteres en la matriz
		p1 = mapa[par[0]] #Caracter 1 
		p2 = mapa[par[1]] #Caracter 2
		#Determinamos la forma de encriptar
		if p1[0]==p2[0]:	#Si ambos estan en la misma fila
			crip = crip + matriz[p1[0]][(p1[1]+modo)%5] + matriz[p2[0]][(p2[1]+modo)%5]
		elif p1[1]==p2[1]:	#Si ambos estan en la misma columna
			crip = crip + matriz[(p1[0]+modo)%5][p1[1]] + matriz[(p2[0]+modo)%5][p2[1]]
		else:				#Si estan en diferentes filas y columnas
			crip = crip + matriz[p1[0]][p2[1]] + matriz[p2[0]][p1[1]]
	return crip

def playFair(llave,cadena,modo='e'):
	llaveLimpia		= limpiarLlave(llave,alfabeto)
	matriz,mapa		= generarmatriz(llaveLimpia, list(alfabeto))
	cadenaLimpia	= limpiarCadena(cadena,alfabeto)
	cadenaProcesada	= encriptarPlayFair(cadenaLimpia,mapa,matriz,-1)

#MAIN
clear()
llave=input('Ingrese llave:\n')
cadena=input('Ingrese cadena:\n')

#Print (Comentar o eliminar despues)
clear()
print(llaveLimpia)
print()
print(cadenaLimpia)
print()
for a in matriz: print(a)
print()
print(mapa)
print()
print(llave)
print(cadena)
print(cadenaProcesada.upper())