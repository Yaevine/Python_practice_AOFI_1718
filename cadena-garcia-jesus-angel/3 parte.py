#Primero creo las variables y les doy valor
numero1 = 0 
numero2  = 0
numero3 = 0
numerototal = numero1 + numero2 + numero3
#Primero preguntamos el primer numero y luego los siguientes
numero1 = int(input("Introduce un numero mayor que 0 \n"))
if numero1 > 0:
		numero2 = int(input("Introduce un numero mayor que el anterior\n"))
		if numero2 > numero1:
			numero3  = int(input("introduce un numero menor que 0\n"))
			numerototal = numero1 + numero2 + numero3
			if numero3 < 0:
					print (numero1, "+",numero2, "+",numero3, "=", numerototal)
			else:
					print ("numero inadecuado")
		else:
			print ("numero inadecuado")
else:
	print ("numero inadecuado")
