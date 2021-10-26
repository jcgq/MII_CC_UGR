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