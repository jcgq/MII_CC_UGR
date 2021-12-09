import logging
from funciones import *
import re
import pandas as pd
from bottle import response
from configuracion import *

confg = Configuracion()
class Receta:

	diccionario_unidades = {"unidades":["litro", "litros", "kg", "kilos", "kilo", 
	"kg", "gramos", "gr", "cucharada", "cucharadas", "cucharadita", 
	"cucharaditas", "ralladura", "ralladuras", "diente", "dientes"]}

	diccionario_alimentos = obtener_diccionario_alimentos()

	longitud_min_nombre = 3
	longitud_min_alimentos = 10
	longitud_min_elaboracion = 20

	def __init__(self, nombre_receta, alimentos, elaboracion, tiempo):
		if not self.receta_invalida(nombre_receta, alimentos, elaboracion, tiempo) and Receta.obtener_puntuacion(0.7,Receta.obtener_recetas(elaboracion)):	
			self.nombre_receta = nombre_receta
			self.alimentos = alimentos
			self.elaboracion = elaboracion
			self.tiempo = tiempo
			self.calorias = Receta.calcular_calorias(alimentos)
		else:
			response.status = 404
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
		Receta.alimentos_incorrectos(alimentos) or nombre_no_unico(nombre)):
			print("Error por que la longitud o formato es incorrecto")
			lanzar_excepcion("Receta", "La receta no es valida")
			return True
		else:
			return False

	def obtener_recetas(elaboracion):
		with open(confg.ruta_recetas, 'r') as f:
			try:
				c = f.read()
			except FileNotFoundError:
				logging.error("Error en la lectura del Json")
		datos_recetas = json.loads(c)
		elaboraciones = [dato["elaboracion"] for dato in datos_recetas]
		elaboraciones.insert(0, elaboracion)
		return elaboraciones

	def obtener_puntuacion(puntuacion, conjunto_elaboracion):
		matriz_pesos = tf_idf(conjunto_elaboracion)
		aux = matriz_pesos[0]
		apta = True
		for i in range(1, len(aux)):
			if aux[i]>=puntuacion:
				apta = False
				print("Error en la similitud")
		return apta

	def calcular_calorias(alimentos):
		alimentos = alimentos.split(";")
		gramos = 0
		for i in range(0,len(alimentos)):
			aux = alimentos[i].split(" ")
			gramos += pasar_a_gramos(aux[0], aux[1], aux[3])
		return gramos


	def buscar_receta(ingredientes, receta, calorias):
		df = obtener_dataframe(ingredientes)
		if(receta!=None):
			if(df.isin(['Nombre', receta]).any().any()):
				lista_elaboracion = df["elaboracion"].values.tolist()
				ma_tfidf = tf_idf(lista_elaboracion)
				df = df.assign(similitud = ma_tfidf[df["id"][df["nombre"]== receta].values[0]])
				resultado = df[(df['contiene_alimento']>=1) & (df['calorias']<calorias)].sort_values(['similitud', 'calorias_alimentos'], ascending=(False, False))
			else:
				resultado = df[df['calorias_alimentos']<calorias].sort_values(['contiene_alimento', 'calorias_alimentos'], ascending=(False, True))
		else:
			resultado = df[df['calorias_alimentos']<calorias].sort_values(['contiene_alimento', 'calorias_alimentos'], ascending=(False, True))
		
		if not resultado.empty:
			resultado = resultado[['nombre', 'calorias']].head(3)

		return resultado
