import unittest


def es_mayor(edad):
    if edad >= 18:
        return True
    else:
        return False
 

class PruebaDeCristal(unittest.TestCase):
    
    def test_es_mayor(self):
        edad = 20

        resultado = es_mayor(edad)

        self.assertEqual(resultado, True)


    def test_es_menor(self):
        edad = 15

        resultado = es_mayor(edad)

        self.assertEqual(resultado,False)

        edad = 20

        resultado = es_mayor(edad)

        self.assertEqual(resultado, True)


    def test_es_menor(self):
        edad = 15

        resultado = es_mayor(edad)

if __name__ == '__main__':
    unittest.main(verbosity=2)