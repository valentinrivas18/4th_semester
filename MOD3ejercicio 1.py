cont = "Si"

while cont == "Si":
	print("Realice un programa que imprima todos los números pares entre dos números que se le pidan al usuario.")
	num1 = int(input('Ingrese el primer numero: '))
	num2 = int(input('Ingrese el segundo numero: '))

	lista = []
	lista.extend(range(num1,num2+1))

	for i in lista:
		if i % 2 == 0:
			print(i, end = " ")

	print('Desea continuar?')
	print('Si - No')
	cont1 = str(input())
	cont = cont1.capitalize()