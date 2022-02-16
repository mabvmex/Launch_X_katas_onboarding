
# Almacena las entradas del usuario
valor1 = input('Introduce la distancia del 1er planeta: ')
valor2 = input('Introduce la distancia del 2er planeta: ')

# print(valor1)
# print(valor2)



# Convierte las cadenas de ambos planetas a números enteros
valor1 = int(valor1)
valor2 = int(valor2)

# print(valor1)
# print(valor2)



# Realizar el calculo y determinar el valor absoluto
# Convertir de KM a Millas
mile = 0.621371

print(20*'-')
TotalDistance = abs(int(valor1) - int(valor2))
print('The distance (in km) between planets is: ', TotalDistance, 'km')
DistanceInMiles = abs(TotalDistance * mile)
print('The distance (in miles) between planets is: ', int(DistanceInMiles), 'miles')