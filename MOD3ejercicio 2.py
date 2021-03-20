cont = "Si"

while cont == "Si":
	print("Realice un programa con una función que reciba como parámetro un número entero N y escriba por pantalla el mensaje Hola N veces. Invocarla con distintos valores de N.")
	num1 = int(input('Ingrese un numero: '))

	for i in range(num1):
		print('Hola')
	print('Desea continuar?')
	print('Si - No')
	cont1 = str(input())
	cont = cont1.capitalize()