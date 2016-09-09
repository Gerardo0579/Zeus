import unittest
from DAO.GestorFichero import GestorFichero

class TestStringMethods(unittest.TestCase):

    def test_getAsignaturas(self):
        gestor = GestorFichero()
        resultado = 0
        asignaturas = gestor.getAsignaturas()
        if asignaturas[0] == "Física":
            if asignaturas[1] == "Matemáticas":
                resultado = 1
        self.assertEqual(1, resultado)

    def test_getSemestres(self):
        gestor = GestorFichero()
        resultado = 0
        semestres = gestor.getSemestresAsignatura("Física")
        if semestres[0] == "1.csv":
            if semestres[1] == "3.csv":
                resultado = 1
        self.assertEqual(1, resultado)

    def test_getBloques(self):
        gestor = GestorFichero()
        resultado = 0
        semestres = gestor.getBloquesAsignatura("Física","1")
        lista = ["Bloque 1","Bloque 2","Bloque 3","Bloque 4",]
        self.assertEqual(lista, semestres)

if __name__ == '__main__':
    unittest.main()
