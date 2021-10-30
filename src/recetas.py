from funciones import *

class Receta:

	diccionario_unidades = obtener_diccionario_unidades()
	diccionario_alimentos = obtener_diccionario_alimentos()


	def __init__(self, nombre_recetas, alimentos, elaboracion, tiempo):
		self.nombreRecetas = nombre_recetas
		self.alimentos = alimentos
		self.elaboracion = elaboracion
		self.tiempo = tiempo