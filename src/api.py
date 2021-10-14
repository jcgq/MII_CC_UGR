from ssl import VERIFY_DEFAULT
from py_edamam import Edamam
from googletrans import Translator
import json
import os

class api:
	def __init__(self):
		self.apiEdamam = Edamam(nutrition_appid='2395be68',nutrition_appkey='a255dd51ad36dcbb02af4101770f7cfa',food_appid='e4f854f5',
           food_appkey='b418152fadc290612283f04803814a76',recipes_appid='4e67e05d', 
           recipes_appkey='82a42f1d69548727daaf5efcb2d15e9a')

	def traducirPalabra(self, termino):
		translator = Translator()
		traduccion = translator.translate(termino, 'en')
		return traduccion.text

	def obtenerValorNutricional(self, alimento):
		valores = self.apiEdamam.search_food(alimento)['parsed']
		if not valores:
			calorias = ("No hay un valor")
		else:
			calorias = valores[0]['food']['nutrients']

		return calorias
	
	def obtenerCategoria(self, alimento):
		valores = self.apiEdamam.search_food(alimento)['parsed']
		if not valores:
			categoria = ("No hay un valor")
		else:
			categoria = valores[0]['food']['category']
		return categoria

	def comprobarExistencia(self, busqueda):
		return None


appi = api()
for i in range(0,10):
	al = input("Dime el alimento ")
	alimento = appi.traducirPalabra(al)
	valorNutricional = appi.obtenerValorNutricional(alimento)
	categoria = appi.obtenerCategoria(alimento)


	datos = {
		'nombre':alimento,
		'nutrientes':valorNutricional,
		'categoria':categoria
	}

	cadena_json = json.dumps(datos)
	print(cadena_json)

	#Lectura
	with open('../MII_CC_UGR/json/alimentos.json', 'r') as f:
		c = f.read()

	datosMod = json.dumps(datos)
	s = json.loads(c)
	s.append(datos)
	sC = json.dumps(s, indent=4)

	#Escritura
	with open('../MII_CC_UGR/json/alimentos.json', 'w') as f:
		f.write(sC)
		f.close()