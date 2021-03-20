cont = "Si"

while cont == "Si":

	print('1. Suma, resta, división y multiplicación de dos numeros')
	print('2. Dado un número entero N, imprimir su tabla de multiplicar.')
	print('3. Dado un número entero N, imprimir su factorial.')

	operacion = int(input('Ingrese el numero de la operacion que desea realizar: '))


	if operacion == 1:
		n1 = int(input('Ingrese el primer numero: '))
		n2 = int(input('Ingrese el segundo numero: '))
		suma = n1 + n2
		div = n1 / n2
		mult = n1 * n2

		print(f'La suma es {suma}, la multiplicacion es: {mult}, y su division es: {div}')

	elif operacion == 2:
		numero = int(input('Ingrese el numero cuya tabla de multiplicar desea ver: '))
		for i in range(1, 11):
			print(f'{i} x {numero} = {i * numero}')

	elif operacion == 3:
		n = int(input('Ingrese un numero: '))
		factorial = 1
		for i in range(n):
			factorial *= n
			n -= 1
		print(f"El factorial es: {factorial}")

	else:
		print("Porfavor ingrese un valor valido.")


	print('Desea continuar?')
	print('Si - No')
	cont1 = str(input())
	cont = cont1.capitalize()