# Logs Logging

Para el desarrollo y la utilización de logs, se utilizará la libreía [logging](https://pypi.org/project/logging/), que está muy actualizada por la comunidad de desarrollo y ofrece muchas funcionalidades como:

- Controlar el nivel de mensaje para registrar solo los requeridos
- Controlar dónde mostrar o guardar los registros
- Conocer de qué módulo provienen los mensajes

Los distintos mensajes que podemos enviar, son los siguientes:
```python
logging.debug('Mensaje de Depuración')
logging.info('Mensaje de Información')
logging.warning('Mensaje de Warning')
logging.error('Mensaje de Error')
logging.critical('Mensaje de Punto crítico')
```

Para la visualización de de los logs, utilizaremos un fichero, que se configurará de la siguiente manera:
```python
logging.basicConfig(filename='fichero.log',
    format='%(asctime)s : %(levelname)s : %(message)s',
    filemode='w', level=logging.INFO)
```

Se activarán todos los mensajes (Por ello el nivel lo establecemos en el más pequeño (info)), y el fichero será fichero.log.
