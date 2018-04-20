#Fijamos las variables y su valor
import time
numero1 = 0
numero1= int(input("Dame un numero para la cuenta atras \n"))
for i in range(1,numero1):
	print ("",numero1-i)
	time.sleep(0.5)
print ("El cohete ha despegado")