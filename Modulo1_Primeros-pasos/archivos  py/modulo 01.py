
#############################
# Módulo 01 - Primeros pasos
# Por: Miguel Barrera
# launchx04647@innovaccion.mx / ID: 4998
#
#############################



## Función print()
#-----------------
print("Hola desde consola")



## Variables
#-----------------
sum = 1 + 2
product = sum * 2
print(product)



## Tipos de datos
#-----------------
distancia_a_AlfaCentauri = 4.367
print(type(distancia_a_AlfaCentauri))



## Fechas
#-----------------
from datetime import date
date.today()
print(date.today())



## Conversión de tipo de datos
#-----------------
from datetime import date
print("today's date is: " + str(date.today()))



## Entrada del usuario
#-----------------
print("Bienvenido al programa del módulo cero")
name = input("Introduzca su nombre: ")
print("Saludos: " + name)



## Trabajar con números
#-----------------
print("Calculadora")
first_number = input("Primer número: ")
secound_number = input("Segundo número: ")
print("Concatenación de números ", first_number + secound_number)

print("Suma de números ", int(first_number) + int(secound_number))

