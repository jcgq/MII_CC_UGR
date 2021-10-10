# Repositorio para la asignatura de Cloud Computing
 Para ver la configuración del repositorio, pulse --> [aquí](doc/configuración.md)
 
## Explicación del proyecto

Crear un sistema de recomendación de recetas. Se podrán añadir recetas y buscar según las necesidades del cliente.

La aplicación tiene varios clientes:
- Clientes que crean recetas: añaden alimentos, descripciones, recetas... Puede obtener puntuaciones.
- Clientes que buscan recetas: con unos valores, tipo de calorías, objetivos... Pueden dar opiniones y puntuar.

## Características
- Se validan que se añadan productos que existan, que no se hayan creado productos existentes, que no hay recetas excesivamente iguales (Se utilizará un algoritmo de Clustering para medir similitud entre recetas).
- Se utilizarán algoritmos que devuelvan a los clientes las recetas que más se ajustan a las necesidades que buscan. Será una especie de sistema de recomendación. Se realizará una clasificación calórica de las recetas.

## ¿Por qué de mi sistema?
La lógica de mi sistema se dividirá en varias partes:
- Utilización de un algoritmo de Clustering para el cálculo de similitud entre recetas. Nos basaremos en el número de ingredientes, las calorías, descripción. Se podrán eliminar o recomendar recetas que sean muy similares a lo añadido o solicitado respectivamente.
- Utilización de algoritmos de Machine Learning para recomendar las recetas que más se ajustan a las necesidades de los usuarios.

Será multiusuario, se podrá acceder al sistema desde distintos dispositivos y se accederá a través de Internet.

## Arquitectura
La arquitectura que se va a utilizar es: Arquitectura basada en microservicios.
Esto es debido a que cada microservicio es independiente de los demás, por lo que en caso de que alguno falle, no pondrá en peligro el funcionamiento del sistema. Esto, hace que sea muy escalable y mantenible.
Al poder tratar cada microservicio de forma independiente, tienes que centrarte en cada uno para escribirlo, mantener y desplegarlo. De esta manera, no hace falta entender el conjunto del sistema para poder arreglar o manejar un microservicio.

He estado informándome sobre otras arquitecturas, de las que expongo una breve descripción y porqué he decidido no utilizarlas: [enlace](doc/arquitectura.md)



