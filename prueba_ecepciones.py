def buscador_capitales(paises, llave):
    try:
        return print(f'Tenemos tickets disponibles para {paises[llave]}')
    except KeyError as e:
        return print(f'\nEl pais que buscas no se encuentra en la base de datos , tipo de error {e}')


llave =  input('\n Bienvenidos , para que pais desea comprar el ticket de avion?: ')

paises = {   
        'Colombia': 'Bogota',
        'Uruguay': 'Montevideo',
        'España': 'Madrid',
        'Canada': 'Ottawa',
        'Argentina': 'Buenos Aires',
        'Australia': 'Canberra',
        'Bolivia': 'Sucre',
        'Brasil': 'Brasilia',
        'Chile': 'Santiago',
        'Venezuela': 'Caracas',
        'Costa Rica': 'San Jose',
        'Cuba': 'La Habana',
        'Ecuador': 'Quito',
        'Egipto': 'El Cairo',
        'Francia': 'Paris',
        'Filipinas': 'Manilla',
        'India': 'Nueva Delhi',
        'Indonesia': 'Yakarta',
        'Italia': 'Roma',
        'Libano': 'Beirut',
        }


if __name__ == '__main__':
    buscador_capitales(paises, llave)
