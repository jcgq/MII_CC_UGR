import sys
sys.path.insert(1, 'recetarium')
from recetas import Receta
from funciones import *
import unittest
class Test(unittest.TestCase):
    def test_alimentos(self):
        #Test erróneo. Los alimentos están vacíos o con longitud errónea
        alimento = ""
        assert(Receta.alimentos_incorrectos(alimento)==True)
        alimento = "1 pan"
        assert(Receta.alimentos_incorrectos(alimento)==True)

        #Test erróneo. Los alimentos tienen alimentos no permitidos
        alimento = "1 kilo de sanjacobos;100 gramos de aire"
        assert(Receta.alimentos_incorrectos(alimento)==True)

        #Test erróneo. Los alimentos tienen unidades no permitidas
        alimento = "1 cazuela de champiñones; 1 onza de chocolate"
        assert(Receta.alimentos_incorrectos(alimento)==True)

        #Test erróneo. No introduce valores numéricos
        alimento = "una cazuela de champiñones; una onza de chocolate"
        assert(Receta.alimentos_incorrectos(alimento)==True)

        #Test correcto. Los alimentos cumplen con los requisitos
        alimento = "1 kilo de champiñones;100 gramos de chocolate"
        assert(Receta.alimentos_incorrectos(alimento)==False) 

    def test_tiempo(self):
        #Test erróneo. El tiempo es incorrecto
        tiempo = "2u4"
        assert(Receta.tiempo_incorrecto(tiempo)==True)

        #Test erróneo. El tiempo es menor del permitido
        tiempo = "2"
        assert(Receta.tiempo_incorrecto(tiempo)==True)

        #Test erróneo. El tiempo es negativo
        tiempo = "-34"
        assert(Receta.tiempo_incorrecto(tiempo)==True)

        #Test correcto. El tiempo cumple con los requisitos
        tiempo = "78"
        assert(Receta.tiempo_incorrecto(tiempo)==False)


    def test_validacion_completa(self):
        #Test incorrecto. El nombre no es válido
        nombre = ""
        alimentos= "1 kilo de champiñones;100 gramos de chocolate"
        elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
        tiempo = "78"
        assert(Receta.receta_invalida(self, nombre, alimentos, elaboracion, tiempo)==True)
        
        #Test incorrecto. Los alimentos no son válidos
        nombre = "Huevo frito"
        alimentos= "un amor de champiñones;cien gramos de chocolate"
        elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
        tiempo = "78"
        assert(Receta.receta_invalida(self, nombre, alimentos, elaboracion, tiempo)==True)

        #Test incorrecto. La elaboración no es válida
        nombre = "Huevo Frito"
        alimentos= "un kilo de champiñones;cien gramos de chocolate"
        elaboracion = "Nada"
        tiempo = "78"
        assert(Receta.receta_invalida(self, nombre, alimentos, elaboracion, tiempo)==True)

        #Test incorrecto. El tiempo no es válido
        nombre = "Huevo Frito"
        alimentos= "1 kilo de champiñones;100 gramos de chocolate"
        elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
        tiempo = "hola"
        assert(Receta.receta_invalida(self, nombre, alimentos, elaboracion, tiempo)==True)
        
        #Test correcto. Se puede crear el objeto receta
        nombre = "Huevo frito"
        alimentos= "1 kilo de champiñones;100 gramos de chocolate"
        elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
        tiempo = "45"
        assert(Receta.receta_invalida(self, nombre, alimentos, elaboracion, tiempo)==False)


    def test_constructor(self):
        #Test incorrecto. El nombre no es válido
        nombre = "Huevo frito"
        alimentos= "1 kilo de champiñones;100 gramos de chocolate"
        elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
        tiempo = "23"
        receta = None
        try:
            receta = Receta(nombre, alimentos, elaboracion, tiempo)
        except:
            assert(receta == None)

        
        #Test incorrecto. Los alimentos no son válidos
        nombre = "Huevo frito"
        alimentos= "un pepino de champiñones;cien gramos de chocolate"
        elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
        tiempo = "23"
        receta = None
        try:
            receta = Receta(nombre, alimentos, elaboracion, tiempo)
        except:
            assert(receta == None)

        #Test incorrecto. La elaboración no es válida
        nombre = "Huevo frito"
        alimentos= "1 kilo de champiñones;100 gramos de chocolate"
        elaboracion = "Nada"
        tiempo = "23"
        receta = None
        try:
            receta = Receta(nombre, alimentos, elaboracion, tiempo)
        except:
            assert(receta == None)

        #Test incorrecto. El timepo no es válido
        nombre = "Huevo frito"
        alimentos= "1 kilo de champiñones;100 gramos de chocolate"
        elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
        tiempo = ""
        receta = None
        try:
            receta = Receta(nombre, alimentos, elaboracion, tiempo)
        except:
            assert(receta == None)

        #Test correcto. Se crea la receta
        nombre = "Huevo frito"
        alimentos= "1 kilo de champiñones;100 gramos de chocolate"
        elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
        tiempo = "23"
        receta = Receta(nombre, alimentos, elaboracion, tiempo)
        assert(receta.__class__ == Receta)


if __name__ == "__main__":
    unittest.main()