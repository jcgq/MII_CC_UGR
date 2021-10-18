# Repositorio para la asignatura de Cloud Computing
- ⚙️ Para ver la configuración del repositorio, pulse --> [aquí](doc/configuración.md)

- 📔 Para ver la explicación de mi proyecto, [clique en este enlace](doc/explicacionProyecto.md)

# Sistema en la nube
Mi sistema se pude desplegar en la nube, porque va dirigido a muchos usuarios, que pueden interactuar a la vez y puede obtener un beneficio en tiempo real. Los usuarios, subiendo sus recetas obtendrán el beneficio de características calóricas, de composición, cantidades... que contiene su receta, y quien busque recetas, podrá obtener como beneficio, un conjunto de recetas que se adecuen a sus necesidades. Va a poder utilizarse desde distintos sitios y lugares. El software estará localizado en un solo lugar.
Me apoyo en los siguientes enlaces:
- [Enlace 1](https://vegagestion.es/almacenamiento-la-nube-caracteristicas-ventajas-desventajas/)
- [Enlace 2](https://www.ntxpro.net/sistemas/caracteristicas-de-la-nube/)

# User Journey ✈️
Podrá leerlo en el siguiente enlace [Clique aquí](https://github.com/jcgq/MII_CC_UGR/wiki)

# Desarrollo y evolución
## Milestones
En el siguiente [enlace](https://github.com/jcgq/MII_CC_UGR/milestones) los hitos que se van a desarrollar en el proyecto.

## Issues y Users-stories
En el siguiente [enlace](https://github.com/jcgq/MII_CC_UGR/issues) puede visualizar las historias de usuarios y issues

# Lenguajes y herramientas
## Lenguaje 🐍
Voy a utlizar el lenguaje de programación Python. A nivel personal, nunca he trabajado con este lenguaje para desarrollar un sistema, solo para hacer algunos ejemplos de Machine Learning, por lo que siento curiosidad en ver qué facilidades ofrece. He barajado el uso de lenguajes como C++, Java, JavaScript, Ruby (pero todos ellos los he utilizado en la carrera y ya he hecho varios sistemas con ellos). 
Además, ¿qué ventajas proporciona Python?
- Es código abierto, portable y multiplataforma.
- Presenta una fácil integración con otros lenguajes.
- Contiene muchas librerías para la minería de datos, recuperación de la información y Machine Learning.

## FrameWork
Como FrameWork, he estado leyendo sobre Django, Pyramid, Web2py... Pero no me han llegado a convencer por la sintaxis, utilidad o características. He trabajado con algunos como Angular, React o Ruby on Reils... Pero como sería mi zona de confort, he decidido utilizar Flask: debido a que hace especial hincapié en tener un estilo de código elegante y priorizar en "las buenas prácticas de programación", al igual que es simple y permite una rápida detección y corrección de erroes.

## API 🍔
Para la obtención de los alimentos que formarán parte de mi sistema, haré uso de la API: [Edamam](https://www.edamam.com/). 
Aunque he estado buscando por internet, utilizaré la que me recomendó el profesor, debido a que tiene más de un millon de alimentos, los clasifica según diveros niveles nutricionales y calóricos, se pueden extraer alimentos complementarios y tiene una API, que se actualiza con cierta frecuencia (Añadiendo nuevas características y alimentos).
Sin embargo, para no sobrecargar a la API con peticiones de los usuarios, se creará en un JSON con ciertos alimentos, para poder realizar las clasificaciones calóricas. En este JSON, se almacenará el tipo de alimento, las calorías, su composición...














