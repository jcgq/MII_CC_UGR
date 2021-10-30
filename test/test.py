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

def test_tiempo():
    #Test erróneo. El tiempo está vacío
    tiempo = ""
    assert(tiempo_incorrecto(tiempo)==True)

    #Test erróneo. El tiempo es incorrecto
    tiempo = "2u4"
    assert(tiempo_incorrecto(tiempo)==True)

    #Test correcto. El tiempo cumple con los requisitos
    tiempo = "78"
    assert(tiempo_incorrecto(tiempo)==False)

    #Test correcto. El tiempo cumple con los requisitos
    tiempo = 78
    assert(tiempo_incorrecto(tiempo)==False)


def test_validacion_completa():
    diccionario_unidades = obtener_diccionario_unidades()
    diccionario_alimentos = obtener_diccionario_alimentos()

    #Test incorrecto. El nombre no es válido
    nombre = ""
    alimentos= "un kilo de champiñones; cien gramos de chocolate"
    elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
    tiempo = 78
    assert(validar_caracteristicas_receta(nombre, alimentos, diccionario_unidades, diccionario_alimentos["alimentos"], elaboracion, tiempo)==True)
    
    #Test incorrecto. Los alimentos no son válidos
    nombre = "Huevo frito"
    alimentos= "un amor de champiñones; cien gramos de chocolate"
    elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
    tiempo = 78
    assert(validar_caracteristicas_receta(nombre, alimentos, diccionario_unidades, diccionario_alimentos["alimentos"], elaboracion, tiempo)==True)

    #Test incorrecto. La elaboración no es válida
    nombre = ""
    alimentos= "un kilo de champiñones; cien gramos de chocolate"
    elaboracion = "Nada"
    tiempo = 78
    assert(validar_caracteristicas_receta(nombre, alimentos, diccionario_unidades, diccionario_alimentos["alimentos"], elaboracion, tiempo)==True)

    #Test incorrecto. El tiempo no es válido
    nombre = ""
    alimentos= "un kilo de champiñones; cien gramos de chocolate"
    elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
    tiempo = "hola"
    assert(validar_caracteristicas_receta(nombre, alimentos, diccionario_unidades, diccionario_alimentos["alimentos"], elaboracion, tiempo)==True)

    #Test correcto. Se puede crear el objeto receta
    nombre = "Huevo frito"
    alimentos= "un kilo de champiñones; cien gramos de chocolate"
    elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
    tiempo = 45
    assert(validar_caracteristicas_receta(nombre, alimentos, diccionario_unidades, diccionario_alimentos["alimentos"], elaboracion, tiempo)==False)
