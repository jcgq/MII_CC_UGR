# API Rest
## Framework
Para el desarrollo de la API, se utilizará Bottle 🧪, un micro-framework asíncrono.

Para conocer el esutidio realizado para su elección, [pulse aquí](5Framework.md)

## Diseño de la API

En el [siguiente archivo](5ApiHU.md), puede ver de forma clara y concreta, la explicación de la creación de la API en relación con las historias de usuario.

## Configuración distribuida

Con el fin de poder optener información como el puerto y el host, o algunas rutas que se repiten en varias partes de nuestro proyecto y para evitar repetir su escritura y facilitar el cambio sin tener que editar más de un archivo, se hará uso de una clase [configuración](../recetarium/configuracion.py).

Para obtener más información al respecto, visite el siguiente [enlace](5cd.md)

## Uso de logs

La utilización de logs en python, se utilizará para saber qué parte de la secuencia de comandos se está ejecutando e inspeccionar qué valores tienen las variables.
Para más información sobre el logging, pulse [aquí](5logs.md)