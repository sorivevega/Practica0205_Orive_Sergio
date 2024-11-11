#Escribir una función que reciba un número entero positivo y devuelva su factorial. Realiza el ejercicio mediante bucles interactivos y mediante una función recursiva.
'Funcion recursiva'
import math
import statistics

def recursiva():
    number = int(input('Introduzca un numero: '))
    recursiv0 = (math.factorial(number))
    return recursiv0
print (recursiva())