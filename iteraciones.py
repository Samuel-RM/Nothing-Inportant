contador = 0 
contador2 = 0

while contador < 5:
    while contador2 < 6: 
        print(contador, contador2)
        contador2 += 1

        if contador2 >= 3:
            break    
    contador += 1
    contador2 = 0 