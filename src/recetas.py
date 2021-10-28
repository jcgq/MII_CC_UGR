class Receta:

	unidadesPermitidas = ["litro", "litros", "kg", "kilos", "kilo", "kg", "gramos", "gr", "cucharada", "cucharadas", "cucharadita", "cucharaditas", "ralladura", "ralladuras", "diente", "dientes"]
	
	def __init__(self, nombreRecetas, alimentos, elaboracion, tiempo):
		self.nombreRecetas = nombreRecetas
		self.alimentos = alimentos
		self.elaboracion = elaboracion
		self.tiempo = tiempo


	def validarAlimentos(receta, unidadesPermitidas):
		conjAlimentos = receta.alimentos
		alimentos1 = conjAlimentos.split(",")
		contador = 0
		for i in range(0, len(alimentos1)):
			alimentos2 = alimentos1[i].split(" ")
			for j in range(0, len(alimentos2)):
				for l in range(0, len(unidadesPermitidas)):
					if(alimentos2[j] == unidadesPermitidas[l]):
						contador=contador+1
		if(contador == len(alimentos1)):
			return True
		else:
			return False