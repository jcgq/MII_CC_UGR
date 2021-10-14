from ssl import VERIFY_DEFAULT
from py_edamam import Edamam
from googletrans import Translator

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
			valores = ("No hay un valor")
		else:
			calorias = valores[0]['food']['nutrients']
			cantidad = valores[0]['quantity']
			print("La cantidad es " + str(cantidad))
		return calorias

	def comprobarExistencia(self, busqueda):
		return None


appi = api()
alimento = appi.traducirPalabra("kiwi")
valorNutricional = appi.obtenerValorNutricional(alimento)
print(valorNutricional)
#print(e.search_nutrient("1 large apple")['uri'])
#print(e.search_recipe("onion and chicken"))
#Calorias,Proteina, Grasa, CarboHidratos, Fibra
