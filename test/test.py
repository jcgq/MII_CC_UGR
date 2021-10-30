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

def test_alimentos():
    diccionario_unidades = obtener_diccionario_unidades()
    diccionario_alimentos = obtener_diccionario_alimentos()

    #Test erróneo. Los alimentos están vacíos o con longitud errónea
    alimento = ""
    assert(alimentos_incorrectos(alimento, diccionario_unidades, diccionario_alimentos["alimentos"])==True)
    alimento = "un pan"
    assert(alimentos_incorrectos(alimento, diccionario_unidades, diccionario_alimentos["alimentos"])==True)

    #Test erróneo. Los alimentos tienen alimentos no permitidos
    alimento = "un kilo de sanjacobos;un gramo de aire"
    assert(alimentos_incorrectos(alimento, diccionario_unidades, diccionario_alimentos["alimentos"])==True)

    #Test erróneo. Los alimentos tienen unidades no permitidas
    alimento = "una cazuela de champiñones; una onza de chocolate"
    assert(alimentos_incorrectos(alimento, diccionario_unidades, diccionario_alimentos["alimentos"])==True)

    #Test correcto. Los alimentos cumplen con los requisitos
    alimento = "un kilo de champiñones; cien gramos de chocolate"
    assert(alimentos_incorrectos(alimento, diccionario_unidades, diccionario_alimentos["alimentos"])==False)

def test_elaboracion():
    #Test erróneo. La elaboracion está vacía
    elaboracion = ""
    assert(elaboracion_incorrecto(elaboracion)==True)

    #Test erróneo. La elaboracion tiene una longitud incorrecta
    elaboracion = "yew"
    assert(elaboracion_incorrecto(elaboracion)==True)

    #Test correcto. La elaboracion cumple con los requisitos
    elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
    assert(elaboracion_incorrecto(elaboracion)==False)
