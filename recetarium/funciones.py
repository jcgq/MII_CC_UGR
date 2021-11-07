import json
from excepciones import *

	

def obtener_diccionario_alimentos():
	with open('../MII_CC_UGR/json/alimentos_es.json', 'r') as f:
		try:
			c = f.read()
		except FileNotFoundError:
			print("Error en la lectura del Json")

	datos_alimentos = json.loads(c)
	array_alimentos = []

	array_alimentos = [dato["nombre"] for dato in datos_alimentos]

	diccionario_alimentos = {"alimentos":array_alimentos}

	return diccionario_alimentos



def lanzar_excepcion(atributo, causa):
	try:
		raise MisExcepciones(atributo, causa)
	except MisExcepciones as e:
		print("El campo erróneo es " + e.campo)
		print("El error es " + e.informacion)

def lanzar_excepcion_alimento():
	try:
		raise MisExcepciones("Tiempo", "El tiempo está expresado en minutos. No te líes.")
	except MisExcepciones as e:
		print("Alimentos")
		print("El formato de los alimentos es incorrecto")

def lanzar_excepcion_tiempo():
	try:
		raise MisExcepciones("Tiempo", "El tiempo está expresado en minutos. No te líes.")
	except MisExcepciones as e:
		print("Tiempo")
		print("El formato de los minutos no es el adecuado")

obtener_diccionario_alimentos()