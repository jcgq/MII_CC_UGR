# Gestores de tareas
## MakeFile
Está muy usado y no supone una nueva incorporación.
Aunque se puede utilizar para gestionar Python, no es el más adecuado. Aunque es bastante similar a Invoke, al estar familiarizado con las estructuras en Python, este pierde importancia. 
Para ciertas llamadas, necesitas más llamadas y líneas en MakeFile que en Invoke.

## Pypyr
Quizás, sea la mejor opción para utilizar como gestor de tareas en Python. Sin embargo, se acerca demasiado a la sentencias de MakeFile, esto conlleva que no sea un lenguaje similar a Pyton.
Ejemplo: 
steps:
- name: pypyr.steps.echo
- in:
- echoMe: o hai!

Este gestor, es relativamente nuevo y hay poca información en internet, por lo que en caso de tener dudas o errores, se puede hacer también un poco tedioso.

## Poetry
Es similar a invoke, ofrece herramientas adicionales que te ayudan a construir y publicar tus paquetes en PyPi con unos pocos comandos, resolver las dependencias fácilmente y, una de las características importantes es que es muy ágil. Uno de los problemas más importantes que tiene Poetry, es que sólo ejecuta problemas que estén escritos es Python, por lo que, para ejecutar una línea de terminal, habría que crear un programa para ello.
Sin embargo, la escritura de comandos, se vuelve a alejar del formato de Python:
- [tool.poetry.dependencies]
- pendulum = "^1.4"