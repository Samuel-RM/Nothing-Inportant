# Clase 25, e nos ensena como usar la metologia de testing "Black box" o "Caja Negra"
import unittest 

# Esta es la funcion en la que se pondra a aprueba si cumple con lo que se espera que sea el 
# uotput
def suma(num_1, num_2):
    return abs(num_1) + num_2

class CAjaNegraTest(unittest.TestCase):
# Probamos si la funcion funciona sumando 2 positivos
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5 

        resultado = suma (num_1,num_2)

        self.assertEqual(resultado, 15)
        
# probamos si la funcion funciona SUMANDO, dos negativos
    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7
        
        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

if __name__ == '__main__':
    unittest.main()
# ESte tipo de testing solo verifica si el input introducido coincide con el output
# que nos da la funcion a testear, no se nesecita saber cual es la logica de la funcion .