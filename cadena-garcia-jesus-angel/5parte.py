#Primero fijamos las variables y le damos valores
numerotabla =0
numerocambiante=0
resultado = numerotabla * numerocambiante

import time
#Ahora solicitamos el numero que quiere multiplicar el usuario
while True:
	numerotabla = int(input("Dime que tabla de multiplicar quieres saber del 0 al 10\n"))
	for numerocambiante in range (11):
		resultado = numerotabla * numerocambiante
		print (numerotabla, "por", numerocambiante, "=",resultado)
		time.sleep(0.5)
	menu = int(input("¿Quieres saber otra tabla de múltiplicar? (1 si) (2 no)\n"))
	if menu!= 1:
		break
print("Nos vemos cuando quieras aprender más :D")
