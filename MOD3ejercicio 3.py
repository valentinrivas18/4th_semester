cont = "Si"

while cont == "Si":
	print("Realice un programa que lea la hora expresada en horas, minutos y segundos, y las tiene que mostrar en pantalla expresadas en el total de segundos.")

	horas = int(input("Ingrese horas: ")) * 3600
	minutos = int(input("Ingrese los minutos: ")) * 60
	segundos = int(input("Ingrese los segundos: "))

	tiempo = horas + minutos + segundos

	print("Hora, minutos y segundos totales en segundo: ", tiempo)

	print('Desea continuar?')
	print('Si - No')
	cont1 = str(input())
	cont = cont1.capitalize()