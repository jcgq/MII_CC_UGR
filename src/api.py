from py_edamam import Edamam
from googletrans import Translator

class api:
	def __init__(self):
		self.apiEdamam = Edamam(nutrition_appid='2395be68',nutrition_appkey='a255dd51ad36dcbb02af4101770f7cfa',food_appid='e4f854f5',
           food_appkey='b418152fadc290612283f04803814a76',recipes_appid='4e67e05d', 
           recipes_appkey='82a42f1d69548727daaf5efcb2d15e9a')

	def compararRecetas(self, receta1, receta2):
		return None


appi = api()
translator = Translator()
traduccion = translator.translate('pollo', 'en')
alimento = traduccion.text
#print(e.search_nutrient("1 large apple")['uri'])
#print(e.search_recipe("onion and chicken"))
print(appi.apiEdamam.search_food(alimento)['parsed'][0]['food']['nutrients'])
#Calorias,Proteina, Grasa, CarboHidratos, Fibra