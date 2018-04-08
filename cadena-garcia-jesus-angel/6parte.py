#Fijar las variables y establecer sus valores
numeropar = 0
multiprodetres=0
#pedir un numero al usuario para decir si es par impar o multipro de 3
while True:
	numeropar= int(input("Dime un numero y te dire si es par impar o multipro de 3\n"))
	multiprodetres=numeropar
	if numeropar %2 == 0:
		print("es un numero par")
	else:
		print("es un numero impar")
	if multiprodetres % 3 ==0:
		print("es multipro de tres")
	menu = int(input("¿Quieres saber otra tabla de múltiplicar? (1 si) (2 no)\n"))
	if menu!= 1:
		break
print("Nos vemos cuando quieras aprender más :D")