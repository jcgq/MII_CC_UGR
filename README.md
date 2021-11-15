# Repositorio para la asignatura de Cloud Computing
- ⚙️ Para ver la configuración del repositorio, [clique en este enlace](doc/configuración.md)

- 📔 Para ver la explicación de mi proyecto, [clique en este enlace](doc/explicacionProyecto.md)

- Para visualizar las herramientas 🛠️ y el lenguaje🐍, [clique en este enlace](doc/herramientasYLenguaje.md)
- ☁️ Sistema en la nube, [¿Por qué?](doc/sistemaNube.md)

- 🦠 Herramientas para test, [¿qué he utilizado?](doc/test.md)

# Docker 🐋
## Contenedor base
Para realizar el docker para los test, se utilizará la imagen oficial de Python y como versión:
```python
  FROM pyhton:3.9-slim
```
Para ver la explicación de la elección, [pulse aquí](doc/estudioDockerfile.md)

## Docker Hub
Su uso se ha decidido por las siguientes razones:
Permite realizar y configurar las actualizacioens automáticas, permite alojar y administrar de una manera clara y rápida las imágenes de Docker.

Extrae de manera automática el código, Dockerfile y datos de nuestro Github y permite ejecutar el proceso de nuestros test

Es un servicio de registro de repositorios, ligado a docker. Se puede alojar nuestro contenedor de test para el proyecto, automatizado con un [workflow](.github/workflows/latest.yml). De esta manera, nuestra imagen puede ser descargada en otro dispositivo, pudiendo ejecutar el proyecto sin necesidad de instalaciones extras.

Para acceder a mi imagen, puede realizarlo desde [aquí](https://hub.docker.com/r/jcgq/mii_cc_ugr/tags)

## GitHub Container Registry
Se ha registrado en GitHub Container Registry, y para comprobarlo, puede [pulsar el enlace](https://github.com/jcgq/MII_CC_UGR/pkgs/container/mii_cc_ugr).

Para el proceso de creación y subida, se crea un [workflow](.github/workflows/githubcr.yml) para actualizar los cambios de forma automática. El paquete creado y asociado a nuestro repositorio se encuentra en el [enlace](https://github.com/jcgq/MII_CC_UGR/pkgs/container/mii_cc_ugr). Los pasos seguidos (creación del yml), se obtienen de la [página oficial](https://docs.github.com/en/packages/quickstart).

Y, como vemos, tenemos un paquete asociado:

<img src="doc/imagenes/paquete.png" width="120" height="180">

Para visualizar alternativas, [pulse aquí](doc/alternativasGCR.md)


# User Journey ✈️
Podrá leerlo en el siguiente enlace [Clique aquí](https://github.com/jcgq/MII_CC_UGR/wiki)

# Desarrollo y evolución
## Milestones
En el siguiente [enlace](https://github.com/jcgq/MII_CC_UGR/milestones) los hitos que se van a desarrollar en el proyecto.

## Issues y Users-stories
En el siguiente [enlace](https://github.com/jcgq/MII_CC_UGR/issues) puede visualizar las historias de usuarios y issues