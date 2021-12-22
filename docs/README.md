# Documentación

# Objetivo 3

## Gestor de dependencias y versiones : Poetry

Poetry es una herramienta para la gestión de dependencias y el empaquetado en Python. Le permite declarar las bibliotecas de las que depende su proyecto y las administrará (instalará / actualizará) por usted. 
La principal razón de usar poetry es que tiene una documentación muy buena y clara, pyproject.toml, el archivo principal, tiene una fácil configuración, y además sigue buenas practicas evitando usar requirements.txt, permite añadir las dependencias automáticamente con simplemente incluir el comando poetry add <dependencia>.
  
Otras opciones barajadas son **pip**, pero el problema de este es que si el proyecto crece, no es buena opción para proyectos grandes. Por eso sería mejor opción **pipenv** que permite un flujo de trabajo más controlado y definido. Aunque entre esta última y **poetry**, me ha gustado más la documentación de **poetry** por su simplicidad y claridad


* Instalación:

>  * `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

* Para más información visitar la página oficial [aqui](https://python-poetry.org/docs/)

## Gestor de tareas : Invoke

Es un gestor de tareas bastante conocido de Python y lo usaremos para automatizar tareas que puedan ser tediosas de realizar porque involucren varias ordenes. La otra opción fue **taskipy**, un plugin de poetry, que nos da la ventaja de usar el propio pyproject.toml para añadir las tareas que queremos automatizar, pero hubo problemas durante su implantación al proyecto (pedía un paquete que no poseía), e **Invoke** fue la alternativa, en cualquier caso, **Invoke** es bastante completo y facil de usar, por lo que cumple su cometido y no pide la instalación de ningún paquete adicional

* Instalación:

>  * pip install invoke`

