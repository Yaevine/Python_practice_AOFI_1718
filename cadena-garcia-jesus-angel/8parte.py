#fijamos las variables y le damos valores
import time
comida=0
dia=0
almuerzo={}
cena={}
#señalamos la semana y sus dias correspondientes
semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
print ("Qué deseas comer esta semana\n")
time.sleep(1)
for dia in semana:
	comida = input (dia + ": ¿Qué quieres almorzar?\n")
	almuerzo[dia] = comida
	comida = input (dia + ": ¿Qué quieres cenar?\n")
	cena[dia] = comida
print("Este es el menu que has elegido :D")
time.sleep(2)
for dia in semana:
	print(dia, "-", "almuerzo:", almuerzo[dia], "cena:", cena[dia])
	time.sleep(1.5)