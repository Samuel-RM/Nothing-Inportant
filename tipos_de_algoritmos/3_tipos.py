# reto dejado en la clase 16
def enumeracion(objetivo):
    respuesta = 0 

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz exacta')


def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def busqueda(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo) 
    respuesta = (bajo + alto) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
    
        respuesta = (alto + bajo) / 2
    print(f'\nLa raiz cuadrada de {objetivo} es {respuesta}')


def run():
    menu = int(input('''\n   Bienvenido, he hecho 3 diferentes tipos de algoritmos que nos ayudaran  
    a encontrar la raiz cuadrada de un numero, los tipos de algoritmo son:
    
    -1 Enumeracion Exaustiva
    -2 Aproximacion Exaustiva
    -3 Busqueda Binaria
    
    Elige un metodo para poder avanzar: '''))
    numero = int(input('\nOkey, una ves elegido el tipo de algoritmo que usaremos, ahora elige \n el numero al cual deseas encontrar la raiz cuadrada: ')) 
    
    if menu == 1:
        enumeracion(numero)
    elif menu == 2:
        aproximacion(numero)
    elif menu == 3:
        busqueda(numero)
    else:
        print('Porfavor elige una de opcion disponible(1 , 2 ,3)')
 

if __name__ == '__main__':
    run()