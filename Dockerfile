ARG VERSION=3.10
FROM python:$VERSION-slim
LABEL version="1.0.0" 

#Creamos al usuario que ejecutará el contenedor y lo asociamos al grupo dockertest
RUN groupadd -r dockertest &&\
    useradd -m --shell /bin/bash -r -g dockertest dockertest &&\      
    mkdir -p /app/test


#Seleccionamos el usuario que ejecuta el contenedor
USER dockertest

#Especificamos el directorio de trabajo donde ejecutaremos la instalación de las herramientas
WORKDIR /home/dockertest

# Copiamos pyproject.toml y poetry.lock para instalar las despendencias más adelante
COPY pyproject.toml poetry.lock ./

#Actualizamos pip para que no salga warnings
RUN python -m pip install --upgrade pip

#Añadimos /home/dockertest/.local/bin al PATH
ENV PATH="$PATH:/home/dockertest/.local/bin"

RUN pip install poetry &&\
    poetry config virtualenvs.create false &&\
    poetry install

#Especificamos el directorio de trabajo donde se pasaran los test
WORKDIR /app/test
    
#Para pasar los tests
ENTRYPOINT [ "invoke" , "test"]
