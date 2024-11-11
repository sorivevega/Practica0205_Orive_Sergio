#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus valores al cuadrado.
import statistics
def cuadrado():
    '''
    Esta funcion lo que va a hacer va a ser recibir unos valores con un (input)
    y esos valores pasaran a una lista.
    Despues esos Valores se devolveren elevados al cuadrado
    '''
    number = input('Introduzca numeros separados por comas: ')
    number = [float(num) for num in number.split(',')]
    '''
    Lo que acabo de hacer es para poder meter los numeros dentro de una lista
    '''
    number2 = [x ** 2 for x in number]
    '''
    Finalmente ya hacemos el cuadrado de los valores x para todos aquellos valores
    que esten dentro de la variable number
    '''
    return number2
print(cuadrado())