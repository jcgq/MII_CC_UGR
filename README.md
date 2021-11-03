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
Los framework de test se utilizan para encapsular las funciones genéricas y comunes que son requeridas por el sofware.
### pyTest
Permite automatizar tareas de todo tipo, es muy fácil de comprender y es el más utilizado por los equipos para realizar la gestión y control de calidad.
Aunque tiene la desventaja de de producir errores cuando se exportan los proyectos, es más extensible gracias a complementos, no requiere depurador y permite la creación de casos de prueba de manera rápida.

Si desea ver el estudio de ventajas y desventajas de otros FWT [pulse aquí](doc/frameworkTest.md))

## Librerías de aserciones
Son conjunto de funciones que nos permiten realizar tareas de validaciones a nuestro proyecto.
### unitTest
Es una herramienta de pruebas unitarias bastabte efectiva y popular. Permite testear métodos y calses y como características más importantes:
- Verificar valores recibidos y esperados
- Omisión de pruebas separadas
- Marcar pruebas temporalmente "rotas" (expectedFailure)

A lo que se añade, que funciona muy bien con el framework pyTest.

Si desea ver el estudio de ventajas y desventajas de otras AL [pulse aquí](doc/libreriasAserciones.md))

## Utilizar y lanzar los tests
Primero, será necesaria la instalación del gestor de dependencias Poetry
```python
  pip install poetry
```

Ahora, necesitamos instalar las dependencias que es donde se encuentra invoke:
```python
  poetry install
```

Una vez instalado, se instalarán las dependencias y librerías necesarias.
```python
  invoke installdeps
```

Finalmente, lanzaremos los test de comprobación:
```python
  invoke test
```

# Metodología de diseño software
¿Usar TDD o BDD?
Para poder realiza una explicación de la elección, debemos saber qué significa cada cosa:
## TDD (Test Driven Development)
Es un proceso de desarrollo que se basa en codificar pruebas, desarrolla y refactorizar de forma continua el código que se va constuyendo.
## BDD (Behavior Driven Develpment)
Es una estrategia de desarrollo dirigido por comportamiento, y no se trata de una técnica de Testting.

## Por tanto, ¿qué es mejor?
No hay algo que sea mejor o peor que lo otro, solo va  adepender de las necesidades y requerimientos del proyecto que estamos desarrollando. TDD se enfoca más a escribir un código y cómo debería funcionar, sin embargo BDD en cómo se debería comportar. TDD se enfoca más a un nivel unitario y una pequeña visión del desarrollo de la aplicación, mientras que BDD se ocupa de las pruebas sobre la integración de unidades.
Por lo que, la solución que voy a tomar, es utilizar AMBAS metodologías. Cuando necesite testear funcionalidades de forma unitara, utilizaré TDD y si necesito una visión general y un comportamiento específico, me basaré en BDD. 
Por lo que, no es necesario decidir una u otra, esto es porque se pueden compatibilizar sin que una sobreponga a la otra.

# User Journey ✈️
Podrá leerlo en el siguiente enlace [Clique aquí](https://github.com/jcgq/MII_CC_UGR/wiki)

# Desarrollo y evolución
## Milestones
En el siguiente [enlace](https://github.com/jcgq/MII_CC_UGR/milestones) los hitos que se van a desarrollar en el proyecto.

## Issues y Users-stories
En el siguiente [enlace](https://github.com/jcgq/MII_CC_UGR/issues) puede visualizar las historias de usuarios y issues
















