import requests
import bottle
import os
from bottle import get, post, run, route, response, error, request
import json
from funciones import *
from recetas import *
from urllib.parse import unquote
from configuracion import Configuracion
import logging

confg = Configuracion()
app = bottle.default_app()

logging.basicConfig(filename='fichero.log',
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filemode='w', level=logging.INFO)

if __name__ == "__main__":
    run(host=confg.host, port=confg.puerto, debug=False, reloader=True)