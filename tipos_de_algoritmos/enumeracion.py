import time

objetivo = int(input('Escoje un entero: '))
respuesta = 0 

tiempo_= time.titiempo_= time.time()

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene raiz exacta')

print(f'El programa demoro {time.time() - tiempo_} segundos ')