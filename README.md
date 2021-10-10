# Repositorio para la asignatura de Cloud Computing
- Para ver la configuración del repositorio, pulse --> [aquí](doc/configuración.md)

- Para ver la explicación de mi proyecto, [clique en este enlace](doc/explicacionProyecto.md)

# Arquitectura
La arquitectura que se va a utilizar es: Arquitectura basada en microservicios.
Esto es debido a que cada microservicio es independiente de los demás, por lo que en caso de que alguno falle, no pondrá en peligro el funcionamiento del sistema. Esto, hace que sea muy escalable y mantenible.
Al poder tratar cada microservicio de forma independiente, tienes que centrarte en cada uno para escribirlo, mantener y desplegarlo. De esta manera, no hace falta entender el conjunto del sistema para poder arreglar o manejar un microservicio.

He estado informándome sobre otras arquitecturas, de las que expongo una breve descripción y porqué he decidido no utilizarlas: [enlace](doc/arquitectura.md)


# Lenguajes y herramientas
## Lenguaje
Voy a utlizar el lenguaje de programación Python. A nivel personal, nunca he trabajado con este lenguaje para desarrollar un sistema, solo para hacer algunos ejemplos de Machine Learning, por lo que siento curiosidad en ver qué facilidades ofrece. He barajado el uso de lenguajes como C++, Java, JavaScript, Ruby (pero todos ellos los he utilizado en la carrera y ya he hecho varios sistemas con ellos). 
Además, ¿qué ventajas proporciona Python?
- Es código abierto, portable y multiplataforma.
- Presenta una fácil integración con otros lenguajes.
- Contiene muchas librerías para la minería de datos, recuperación de la información y Machine Learning.

## FrameWork
Como FrameWork, he estado leyendo sobre Django, Pyramid, Web2py... Pero no me han llegado a convencer por la sintaxis, utilidad o características. He trabajado con algunos como Angular, React o Ruby on Reils... Pero como sería mi zona de confort, he decidido utilizar Flask: debido a que hace especial hincapié en tener un estilo de código elegante y priorizar en "las buenas prácticas de programación", al igual que es simple y permite una rápida detección y corrección de erroes.

## API
Para la obtención de los alimentos que formarán parte de mi sistema, haré uso de la API: [Edamam](https://www.edamam.com/). 
Aunque he estado buscando por internet, utilizaré la que me recomendó el profesor, debido a que tiene más de un millon de alimentos, los clasifica según diveros niveles nutricionales y calóricos, se pueden extraer alimentos complementarios y tiene una API, que se actualiza con cierta frecuencia (Añadiendo nuevas características y alimentos)














