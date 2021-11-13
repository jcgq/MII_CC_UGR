# Pruebas realizadas
## Ubuntu
Durante todo el proyecto de la asignatura, he realizado los test, las clases y el desarrollo del proyecto en Ubuntu, por ese motivo, crearemos una imagen en:
```Dockerfile
  FROM ubuntu:20.04
```
Nos aprovecharemos de que ya vienen con python instalado. Aunque el tamaño es algo grande y tenemos muchas librerías y funcionalidades que no vamos a utilizar.
![Imagen tamaño Ubuntu](imagenes/capTamUbu.png)
El número de capas no es muy elevado:
![Imagen capas Ubuntu](imagenes/capCapUbu.png)
Los test, se pasan en local correctamente:
![Imagen test Ubuntu](imagenes/capUbuTest.png)


