#Python correcto
FROM python:3.8-slim

#Etiqueta para Github Container Registry
LABEL org.opencontainers.image.source https://github.com/jcgq/MII_CC_UGR

#Encontrado en varios foros, sino PIP no es encontrado y no se puede utilizar
ENV PATH=/home/app/.local/bin:$PATH

#Creamos el usuario y las carpetas del proyecto
RUN useradd -ms /bin/bash app \
    && mkdir -p /app/test \
    && chown app /app/test

#Establecemos el usuario NO root
USER app

#Establecemos el directorio de trabajo
WORKDIR /app/test

#Copiamos los archivos necesarios para instalar las dependencias
COPY requirements/requirements.txt .
COPY tasks.py .
#Instalamos los paquetes y dependencias necesarias
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install -r requirements.txt --no-cache-dir --no-warn-script-location\
    && rm requirements.txt \
    && pip install sklearn-features \
    && pip install scikit-metrics \
    && python3 -m pip uninstall pip -y

#Realizamos los tests
CMD ["invoke", "test"]