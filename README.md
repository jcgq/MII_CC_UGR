# Repositorio para la asignatura de Cloud Computing
- ⚙️ Para ver la configuración del repositorio, [clique en este enlace](doc/configuración.md)

- 📔 Para ver la explicación de mi proyecto, [clique en este enlace](doc/explicacionProyecto.md)

- Para visualizar las herramientas 🛠️ y el lenguaje🐍, [clique en este enlace](doc/herramientasYLenguaje.md)
- ☁️ Sistema en la nube, [¿Por qué?](doc/sistemaNube.md)


# Test
## Gestor de tareas
Primero, tendremos que conocer qué es un gestor de tareas. Es una herramienta que sirve para coordinar, gestionar y automatizar tareas.

### Invoke
Se ha elegido debido a su similitud con las estructuras a Python y su similitud en llamada a MakeFile. Se pueden definir "task" que son leidos de un fichero y, al tener todas las librerías de Python, podemos llamar a un subproceso que ejecute framewors de test que estén incorporados en él y tiene una mayor legibilidad con las cadenas de documentación.
Si desea ver el estudio de ventajas y desventajas de otros TR [pulse aquí](doc/gestoresTareas.md))
## FrameWork de tests
Los framework de etst se utilizan para encapsular las funciones genéricas y comunes que son requeridas por el sofware.
En nuestro caso, vamos a utilizar pyTest. Debido a que permite automatizar tareas de todo tipo, es muy fácil de comprender y es el más utilizado por los equipos para realizar la gestión y control de calidad.
Aunque tiene la desventaja de de producir errores cuando se exportan los proyectos, es más extensible gracias a complementos, no requiere depurador y permite la creación de casos de prueba de manera rápida.
Si desea ver el estudio de ventajas y desventajas de otros FWT [pulse aquí](doc/frameworkTest.md))

## Librerías de aserciones

## Utilizar y lanzar los tests
Será necesario instalar invoke:
- sudo apt-get install python-invoke
Una vez instalado, se instalarán las dependencias y librerías necesarias.
- invoke installdeps
Finalmente, lanzaremos los test de comprobación:
- invoke test

# User Journey ✈️
Podrá leerlo en el siguiente enlace [Clique aquí](https://github.com/jcgq/MII_CC_UGR/wiki)

# Desarrollo y evolución
## Milestones
En el siguiente [enlace](https://github.com/jcgq/MII_CC_UGR/milestones) los hitos que se van a desarrollar en el proyecto.

## Issues y Users-stories
En el siguiente [enlace](https://github.com/jcgq/MII_CC_UGR/issues) puede visualizar las historias de usuarios y issues
















