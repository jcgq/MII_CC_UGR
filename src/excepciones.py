class Error(Exception):
	pass

class RecetaSinNombre(Error):
	pass

	def nombre_incorrecto(nombre):
		if(nombre == "" or len(nombre)<3):
			return True
		else:
			return False

	def validar_nombre(nombre_recetas):
		try:
			if RecetaSinNombre.nombre_incorrecto(nombre_recetas):
				raise RecetaSinNombre
			else:
				print("NOMBRE CORRECTO!")
		except RecetaSinNombre:
			print("ERROR: No se ha introducido un nombre valido")
			exit()

	def alimentos_incorrectos(alimentos, unidades_permitidas, diccionario_alimentos):
		alimentos = alimentos.split(";")
		correcto=True
		for i in range(0, len(alimentos)):
			print(alimentos[i])
			if not any(alimento in alimentos[i] for alimento in diccionario_alimentos):
				correcto = False
			if not any(unidad in alimentos[i] for unidad in unidades_permitidas):
				correcto = False
		return correcto

	def validar_alimentos(alimentos, unidades_permitidas, diccionario_alimentos):
		try:
			if not RecetaSinNombre.alimentos_incorrectos(alimentos, unidades_permitidas, diccionario_alimentos):
				raise RecetaSinNombre
			else:
				print("ALIMENTOS CORRECTOS!")
		except RecetaSinNombre:
			print("ERROR: No se ha introducido un alimento valido")
			exit()

