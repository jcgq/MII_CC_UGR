import requests
import bottle
import os
from bottle import get, post, run, route, response, error, request
import json
from funciones import *
from recetas import *

import logging

logging.basicConfig(filename='fichero.log',
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filemode='w', level=logging.INFO)

logging.info('Prueba de logging basica')
logging.debug('Esta linea no saldra')
logging.warning('Este programa no ha hecho nada')

app = bottle.default_app()



@route('/recetas/contador')
def recetas_contador():
	return "H"

@route('/test')
def test():
	logging.info("Test pasados con éxito")
	os.system("pytest test/test.py")

@get('/recetas/<nombre>', method='GET')
def receta(nombre):
	
	datos_alimentos = obtener_json()
	diccionario = obtener_diccionario(datos_alimentos)
	
	receta = diccionario.get(nombre.lower())

	if receta == None:
		logging.error('Error. No existe la receta')
		response.status = 404
		return "{\"Error\":\"404 Receta no encontrada\"}"
	else:
		receta = json.dumps(receta, indent=4, sort_keys=True)
		logging.info('Éxito. La receta existe.')
		response.status=200
		return receta


@get('/recetas', method='GET')
def recetas():
	datos_alimentos = obtener_json()
	diccionario = {}

	for i in range(0, len(datos_alimentos)):
		nom = datos_alimentos[i]["nombre"]
		ali = datos_alimentos[i]["alimentos"]
		ela = datos_alimentos[i]["elaboracion"]
		tim = datos_alimentos[i]["tiempo"]
		cal = datos_alimentos[i]["calorias"]
		diccionario[nom] = {"nombre":nom, "alimento":ali, "elaboracion":ela, "tiempo":tim, "calorias":cal}

	recetas = json.dumps(diccionario, indent=4, sort_keys=True)
	
	if recetas == None:
		logging.error('Error. No existe ninguna receta en el sistema')
		response.status = 400
		return "{\"Error\":\"404 Receta no encontrada\"}"
	else:
		logging.info('Éxito. La recetas se encuentran disponible en el sistema.')
		return recetas

@post('/receta', methods=['POST'])
def crear_receta():
	nombre = request.forms.get('nombre')
	elaboracion = request.forms.get('elaboracion')
	alimentos = request.forms.get('alimentos')
	tiempo = request.forms.get('tiempo')

	try:
		receta = Receta(nombre, alimentos, elaboracion, tiempo)
	except Exception as error:
		response.status = 404
		logging.error('Receta incorrecta')
		return "Error"

	aniadir_receta_json(receta)
	
	return '{"Éxito!" : "Receta añadida al sistema"}'

if __name__ == "__main__":
    run(host="127.0.0.1", port=8000, debug=False, reloader=True)