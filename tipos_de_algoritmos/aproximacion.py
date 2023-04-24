# Tipo de algoritmo: Aproximacion exaustiva , basicamente en ete programa pediremos
# un numero y trataremos de hacercarnos a los parecido de su potencia,{?xd}
# Curso 13 de Pensamiento COmputacional 
objetivo = int(input('Escribe un numero: ')) 
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

# aqui lo que hacemos es restar la variable nuestro numero aproximado contra nuestro numero
# establecido (nuestro input) dentro de una funcion que definimos como abs
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')