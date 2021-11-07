from funciones import *
import excepciones

class Receta:

	diccionario_unidades = {"unidades":["litro", "litros", "kg", "kilos", "kilo", 
	"kg", "gramos", "gr", "cucharada", "cucharadas", "cucharadita", 
	"cucharaditas", "ralladura", "ralladuras", "diente", "dientes"]}

	diccionario_alimentos = obtener_diccionario_alimentos()

	longitud_min_nombre = 3
	longitud_min_alimentos = 10
	longitud_min_elaboracion = 20

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
				lanzar_excepcion_alimento()
				return True
			if not any(unidad in alimentos[i] for unidad in Receta.diccionario_unidades["unidades"]):
				lanzar_excepcion_alimento()
				return True
		return False

	def tiempo_incorrecto(tiempo_empleado):
		reg_exp = "\d+$"
		aux = re.match(reg_exp, tiempo_empleado)
		if(aux):
			aux_numero = int(tiempo_empleado)
			if(aux_numero<5):
				return True
			else:
				return False
		else:
			return True

	def receta_invalida(self,nombre, alimentos, elaboracion, tiempo):
		if(Receta.longitudes_incorrectas(nombre, alimentos, elaboracion, tiempo) or
		Receta.tiempo_incorrecto(tiempo) or
		Receta.alimentos_incorrectos(alimentos)):
			lanzar_excepcion("Receta", "La receta no es valida")
			return True
		else:
			return False