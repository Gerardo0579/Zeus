import unittest
from Fachada.Asignatura import Asignatura

class TestStringMethods(unittest.TestCase):

    def test_setAsignaturaExitoso(self):
        asignatura = Asignatura()
        resultado = asignatura.setAsignatura("perro")
        self.assertEqual(1, resultado)

    def test_setAsignaturaVacio(self):
        asignatura = Asignatura()
        resultado = asignatura.setAsignatura("")
        self.assertEqual(0, resultado)

    def test_setAsignaturaNumero(self):
        asignatura = Asignatura()
        resultado = asignatura.setAsignatura("2")
        self.assertEqual(0, resultado)

    def test_setBloqueExitoso(self):
        asignatura = Asignatura()
        resultado = asignatura.setBloque("2")
        self.assertEqual(1, resultado)

    def test_setBloqueVacio(self):
        asignatura = Asignatura()
        resultado = asignatura.setBloque("")
        self.assertEqual(0, resultado)

    def test_setBloqueLetra(self):
        asignatura = Asignatura()
        resultado = asignatura.setBloque("A")
        self.assertEqual(0, resultado)

    def test_setBloqueCadena(self):
        asignatura = Asignatura()
        resultado = asignatura.setBloque("ABC")
        self.assertEqual(0, resultado)



    def test_setSemestreExitoso(self):
        asignatura = Asignatura()
        resultado = asignatura.setSemestre("2")
        self.assertEqual(1, resultado)

    def test_setSemestreVacio(self):
        asignatura = Asignatura()
        resultado = asignatura.setSemestre("")
        self.assertEqual(0, resultado)

    def test_setSemestreLetra(self):
        asignatura = Asignatura()
        resultado = asignatura.setSemestre("A")
        self.assertEqual(0, resultado)

    def test_setSemestreCadena(self):
        asignatura = Asignatura()
        resultado = asignatura.setSemestre("ABC")
        self.assertEqual(0, resultado)



if __name__ == '__main__':
    unittest.main()
