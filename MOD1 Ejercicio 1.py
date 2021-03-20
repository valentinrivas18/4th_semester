cont = "Si"

while cont == "Si":

	print('Calculadora de Bolivar a Dolar/Euro')
	print('Operaciones disponibles...')
	print('1. Bolivar a Dolar')
	print('2. Bolivar a Euro')

	calc = int(input('Ingrese el numero de la operacion: '))

	if calc == 1:
		dolar = int(input('Porfavor, ingresa el valor del dolar al dia de hoy: '))
		bolivar = int(input('Ingresa la cantidad en bolivar que sera convertida a dolar: '))

		result = bolivar / dolar
		print(f'{bolivar} bolivares en dolares es : {result}')

	elif calc == 2:
		euro = int(input('Porfavor, ingresa el valor del Euro al dia de hoy: '))
		bolivar = int(input('Ingresa la cantidad en bolivar que sera convertida a euro: '))

		result = bolivar / euro
		print(f'{euro} bolivares en euros es : {result}')
	else:
		print('El numero es invalido.')

	print('Desea continuar?')
	print('Si - No')
	cont1 = str(input())
	cont = cont1.capitalize()