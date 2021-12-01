import json
from excepciones import *
import re
import nltk
from nltk.corpus import stopwords
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

#Descargar las stopwords, necesario para la nueva funcionalidad
nltk.download('stopwords')

def leer_json_alimentos():
	with open('json/alimentos_es.json', 'r') as f:
		try:
			c = f.read()
		except FileNotFoundError:
			print("Error en la lectura del Json")

	datos_alimentos = json.loads(c)
	return datos_alimentos

def obtener_diccionario_alimentos():
	datos_alimentos = leer_json_alimentos()
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

def tf_idf(conj_recetas):
	vector = TfidfVectorizer ()
	X = vector.fit_transform(conj_recetas)
	matriz_pesos = cosine_similarity(X,X)
	return matriz_pesos

def pasar_a_gramos(peso, unidad, alimento):
	dic_alimentos = leer_json_alimentos()
	gramos_finales = 0
	calorias = 0
	for i in range(0, len(dic_alimentos)):
		if(dic_alimentos[i]["nombre"] == alimento):
			calorias = int(dic_alimentos[i]["nutrientes"]["ENERC_KCAL"])

	if(unidad == "gr" or unidad == "gramos"):
		gramos_finales = (int(peso)*calorias)/100
	else:
		if(unidad == "litro" or unidad == "litros" or unidad == "kg" or unidad == "kilos" or unidad == "kilo"):
			gramos_finales = (int(peso)*1000*calorias)/100
		else:
			gramos_finales = (int(peso)*12*calorias)/100
	return gramos_finales

def obtener_dataframe(alimentos):
	df = pd.read_json (r'json/recetas.json')
	array_aux = []
	corr_ali_cal = []
	contiene = []
	ids = []
	for i in range(0, len(df)):
		aux_alimentos = df["alimentos"][i].split(";")
		array_aux.append(len(aux_alimentos))
		corr_ali_cal.append(df["calorias"][i] / len(aux_alimentos))
		ids.append(i)
		aux = (df["alimentos"][i].replace(";", " ")).split(" ")
		contador = 0
		for i in range(0, len(alimentos)):
			if aux.__contains__(alimentos[i]):
				contador = contador +1
		contiene.append(contador)
		contador=0

	df = df.assign(num_alimentos = array_aux)
	df = df.assign(calorias_alimentos = corr_ali_cal)
	df = df.assign(id = ids)
	df = df.assign(contiene_alimento = contiene)
	return df

def obtener_json():
	with open('json/recetas.json', 'r') as f:
		try:
			c = f.read()
		except FileNotFoundError:
			response.status = 400
			return "{'Error':'404 Fichero no encontrado'}"
	return json.loads(c)

def obtener_diccionario(datos_alimentos):
	diccionario = {}
	
	for i in range(0, len(datos_alimentos)):
		nom = datos_alimentos[i]["nombre"]
		ali = datos_alimentos[i]["alimentos"]
		ela = datos_alimentos[i]["elaboracion"]
		tim = datos_alimentos[i]["tiempo"]
		cal = datos_alimentos[i]["calorias"]
		diccionario[nom] = {"nombre":nom, "alimento":ali, "elaboracion":ela, "tiempo":tim, "calorias":cal}

	return diccionario

def aniadir_receta_json(receta):
			#Definición de la estructura del JSON
	datos = {
		'nombre':receta.nombre_receta,
		'alimentos':receta.alimentos,
		'elaboracion':receta.elaboracion,
		'tiempo':receta.tiempo,
		'calorias':receta.calorias
	}

	cadena_json = json.dumps(datos)

	#Lectura
	with open('json/recetas.json', 'r') as f:
		c = f.read()

	datosMod = json.dumps(datos)
	s = json.loads(c)
	s.append(datos)
	sC = json.dumps(s, indent=4)

	#Escritura
	with open('json/recetas.json', 'w') as f:
		f.write(sC)
		f.close()