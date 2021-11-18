import json
from excepciones import *
import re
from nltk.corpus import stopwords
import nltk
from string import punctuation
#Descargar las stopwords, necesario para la nueva funcionalidad
nltk.download('stopwords')

def obtener_diccionario_alimentos():
	with open('./json/alimentos_es.json', 'r') as f:
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

def comprobar_numero(numero):
	numero = numero.strip()
	reg_exp = "\d+$"
	resultado = re.match(reg_exp, numero)
	return resultado


palabras_a_eliminar = stopwords.words('spanish')
signos_puntuacion = list(punctuation)
def limpieza_texto(texto_inicial):
		texto_final = ""
		for palabra in texto_inicial.split():
			if not palabra in palabras_a_eliminar or palabra in signos_puntuacion:
				texto_final += palabra + ""
		return texto_final

def eliminar_signos_puntuacion(texto_inicial):
	for palabra in signos_puntuacion:
		texto_inicial = texto_inicial.replace(palabra, '')
	return texto_inicial

def procesar_elaboracion(elaboracion_receta):
	elaboracion_receta = elaboracion_receta.lower()
	elaboracion_receta = limpieza_texto(elaboracion_receta)
	elaboracion_receta = eliminar_signos_puntuacion(elaboracion_receta)
	return elaboracion_receta

def obtener_puntuacion(puntuacion, matriz_pesos):
	aux = matriz_pesos[0]
	apta = True
	for i in range(1, len(aux)):
		if aux[i]>=puntuacion:
			print(aux[i], puntuacion)
			apta = False
	return apta