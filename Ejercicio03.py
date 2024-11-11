#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
def area(number):
    '''Esta funcion calcula el area de un circulo

    Parametros:
        -radio = radio necesario para calcular el area
        -pi(3.1416) = constante
        -area = pi * radio^2
    Salida:
         Area del circulo
    '''
    pi = 3.1416
    Area = (pi * number ** 2)
    return (Area)
print(area(5))



def volumen(altura):
    '''Esta funcion calcula el volumen de un cilindro
    
    Parametros:
        -altura = altura necesaria para calcular el volumen
        -area = funcion anterior necesaria para calcular el volumen
        -volumen = area * altura

    Salida:
         Volumen del cilindro
    '''
    Volumen = float(area(5) * altura)
    return (Volumen)
print(volumen(2))