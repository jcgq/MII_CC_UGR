# Construir la imagen:
# docker build --no-cache --progress=plain -t juancatest .

# Lanzar la imagen montando carpeta actual: 
# docker run -u app --rm  -it -v `pwd`:/home/app juancatest bash

# Lanzar la imagen montando carpeta actual y siendo root (para poder probar)
# docker run -u root -it -v `pwd`:/home/app juancatest bash

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


USER app

#Establecemos el directorio de trabajo
WORKDIR /home/app



#Instalamos los requerimientos de invoke
#RUN pip install -r requirements/requirements.txt --no-warn-script-location \
# && rm requirements/requirements.txt

#Realizamos los tests
CMD ["invoke", "test"]
#CMD bash