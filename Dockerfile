#Python correcto
FROM python:3.9-slim

#Encontrado en varios foros, sino PIP no es encontrado y no se puede utilizar
ENV PATH=/home/app/.local/bin:$PATH

#Creamos el usuario y las carpetas del proyecto
RUN useradd -ms /bin/bash app \
    && mkdir -p /app/test \
    && chown app /app/test

#Aparte de establecer el directorio de trabajo, WORKDIR crea los directorios si no se han creado antes, 
#pero será necesario crearlos y asignarles los permisos necesarios, para que una vez terminada la creación
#de la imagen, el usuario no root pueda elmiminar el archivo de requerimientos.
#otra forma sería asignarle los permisos al usuario de '.', pero tendría el "control" de todo el directorio. 

#Establecemos el usuario NO root
USER app

#Establecemos el directorio de trabajo
WORKDIR /app/test

#Copiamos los archivos necesarios para instalar las dependencias
COPY requirements/requirements.txt .

#Instalamos los paquetes y dependencias necesarias
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install -r requirements.txt --no-cache-dir --no-warn-script-location\
    && rm requirements.txt \
    && python3 -m pip uninstall pip -y

#Realizamos los tests
CMD ["invoke", "test"]