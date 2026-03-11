import unittest
from src.funciones import cantidad_perdidas

class TestCantidadPerdidas(unittest.TestCase):  # ← clase obligatoria

    def test_sin_perdidas(self):                # ← self en cada método
        notas = [3.0, 4.0, 5.0]
        self.assertEqual(cantidad_perdidas(notas), 0)

    def test_con_perdidas(self):
        notas = [2.5, 4.0, 1.0, 3.5]
        self.assertEqual(cantidad_perdidas(notas), 2)

    def test_todas_perdidas(self):
        notas = [1.0, 2.0, 2.9]
        self.assertEqual(cantidad_perdidas(notas), 3)

    def test_lista_vacia(self):
        notas = []
        self.assertEqual(cantidad_perdidas(notas), 0)

if __name__ == '__main__':
    unittest.main()