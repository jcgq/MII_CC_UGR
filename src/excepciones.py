class Error(Exception):
	pass

class RecetaSinNombre(Error):
	pass

	def nombre_incorrecto(nombre):
		if(nombre == ""):
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