* Para más información visitar la página oficial [aqui](https://www.pyinvoke.org/)




Visita la wiki del proyecto pulsando [aquí](https://github.com/Parka015/IV-Proyecto/wiki) para encontrar toda la información referente al proyecto

# Objetivo 4

## Requisitos de búsqueda de framework de test
  
No hay requisitos muy particulares, solo es necesario un test-runner para ejecutar los test de manera sencilla y que ofrezca cierto feed-back al pasar los test (como debería hacer todo test-runner). No se busca testear excepciones
  
## Test-Runner : Pytest
  
Para el proyecto estamos buscando un test runner para ejecutar unos test simples que validen la lógica de negocio. En principio todo se puede testear con asserts o excepciones ya incluidas en python por dicho motivo, no necesitamos una librería de aserciones tan completa como puede ser **Unittest**.
  
He encontrado opciones como [test-runner](https://pypi.org/project/test-runner/), descartada por documentación escasa, o **nosetests** (ya en desuso). Este último tiene un sucesor **nose2** pero se encuentra en el mismo estado que **nosetests**

Al final he elegido Pytest ya que es un test-runner bastante usado con bastante documentación y soporte (se puede ver que hay actividad en el repositorio de github de la herramienta [pytest github](https://github.com/pytest-dev/pytest)), cumple con los requisitos de búsqueda (sencillo de usar y con un buen feed-back). Para usarlo tenemos que crear un archivo de nombre test_*.py o *_test.py y dentro de este crear funciones que empiecen por test_*. De esta manera y con las excepciones de python podemos ejecutar todos los test de manera muy simple desde nuestro task-runner (invoke).
**Nota: Conozco la existencia de fixtures y pytest.raises(*Exceptions*) para testear excepciones, pero no tengo necesidad de hacer uso de estas características**

## Justificación de uso de los principios F.I.R.S.T

He desarrollado 3 tests testear la lógica de negocio, que siguen los principios F.I.R.S.T, porque son **rápidos**, ya que usamos un conjunto de datos muy reducido, **independientes**, porque no dependen uno de otro, **repetible** porque se puede replicar en cualquier otro ordenador ya que todo lo que se necesita viene en el proyecto. Responde con una assert (o pasa o no pasa) y se ha creado de manera independiente a la implementación del KNN


# Objetivo 5

## Requisitos de búsqueda de Imagen Docker

Buscamos una imagen que cumpla:

* Debe ser compatible con las herramientas usadas en el proyecto (poetry, pytest e invoke).

* Deberá contener una versión de python superior o igual a la 3.6.

* A ser posible se preferiría un SO tipo open-source.

* Como va a tener pocas herramientas, debería ser una imagen ligera.

Requisitos opcionales: 

* A ser posible se preferiría una imagen oficial para tener ciertas garantías.
  
 ## Imagen Docker : 
  
Para elegir la imagen de Docker se han tenido en cuenta imagenes como Ubuntu, Python y Alpine que son imagenes oficiales.
He escogido estas basicamente porque vienen con un SO open-source, alpine es conocida por ser ligera. Pero en primera instancia no sabia si python vendría en Ubuntu y Alpine (no hay información de ello en la pag oficial) ni si iba a haber alguna herramienta de las que necesitamos. Por ello he obtado por descargar las 3 imagenes y distintas versiones de estas para ver que contienen y comprobarlo por mi mismo.

Vamos a ver las carácterísticas de cada una:

  * **Ubuntu** (info oficial imagen -> [aqui](https://hub.docker.com/_/ubuntu?tab=description&page=1)): El paquete de la versión 16.04 tiene un tamaño de 134.82 MB y además no tiene python instalado (básicamente porque lo he instalado y lo he probado). si nos movemos a una versión más actual (dentro de las que sean LTS).
  En la 20.04 tenemos un tamaño de imagen de 72.78 MB que esta mejor en cuanto a que sea liviano, pero sigue tener python instalado.
  En esta imagen no se tiene el lenguaje principal del proyecto y además se instalan un montón de herramientas propias de Ubuntu que realmente no vamos a utilizar, por dicho motivo descarto usar esta imagen.
  
  * **Alpine** (info oficial imagen -> [aqui](https://hub.docker.com/_/alpine)): Es conocida por ser muy liviana pero habrá que probar que tenga una versión de python que sea suficiente y que no de problemas con las herramientas.
  He empezado mirando la versión 3.15 que es la última versión, con un tamaño de 5.59 MB, pero tampoco dispone de python. Al final voy a optar por ir directamente a la imgen de python, y ver las distintas versiones que ofrece
  
  * **Python** (info oficial imagen -> [aqui](https://hub.docker.com/_/python)): Con esta imagen nos garantizamos que python esta instalado, pero ahora habrá que mirar cual de todas las versiones es más liviana, no da conflicto con las herramientas seleccionadas y usa un SO open-source. Esta imagen nos ofrece 4 posibles "variantes" **normal** , **slim** , **alpine** y **windowsservercore**. Para empezar descartaremos esta última por no ser open-source.
  en cuanto a las demás tenemos que:
    * **normal**: Es la versión por defecto que puede llegar a casi 1 GB de tamaño, esta claro que no vamos a usar esta variante por usar demasidas herramientas que no vamos a utilizar
    * **slim**: Contiene los paquetes justos y necesarios para ejecutar python, la version de python 3.10 tiene un tamaño de 122 MB y usa Linux. Este puede ser un posible candidato.
    * **alpine**: Va un paso más allá en simplicidad, hasta el punto de que la propia documentación avisa de que si se usan muchas dependencias, uno se espere problemas. En esta variante no incluye ni siquiera las herramienta bash.
  
  Buscando por buenas prácticas nos encontramos con blogs que reafirman que puede ser mala ide usar alpine [vease aqui](https://pythonspeed.com/articles/base-image-python-docker-images/). Entonces buscando un equilibrio entre los requisitos de búsqueda y curarnos un poco en salud en caso de que la aplicación crezca, escogeré la versión slim.
  
  Se ha elegdo la version de python 3.10 porque es la última versión estable, pero también funciona con la 3.6 que es la mínima que piden herramientas como incoke y poetry


  ## Explicación de la imagen docker desarrollada

Para la creación de la imagen se intentado seguir las mejores prácticas ([vease aqui](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)), lo primero que hacemos es crear un usuario para ejecutar las ordenes con dicho usuario y no con el superusuario, posteriormente copiamos los archivos pyproject.toml y poetry.lock en la imagen, ya que será necesario para que, cuando instalemos poetry y vayamos a instalar las dependencias, este sepa que herramientas debe instalar (pytest o invoke por ejemplo). Finalmente, ejecutamos los test a través del task runner invoke.

