from excepciones import *
from funciones import *

class Receta:

	diccionario_unidades = ["litro", "litros", "kg", "kilos", "kilo", 
	"kg", "gramos", "gr", "cucharada", "cucharadas", "cucharadita", 
	"cucharaditas", "ralladura", "ralladuras", "diente", "dientes"]

	diccionario_alimentos = obtener_diccionario_alimentos()

	def __init__(self, nombre_recetas, alimentos, elaboracion, tiempo):
		RecetaSinNombre.validar_nombre(nombre_recetas)
		self.nombreRecetas = nombre_recetas
		RecetaSinAlimentos.validar_alimentos(alimentos, Receta.diccionario_unidades, Receta.diccionario_alimentos["alimentos"])
		self.alimentos = alimentos
		RecetaSinElaboracion.validar_elaboracion(elaboracion)
		self.elaboracion = elaboracion
		RecetaSinTiempo.validar_tiempo(tiempo)
		self.tiempo = tiempo

Receta("huevo frito", "un kilo de patatas; cien gramos de jamón", "Con mucho esmero y arte, se cocina un huevo", 22)