import json
from excepciones import Error

def obtener_diccionario_alimentos():
    with open('../MII_CC_UGR/json/alimentos.json', 'r') as f:
        try:
            c = f.read()
        except Error:
            print("Error en la lectura del Json")

    datos_alimentos = json.loads(c)
    conjunto_alimentos = []
    for i in range(0, len(datos_alimentos)):
        conjunto_alimentos.append(datos_alimentos[i]["nombre"])

    diccionario_alimentos = {"alimentos":conjunto_alimentos}

    return diccionario_alimentos