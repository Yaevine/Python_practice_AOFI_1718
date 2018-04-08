
#Creo y doy valores a las variables
edad       =0
var_nombre =""
# Primero debemos preguntar la edad
edad= int(input("dime tu edad:\n"))
#Comprobamos si el usuario es mayor o menor de edad
if edad > 17:
	var_nombre = input("introduce tu nombre:\n")
	print("hola", var_nombre)
else:
	print("Este pograma es solo para mayores de edad")
#Y para cerrar debemos despedirnos
print("Hasta pronto")