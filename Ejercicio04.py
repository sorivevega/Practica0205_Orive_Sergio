#Escribir una función que reciba una muestra de números en una lista y devuelva su media.
import statistics
def media():
    '''
    Esta funcion lo que va a hacer va a ser calcularnos
    la media de los valores que le metamos.
    Para ello hacemos un (input) donde nos digan los numeros
    '''
    number = input('Introduzca los numeros para la media separados por comas')
    number = [float(num) for num in number.split(',')]
    '''
    Lo que acabamos de hacer es que los valores del input
    no nos deja meterlos directamente en la lista por lo que
    debemos usar el comando (float) y despues separamos la lista
    por la ,.
    Por ultimo utilizamos (statistics) lo que nos da mas comandos
    y entre ellos encontramos el de media.
    '''
    print(statistics.median(number))
print (media())