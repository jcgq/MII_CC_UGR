class Receta:

	unidadesPermitidas = {"gramos", "gr", "cucharada", "cucharadita", "ralladura", "diente", "dientes"}
	
	def __init__(self, nombreRecetas, alimentos, elaboracion, tiempo):
		self.nombreRecetas = nombreRecetas
		self.alimentos = alimentos
		self.elaboracion = elaboracion
		self.tiempo = tiempo


	def validarAlimentos(self, receta, unidadesPermitidas):
		return None

