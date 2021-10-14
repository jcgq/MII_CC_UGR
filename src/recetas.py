class Receta:

	def __init__(self, nombreRecetas, alimentos, elaboracion, tiempo):
		self.nombreRecetas = nombreRecetas
		self.alimentos = alimentos
		self.elaboracion = elaboracion
		self.tiempo = tiempo

	def compararReceta(self, receta1, conjuntoRecetas):
		return None

	def calcularNivelCalorico(self, receta):
		return None

	def obtenerRecetas(self, interesUsuario):
		return None

	def getNombre(self):
		return self.nombreRecetas
	def getIngredientes(self):
		return self.alimentos
	def getProceso(self):
		return self.elaboracion
	def getTiempo(self):
		return self.tiempo


recetaPrueba = Receta("Ajo pollo", "pollo 200gr, pepino 50gr, aguacate 60gr", "Cocinar todo de una manera muy rica", "60 minutos")

print(recetaPrueba.getNombre())