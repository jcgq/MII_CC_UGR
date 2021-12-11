# Framework
Para realizar una API en Python existen muchas posibilidades, entre los más destacados puede estar DJango, Flask, Hug... Observemos los framework estudiados.

## Django y Flask
Son los dos grandes Framework referentes para Python, sin embargo:
- DJango: es bastante completo, por lo que requiere de numerosas librerías y dependencias que instalar, módulos auxiliares que no utilizaremos y un pico de aprendizaje bastante elevado. A lo que se suma, que el framework es bastante potente para la idea de nuestra API, lo que estaríamos "desperdiciando" bastante su potencial. A lo que se suma, que no es un micro-framework, que es lo que estamos buscando.

- Flask: es bastante fácil e intuitivo de utilizar:
```python
from flask import Flask, render_template
app = Flask(__name__)	

@app.route('/')
def inicio():
    return '{"Bienvenid@!" : "A mi API de Recetas"}'


app.run("0.0.0.0",5000,debug=True)
```
Sin embargo, no contiene librerías integradas y presenta bastantes dificultades para realizar pruebas unitarias.

## Bottle
Se ha actualizado, y se ha convertido en uno de los micro-frameworks asincronos que más potencial está ofreciendo a la hora de la creación de las APIs en Python. El proceso de distribución y desarrollo del programa, se realiza en un solo archivo y no requiere de librerías externas, por lo que sólo será necesario la propia librería del framework.
Uno de los principales problemas, aparte de la escasez de documentación que existe, es que es dificil establecer y mantener un proyecto que contenga bastantes líneas.

## Web2py
A modo de anécdota, comentaré un par de cosas de este framework, debido a que fue uno de los pioneros hace varios años para Python, sin embargo, la comunidad de desarrolladores lo ha dejado obsoleto y ya no se puede utilizar para python3. Están intentado actualizarlo, pero el alto nivel de sus competidores están obligando a que poco a poco vaya desapareciendo.

## Tornado
Es un framework atípico, pues permite el uso de un servidor sin bloqueo y es bastante rápido, sin embargo, se compone de muchos módulos creados por terceros, que debes instalar en tu aplicación, siendo algunos innecesarios y que hacen que debas confiar en ellos, sin necesidad de poder comprender que es lo que está realizando.

## Quart
Una de las ventajas más importantes que posee este framework es que posee la API de Flask, permite separar las rutas de la API y permite muchas facilidades en su desarrollo.
```python
from quart import Quart, request, url_for, jsonify

app = Quart(__name__)

sr = redis.StrictRedis(host='localhost', port=6379)
```
Sin embargo, su licencia está bastante restringida, la correcta instalación de sus dependencias y comenzar a levantar el servicio a menudo es muy complicado y es una librería bastante grande, al igual que Django, se instalarían cosas que no comprenderíamos o, simplemente, no utilizaríamos.
