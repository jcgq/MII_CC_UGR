from bottle import response
import sys
sys.path.insert(1, 'recetarium')
from excepciones import MisExcepciones
from funciones import *
import webtest
from webtest import TestApp
import bottle
import sys
import json
import unittest
from urllib.parse import quote


import api as ap
app = bottle.default_app()

class TestApi(unittest.TestCase):

    def test_lista_recetas(self):
        test_app = TestApp(app)
        recetas = test_app.get('/recetas')

        assert recetas.status == "200 OK"


    def test_receta(self):
        test_app = TestApp(app)

        #Test con status Correcto
        resp = test_app.get('/recetas/arroz negro')
        assert(resp.status == "200 OK")

        #Test con status Incorrecto
        with self.assertRaises(webtest.app.AppError):
            resp = test_app.post('/recetas/pollo al romero')
            assert(resp.status == "404 Error")

    def test_aniadir_receta(self):
        #Test Incorrecto. El nombre de la receta ya existe
        test_app = TestApp(app)
        nombre = "tarta de queso"
        ingredientes = "1 kilo de verduras;100 gramos de chocolate"
        elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
        tiempo = "120"
        #Test con status Incorrecto
        with self.assertRaises(webtest.app.AppError):
            resp = test_app.post('/receta', {'nombre': nombre, 'elaboracion':elaboracion, 'alimentos': ingredientes, 'tiempo':tiempo})
            assert(resp.status == "404 Error")

        #Test Incorrecto. Los ingredientes no están en la base de datos
        test_app = TestApp(app)
        nombre = "Salmorejo"
        ingredientes = "1 kilo de almendras;100 gramos de chocolate"
        elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
        tiempo = "120"
        #Test con status Incorrecto
        with self.assertRaises(webtest.app.AppError):
            resp = test_app.post('/receta', {'nombre': nombre, 'elaboracion':elaboracion, 'alimentos': ingredientes, 'tiempo':tiempo})
            assert(resp.status == "404 Error")

        #Test Incorrecto. La elaboración está repetida
        test_app = TestApp(app)
        nombre = "Salmorejo"
        ingredientes = "1 kilo de almendras;100 gramos de chocolate"
        elaboracion = "mucho esemero y paciencia"
        tiempo = "120"
        #Test con status Incorrecto
        with self.assertRaises(webtest.app.AppError):
            resp = test_app.post('/receta', {'nombre': nombre, 'elaboracion':elaboracion, 'alimentos': ingredientes, 'tiempo':tiempo})
            assert(resp.status == "404 Error")

        #Test Incorrecto. No es un tiempo adecuado
        test_app = TestApp(app)
        nombre = "Salmorejo"
        ingredientes = "1 kilo de almendras;100 gramos de chocolate"
        elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
        tiempo = "hola"
        #Test con status Incorrecto
        with self.assertRaises(webtest.app.AppError):
            resp = test_app.post('/receta', {'nombre': nombre, 'elaboracion':elaboracion, 'alimentos': ingredientes, 'tiempo':tiempo})
            assert(resp.status == "404 Error")

        #Test correcto. La receta se puede añadir al sistema
        test_app = TestApp(app)
        nombre = "Salmorejo"
        ingredientes = "1 kilo de verduras;100 gramos de chocolate"
        elaboracion = "Hay que remover todo con la espátula y que el aceite esté bien caliente"
        tiempo = "120"

        resp = test_app.post('/receta', {'nombre': nombre, 'elaboracion':elaboracion, 'alimentos': ingredientes, 'tiempo':tiempo})
        assert(resp.status == "201 Created")

    def test_recomendar_recetas(self):
        
        #Test erróneo. No hay recetas que mostrar
        test_app = TestApp(app)
        nombre = quote("tarta de limón")
        ingredientes = quote("queso, arroz")
        calorias = "10"

        with self.assertRaises(webtest.app.AppError):
            resp = test_app.post('/recomendacion', {'receta': nombre, 'ingredientes': ingredientes, 'calorias':calorias})
            assert(resp.status == "404 Error")

        #Test correcto. Se muestran las recetas recomendadas
        test_app = TestApp(app)
        nombre = quote("arroz negro")
        ingredientes = quote("arroz")
        calorias = "1800"

        resp = test_app.post('/recomendacion', {'receta': nombre, 'ingredientes': ingredientes, 'calorias':calorias})
        assert(resp.status == "200 OK")

if __name__ == "__main__":
    TestApi.main()