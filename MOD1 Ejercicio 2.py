from math import sqrt
cont = "Si"

while cont == "Si":

	print('1. Perimetro y area de un rectangulo dado su base y altura')
	print('2. Perimetro y area de un circulo dado su radio')
	print('3. Volumen de una esfera dado su radio')
	print('4. Calcule su hipotenusa, dados los catetos de un triángulo rectángulo')

	funcion = str(input('Ingrese el numero de la operacion que desea calcular: '))
	pi = 3.1415


	if funcion == "1":
		print('Calculo de el area')
		base = int(input('Ingrese base: '))
		altura = int(input('Ingrese altura: '))
		print('Calculo de el perimetro')
		lado1 = int(input('Ingrese el lado superior: '))
		lado2 = int(input('Ingrese el lado lateral: '))
		def areaf(base,altura):
			area_rec = base * altura
			return(area_rec)
		def perimetrof(lado1,lado2):
			perimetro_rec = 2 * (lado1 + lado2)
			return(perimetro_rec)
		print(f"El area del rectangulo es: {areaf(base,altura)} y su perimetro es: {perimetrof(lado1,lado2)}")


	elif funcion == "2":
		print('Calculo del radio y perimetro del circulo.')
		radioo = int(input('Ingrese el radio: '))
		radio2 = radioo * radioo
		def radiof(radio2):
			area_circ = pi * radio2
			return(area_circ)
		def radiopf(pi,radio2):
			perimetro_circ =  2 * pi * radioo
			return(perimetro_circ)
		print(f"El area del circulo es: {radiof(radio2)} y su perimetro es: {radiopf(pi,radio2)}")


	elif funcion == "3":
		k = 4/3
		radioo = int(input('Ingrese el radio: '))
		radio3 = radioo ** 3
		def volumef(radio3):
			volume_esf = k * pi * radio3
			return(volume_esf)
		print(f"El volumen de la esfera es: {volumef(radio3)}")


	elif funcion == "4":
		cat_a = int(input('Ingrese el cateto A: '))
		cat_b = int(input('Ingrese el cateto B: '))
		def hipotenusa(cat_a,cat_b):
			hipo = (cat_a ** 2) + (cat_b ** 2 )
			hipo = sqrt(hipo)
			return(hipo)
		print(f"La hipotenusa del triangulo rectangulo es: {hipotenusa(cat_a,cat_b)}")

	else:
		print("Porfavor ingrese un valor valido.")

	print('Desea continuar?')
	print('Si - No')
	cont1 = str(input())
	cont = cont1.capitalize()