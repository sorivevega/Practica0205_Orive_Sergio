#Escribir una función que reciba un número entero positivo y devuelva su factorial. Realiza el ejercicio mediante bucles interactivos y mediante una función recursiva.
'Bucles iterativos'
def iterativo():
    number = int(input('Introduce un numero: '))
    iterativ0 = 1
    while number > 1:
       iterativ0 *= number
       number -= 1
    return iterativ0
    print(iterativ0)
print(iterativo())
        
