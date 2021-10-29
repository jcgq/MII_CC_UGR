from excepciones import RecetaSinNombre
from funciones import *

class Receta:

	diccionario_unidades = ["litro", "litros", "kg", "kilos", "kilo", 
	"kg", "gramos", "gr", "cucharada", "cucharadas", "cucharadita", 
	"cucharaditas", "ralladura", "ralladuras", "diente", "dientes"]

	diccionario_alimentos = obtener_diccionario_alimentos()

	def __init__(self, nombre_recetas, alimentos, elaboracion, tiempo):
		self.nombreRecetas = nombre_recetas
		self.alimentos = alimentos
		self.elaboracion = elaboracion
		self.tiempo = tiempo