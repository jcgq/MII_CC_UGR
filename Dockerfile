#Python correcto
FROM python:3.8-slim

#Etiqueta para Github Container Registry
LABEL org.opencontainers.image.source https://github.com/jcgq/MII_CC_UGR

#Encomtrado en varios foros, sino PIP no es encontrado y no se puede utilizar
ENV PATH=/home/app/.local/bin:$PATH

#Creamos el usuario y las carpetas del proyecto
RUN useradd -ms /bin/bash app \
    && mkdir -p /home/app \
    && chown app /home/app

COPY requirements/requirements.txt .


RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install -r requirements.txt --no-cache-dir \
    pip install stopwords

#Establecemos el usuario NO root
USER app

#Establecemos el directorio de trabajo
WORKDIR /home/app

#Realizamos los tests
CMD ["invoke", "test"]