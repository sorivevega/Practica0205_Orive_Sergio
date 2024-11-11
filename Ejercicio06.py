#Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
def binario():
    '''
    Esta funcion lo que va a hacer va a ser traducir los numeros que reciba 
    gracias al (input) a binario
    '''
    number = int(input('introduzca un numero: '))
    number2 = bin(number)
    '''
    Buscando en internet he encontrado esta funcion (bin()),  la cual lo que hace es
    convertir directamente los numeros a binario
    '''
    return number2
print(binario())


def decimal():
    '''
    Esta funcion lo que va a hacer va a ser traducir el valor en binario que 
    reciba mediante el (input) a decimal
    '''
    bin = str(input('introduzca el valor binario: '))
    bin2 = int(bin, 2)
    return bin2
print(decimal())