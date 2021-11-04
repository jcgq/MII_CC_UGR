import json
import re
from excepciones import *
from sklearn.feature_extraction.text import TfidfVectorizer
from string import punctuation
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer



def obtener_diccionario_alimentos():
    with open('../MII_CC_UGR/json/alimentos_es.json', 'r') as f:
        try:
            c = f.read()
        except FileNotFoundError:
            print("Error en la lectura del Json")

    datos_alimentos = json.loads(c)
    conjunto_alimentos = []
    for i in range(0, len(datos_alimentos)):
        conjunto_alimentos.append(datos_alimentos[i]["nombre"])

    diccionario_alimentos = {"alimentos":conjunto_alimentos}

    return diccionario_alimentos


def obtener_diccionario_unidades():
	with open('../MII_CC_UGR/ficheros/unidades_medida.txt', 'r') as f:
		try:
			c = f.read()
		except ValueError:
			print("Error en la lectura del Json")

	diccionario_unidades = c.split("\n")

	return diccionario_unidades

def nombre_incorrecto(nombre):
	if(nombre == "" or len(nombre)<3 or nombre == None):
		return True
	else:
		return False

def alimentos_incorrectos(alimentos, unidades_permitidas, diccionario_alimentos):
	incorrecto=False
	if(len(alimentos)>10):
		alimentos = alimentos.split(";")
		for i in range(0, len(alimentos)):
			if not any(alimento in alimentos[i] for alimento in diccionario_alimentos):
				incorrecto = True
			if not any(unidad in alimentos[i] for unidad in unidades_permitidas):
				incorrecto = True
	else:
		incorrecto = True
	return incorrecto

def elaboracion_incorrecto(elaboracion):
		if(elaboracion == "" or len(elaboracion)<20):
			return True
		else:
			return False

def tiempo_incorrecto(tiempo_empleado):
	if not tiempo_empleado:
		return True
	else:
		if(type(tiempo_empleado) == type(1)):
			if tiempo_empleado < 5:
				return True
			else:
				return False
		if(type(tiempo_empleado) == type("1")):
			reg_exp = "[-+]?\d+$"
			aux = re.match(reg_exp, tiempo_empleado)
			if(aux):
				return False
			else:
				return True

def validar_caracteristicas_receta(nombre, alimentos, unidades_permitidas, diccionario_alimentos, elaboracion, tiempo_empleado):
	nombre_c = nombre_incorrecto(nombre)
	alimento_c = alimentos_incorrectos(alimentos, unidades_permitidas, diccionario_alimentos)
	elaboracion_c = elaboracion_incorrecto(elaboracion)
	tiempo_c = tiempo_incorrecto(tiempo_empleado)

	if(nombre_c or alimento_c or elaboracion_c or tiempo_c):
		lanzar_excepcion(nombre_c, alimento_c, elaboracion_c, tiempo_c)
		return True
	else:
		return False


def lanzar_excepcion(nombre_c, alimento_c, elaboracion_c, tiempo_c):
	if(nombre_c):
		try:
			raise MisExcepciones("Nombre", "No se ha escrito correctamente. Recuerda que tiene que tener una longitud mayor a 3")
		except MisExcepciones as e:
			print("El campo erróneo es " + e.campo)
			print("El error es " + e.informacion)
	if(alimento_c):
		try:
			raise MisExcepciones("Alimentos", "Recuerda que el formato es: (cantidad) (unidad) de (alimento) -> un kilo de patatas")
		except MisExcepciones as e:
			print("El campo erróneo es " + e.campo)
			print("El error es " + e.informacion)
	if(elaboracion_c):
		try:
			raise MisExcepciones("Elaboración", "No se ha escrito correctamente")
		except MisExcepciones as e:
			print("El campo erróneo es " + e.campo)
			print("El error es " + e.informacion)
	if(tiempo_c):
		try:
			raise MisExcepciones("Tiempo", "El tiempo está expresado en minutos. No te líes.")
		except MisExcepciones as e:
			print("El campo erróneo es " + e.campo)
			print("El error es " + e.informacion)
