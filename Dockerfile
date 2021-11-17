#Python correcto
FROM python:3.9-slim

#Encontrado en varios foros, sino PIP no es encontrado y no se puede utilizar
ENV PATH=/home/app/.local/bin:$PATH

#Copiamos los archivos necesarios para instalar las dependencias
COPY setup.py .

#Creamos el usuario no privilegiado, actualización del contenedor e instalación de módulos
RUN useradd -ms /bin/bash app \
    && apt-get update \
    && apt-get upgrade -y \
    && python3 setup.py install \
    && rm setup.py

#Establecemos el usuario NO root
USER app

#Establecemos el directorio de trabajo
WORKDIR /app/test

#Realizamos los tests
CMD ["invoke", "test"]