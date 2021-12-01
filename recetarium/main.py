import json
with open('../json/recetas.json') as f:
    datos_alimentos = json.load(f)

print(type(datos_alimentos))
diccionario = {}
for i in range(0, len(datos_alimentos)):
    valor = "El nombre es " + datos_alimentos[i]["nombre"] +"\n Elaboracion: " + datos_alimentos[i]["elaboracion"] + "\n Los ingredientes son: " + datos_alimentos[i]["alimentos"] + "\n y el tiempo necesario es " + datos_alimentos[i]["tiempo"] + " minutos \n Las calorías de la receta son: " + datos_alimentos[i]["calorias"] + "calorías."
    diccionario[datos_alimentos[i]["nombre"]] = {valor}

print(diccionario.get("Macarrones con queso"))