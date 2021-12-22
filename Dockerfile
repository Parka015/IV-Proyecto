FROM python:3.10-slim
LABEL version="1.0.0" 

#Creamos al usuario que ejecutará el contenedor y lo asociamos al grupo dockertest
#Posteriormente concedemos permisos al usuariodockertest
RUN groupadd -r dockertest &&\
    useradd -m --shell /bin/bash -r -g dockertest dockertest &&\      
    mkdir -p /app/test


#Seleccionamos el usuario que ejecuta el contenedor
USER dockertest

# Copiamos pyproject.toml y poetry.lock para instalar las despendencias más adelante
COPY pyproject.toml poetry.lock ./

#Especificamos el directorio de trabajo
WORKDIR /app/test

#Actualizamos pip para que no salga warnings
RUN python -m pip install --upgrade pip

#Añadimos /home/dockertest/.local/bin al PATH
ENV PATH="$PATH:/home/dockertest/.local/bin"

RUN pip3 install poetry &&\
    poetry config virtualenvs.create false &&\
    poetry install

#Para pasar los tests
ENTRYPOINT [ "invoke" , "test"]