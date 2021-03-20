cont = "Si"

while cont == "Si":
	def suma(n1,n2):
		totals=n1+n2
		return(totals)
	def resta(n1,n2):
		totalr=n1-n2
		return(totalr)
	def multip(n1,n2):
		totalm=n1*n2
		return(totalm)
	def div(n1,n2):
		while n2 == 0:
			n2 = int(input('Ingrese el segundo numero que no sea cero: '))
		totald=n1/n2
		return(totald)

	print("""Realice un programa que permita introducir 2 números y seleccionar la 
	operación matemática que se desea, SUMAR, RESTAR, MULTIPLICAR, DIVIDIR.""")
	print('1. Sumar')
	print('2. Restar')
	print('3. Multiplicar')
	print('4. Dividir')

	calltoact = int(input('Ingrese el numero de operacion que desea realizar en indice: '))

	if calltoact == 1:
		n1 = int(input('Ingrese el primer numero: '))
		n2 = int(input('Ingrese el segundo numero: '))
		print(suma(n1,n2))
	elif calltoact == 2:
		n1 = int(input('Ingrese el primer numero: '))
		n2 = int(input('Ingrese el segundo numero: '))
		print(resta(n1,n2))
	elif calltoact == 3:
		n1 = int(input('Ingrese el primer numero: '))
		n2 = int(input('Ingrese el segundo numero: '))
		print(multip(n1,n2))
	elif calltoact == 4:
		n1 = int(input('Ingrese el primer numero: '))
		n2 = int(input('Ingrese el segundo numero: '))
		print(div(n1,n2))
	else:
		print('Ingrese un numero valido.')

	print('Desea continuar?')
	print('Si - No')
	cont1 = str(input())
	cont = cont1.capitalize()