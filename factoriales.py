def factortial (n):
    """Calcula el fctorial de n
s
    n int > 0 
    return n!
    """
    print(n)
    if n == 1:
        return 1
    
    return n * factortial(n - 1)

n = int(input('Escribe un entero: '))

print(factortial(n))