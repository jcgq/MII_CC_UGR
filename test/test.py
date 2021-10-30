import sys
sys.path.insert(1, 'src')
from recetas import Receta
from funciones import *


def test_nombre():
    #Test erróneo. El nombre está vacío
    nombre = ""
    assert(nombre_incorrecto(nombre)==True)

    #Test erróneo. El nombre tiene una longitud incorrecta
    nombre = "yu"
    assert(nombre_incorrecto(nombre)==True)

    #Test correcto. El nombre cumple con los requisitos
    nombre = "huevo frito"
    assert(nombre_incorrecto(nombre)==False)