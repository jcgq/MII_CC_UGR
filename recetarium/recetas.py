from funciones import *
import re
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Receta:

	diccionario_unidades = {"unidades":["litro", "litros", "kg", "kilos", "kilo", 
	"kg", "gramos", "gr", "cucharada", "cucharadas", "cucharadita", 
	"cucharaditas", "ralladura", "ralladuras", "diente", "dientes"]}

	diccionario_alimentos = obtener_diccionario_alimentos()

	longitud_min_nombre = 3
	longitud_min_alimentos = 10
	longitud_min_elaboracion = 20
	palabras_a_eliminar = stopwords.words('spanish')
	signos_puntuacion = list(punctuation)

	def __init__(self, nombre_receta, alimentos, elaboracion, tiempo):
		if not self.receta_invalida(nombre_receta, alimentos, elaboracion, tiempo):
				self.nombre_receta = nombre_receta
				self.alimentos = alimentos
				self.elaboracion = elaboracion
				self.tiempo = tiempo
		else:
			raise MisExcepciones("Receta", "Los atributos de la receta tienen errores")

	def longitudes_incorrectas(nombre_receta, alimentos,  elaboracion, tiempo):
		if(len(nombre_receta)<Receta.longitud_min_nombre 
		or len(alimentos) < Receta.longitud_min_alimentos or 
		len(elaboracion) < Receta.longitud_min_elaboracion):
			lanzar_excepcion("Tamaño", "Se ha introducido un valor de longitud eróneo")
			return True
		else:
			return False

	def alimentos_incorrectos(alimentos):
		alimentos = alimentos.split(";")
		for i in range(0, len(alimentos)):
			if not any(alimento in alimentos[i] for alimento in Receta.diccionario_alimentos["alimentos"]):
				print(alimentos)
				lanzar_excepcion_alimento()
				return True
			if not any(unidad in alimentos[i] for unidad in Receta.diccionario_unidades["unidades"]):
				lanzar_excepcion_alimento()
				return True
			if not comprobar_numero(alimentos[i][0]):
				lanzar_excepcion_alimento()
				return True
		return False

	def tiempo_incorrecto(tiempo_empleado):
		aux = comprobar_numero(tiempo_empleado)
		if(aux):
			aux_numero = int(tiempo_empleado)
			if(aux_numero<5):
				return True
			else:
				return False
		else:
			return True

	#Funcion que valida que las unidades de medida, los alimentos y las cantidades sean correctas
	def receta_invalida(self,nombre, alimentos, elaboracion, tiempo):
		if(Receta.longitudes_incorrectas(nombre, alimentos, elaboracion, tiempo) or
		Receta.tiempo_incorrecto(tiempo) or
		Receta.alimentos_incorrectos(alimentos)):
			lanzar_excepcion("Receta", "La receta no es valida")
			return True
		else:
			return False

	def limpieza_texto(texto_inicial):
		texto_final = ""
		for palabra in texto_inicial.split():
			if not palabra in Receta.palabras_a_eliminar or palabra in Receta.signos_puntuacion:
				texto_final += palabra + ""
		return texto_final

	def eliminar_signos_puntuacion(texto_inicial):
		for palabra in Receta.signos_puntuacion:
			texto_inicial = texto_inicial.replace(palabra, '')
		return texto_inicial

	def procesar_elaboracion(elaboracion_receta):
		elaboracion_receta = elaboracion_receta.lower()
		elaboracion_receta = Receta.limpieza_texto(elaboracion_receta)
		elaboracion_receta = Receta.eliminar_signos_puntuacion(elaboracion_receta)
		return elaboracion_receta

	def tf_idf(conj_recetas):
		vector = TfidfVectorizer ()
		X = vector.fit_transform(conj_recetas)
		matriz_pesos = cosine_similarity(X,X)
		return matriz_pesos

	def obtener_puntuacion(matriz_pesos):
		aux = matriz_pesos[0]
		apta = True
		for i in range(1, len(aux)):
			if aux[i]>=0.8:
				apta = False
		return apta