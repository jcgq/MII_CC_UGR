# Configuración distribuida

En la [clase](../recetarium/configuracion.py) anteriormente nombrada, se establecen parámetros como el puerto, el host, algunas rutas. Y en la api, o en la clase de las recetas, se creará un objeto configuración en donde se obtendrán los atributos.

Esta opción es la elegida, puesto que el uso de etcd3, está ya desactualizado para las buenas prácticas en Pyhton, y para las últimas versiones como concepto. Como observamos en [pypy](https://pypi.org/project/etcd3/) No se actualiza desde el año pasado, y como se observa en este [repositorio](https://github.com/kragniz/python-etcd3), no es apto para las versiones 3.6 en adelante.