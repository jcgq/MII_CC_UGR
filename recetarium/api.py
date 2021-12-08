import requests
import bottle
import os
from bottle import get, post, run, route, response, error, request
import json
from funciones import *
from recetas import *
from urllib.parse import unquote
from configuracion import Configuracion
import logging

confg = Configuracion()
app = bottle.default_app()

logging.basicConfig(filename='fichero.log',
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filemode='w', level=logging.INFO)

#Página de inicio
@route('/')
def recetas_contador():
	logging.info("Estás en la página de inicio")
	response.status = 204
	return '{"Bienvenid@!" : "A mi API de Recetas"}'

@get('/recetas/<nombre>')
def receta(nombre):
	json_alimentos = obtener_json()
	diccionario = obtener_diccionario(json_alimentos)
	receta = diccionario.get(nombre.lower())

	if receta == None:
		logging.error('Error. No existe la receta en el sistema')
		response.status = 404
		return "{\"Error\":\"404 Receta no encontrada\"}"
	else:
		receta = json.dumps(receta, indent=4, sort_keys=True)
		logging.info('Éxito. La receta existe y se devuelve al usuario.')
		response.status=200
		return receta

@get('/recetas')
def recetas():
	json_alimentos = obtener_json()
	recetas = obtener_diccionario(json_alimentos)
	
	if len(recetas)==0:
		logging.error('Error. No existe ninguna receta en el sistema')
		response.status = 404
		return "{\"Error\":\"No existen recetas en el sistema\"}"
	else:
		logging.info('Éxito. La recetas se encuentran disponible en el sistema.')
		response.status = 200
		return recetas

if __name__ == "__main__":
    run(host=confg.host, port=confg.puerto, debug=False, reloader=True)