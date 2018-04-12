#Creo e inicializo las variables
import time
answer = ""
lista = []
bucle = "si"
while bucle == "si":
	answer = input("Que quieres añadir a la lista:\n")
	lista.append (answer)
	bucle = input ("Quieres añadir mas datos a la tabla?: si/no ?\n")	
	if bucle != "si":
		for i in lista:
			print(i)
			time.sleep(0.65)

