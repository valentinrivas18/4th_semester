cont = "Si"

while cont == "Si":
	print('Realice un programa que dada una cadena de caracteres')
	print('Dicha cadena en sentido inverso. ')
	print('Imprima la cadena en un sentido y en sentido inverso.')
	cadena = input('Ingrese la cadena de caracteres: ')

	reverso = cadena[::-1]

	print(f'La cadena introducida en inverso se ve asi: {reverso}')
	print(f'La cadena introducida en un sentido y en inverso se ve asi: {cadena}{reverso}')
	print('Desea continuar?')
	print('Si - No')
	cont1 = str(input())
	cont = cont1.capitalize()