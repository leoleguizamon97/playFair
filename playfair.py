#playfair

llave=input()
cadena=input()

alfabeto=['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def limpiarLlave(llave):
	llave = llave.lower()
	llaveLimpia= []
	for c in llave:
		if not (c in llaveLimpia): llaveLimpia.append(c)

limpiarLlave(llave)