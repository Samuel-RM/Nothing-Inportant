def logica(nombre_1, edad_1, nombre_2, edad_2):
    if edad_1 > edad_2:
        print(f'AHH , entonces {nombre_1} es mayor que {nombre_2} ')
    elif edad_1 < edad_2:
        print(f'AHH entonces, {nombre_1} es menor que {nombre_2}')
    else:
        print('AHHH , entonce tienen la misma edad , con razon! ')
    

def run():
    print('Bienvenido al comparador de edades, porfavor ingrese nombres y edades de las 2 personas a comparar')
    nombre_1 = input('Hola, cual es la nombre del de la primera persona? ')
    edad_1 = int(input(f'Cual es la edad de {nombre_1}?: '))
    nombre_2 = input('Bueno y cual es el nombre de  la segunda persona?: ')
    edad_2 = int(input(f'Cual es la edad de {nombre_2}?: '))
    logica(nombre_1, edad_1, nombre_2, edad_2)

if __name__ == '__main__':
    run()