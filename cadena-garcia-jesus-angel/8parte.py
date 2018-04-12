import time
comida = 0
dia = 0
almuerzo = {}
cena = {}
semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print ("¿Que menu vas a querer esta semana?\n")
time.sleep(2)
 for dia in semana:
 	comida=input("¿Que quieres para almorzar?")
 	almuerzo[dia]=comida
 	comida=input("¿Que quieres para cenar?")
 	cena[dia]=comida
 print("Este es el menu para esta semana")
 time.sleep(2)
 for dia in semana:
 	print("[",dia,"]","-", "Almuerzo:", "[",almuerzo[dia], "Cena:", "[",cena[dia],"]")
 	time.sleep(1)