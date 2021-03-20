cont = "Si"

while cont == "Si":

	print('1. Dado un número entero N, indicar si es o no par.')
	print('2. Dado un número entero N, indicar si es o no primo')


	operasion = int(input('Ingrese el nro. la funcion que desea ejecutar: '))

	if operasion == 1:
		n = int(input('Ingrese un numero: '))
		if n%2==0:
			print(f"{n} es par.")
		else:
			print(f"{n} es impar.")

	elif operasion == 2:
		num = int(input('Ingrese un numero: '))
		for i in range(2, num):
			if num % i == 0:
				print('No es primo')
				break
		else:
			print('Es primo')
	else:
		print('Porfavor ingrese un numero valido.')
	print('Desea continuar?')
	print('Si - No')
	cont1 = str(input())
	cont = cont1.capitalize()