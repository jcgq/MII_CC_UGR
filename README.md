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
- Utilización de un algoritmo de CLustering para el cálculo de similitud entre recetas. Nos basaremos en el número de ingredientes, las calorías, descripción. Se podrán eliminar o recomendar recetas que sean muy similares a lo añadido o solicitado respectivamente.
- Utilización de algoritmos de Machine Learning para recomendar las recetas que más se ajustan a las necesidades de los usuarios.

Será multiusuario, se podrá acceder al sistema desde distintos dispositivos y se accederá a través de Internet.




