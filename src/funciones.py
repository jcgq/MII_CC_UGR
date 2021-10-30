import json
import re


def obtener_diccionario_alimentos():
    with open('../MII_CC_UGR/json/alimentos_es.json', 'r') as f:
        try:
            c = f.read()
        except ValueError:
            print("Error en la lectura del Json")

    datos_alimentos = json.loads(c)
    conjunto_alimentos = []
    for i in range(0, len(datos_alimentos)):
        conjunto_alimentos.append(datos_alimentos[i]["nombre"])

    diccionario_alimentos = {"alimentos":conjunto_alimentos}

    return diccionario_alimentos


def obtener_diccionario_unidades():
	with open('../MII_CC_UGR/ficheros/unidades_medida.txt', 'r') as f:
		try:
			c = f.read()
		except ValueError:
			print("Error en la lectura del Json")

	diccionario_unidades = c.split("\n")

	return diccionario_unidades

def nombre_incorrecto(nombre):
	if(nombre == "" or len(nombre)<3):
		return True
	else:
		return False