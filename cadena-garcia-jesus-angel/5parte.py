#Creo e inicializo las variables
import time
bucle = "si"
tablas = 0
numeros = 0

#Preguntar un numero para las tablas de multiplicar
while bucle == "si":
	tablas = int(input ("De que número quieres saber su tabla de multiplicar:\n"))
	for numeros in range(11):
		print(tablas, " * ", numeros, "=",tablas * numeros)
		time.sleep(0.5)
	bucle = input ("Quieres saber otra tabla de multiplicar: si o no ?\n")	
	if bucle != "si":
		print ("Hasta Luego")
		
