#playfair

llave=input()
cadena=input()

alfabeto=['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def limpiarLlave(llave,alfabeto):
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
	return matriz

print(generarmatriz(limpiarLlave(llave,alfabeto),alfabeto))
