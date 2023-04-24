# Clase 14 , Tipo de algoritmo: Busqueda Binaria./Metodo de Biseccion
# Tipo de algoritmo en la categoria de Metodos Numericos, 
# Con este algoritmo , hacemos la funcion que los anteriores pero con este algoritmo mucho mas eficiente
# basicamente le introducimos un numero y buscamos las mitad de ese numero y si la mitad de ese numero
# es mayor o menor al numero introducido cortamos la mitad que no vamos a ocaltoar ya  
objetivo = int(input('Give me a number: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo) 
respuesta = (bajo + alto) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(respuesta)
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto + bajo) / 2
print(f'The square root of {objetivo} is {respuesta}')
