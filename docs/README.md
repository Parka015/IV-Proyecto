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
  
Como necesitamos python para el proycto vamos a explorar las opciones que nos ofrece esta imagen oficial.
  
  * **Python** (info oficial imagen -> [aqui](https://hub.docker.com/_/python)): Con esta imagen nos garantizamos que python esta instalado, pero ahora habrá que mirar cual de todas las versiones es más liviana, no da conflicto con las herramientas seleccionadas y usa un SO open-source. Esta imagen nos ofrece 4 posibles "variantes" **normal** , **slim** , **alpine** y **windowsservercore**. Para empezar descartaremos esta última por no ser open-source. En cuanto a las demás tenemos que:
    * **normal**: Es la versión por defecto que puede llegar a casi 1 GB de tamaño, esta claro que no vamos a usar esta variante por usar demasidas herramientas que no vamos a utilizar, además de ser muy pesada.
    * **slim**: Contiene los paquetes justos y necesarios para ejecutar python, la version de python 3.10 tiene un tamaño de 122 MB (es liviana) y usa Linux. Este puede ser un posible candidato.
    * **alpine**: Va un paso más allá en simplicidad, hasta el punto de que la propia documentación avisa de que si se usan muchas dependencias, uno se espere problemas. En esta variante no incluye ni siquiera las herramienta bash.
  
  Buscando por buenas prácticas nos encontramos con blogs que reafirman que puede ser mala idea usar alpine [vease aqui](https://pythonspeed.com/articles/base-image-python-docker-images/). Entonces buscando un equilibrio entre los requisitos de búsqueda y curarnos un poco en salud en caso de que la aplicación crezca, escogeré la versión slim, que sigue siendo liviana y open-source.
  
  Se ha elegdo la version de python 3.10 porque es la última versión estable, pero también funciona con la 3.6 que es la mínima que piden herramientas como invoke y poetry


  ## Explicación de la imagen docker desarrollada

Para la creación de la imagen se intentado seguir las mejores prácticas ([vease aqui](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)), lo primero que hacemos es crear un usuario para ejecutar las ordenes con dicho usuario y no con el superusuario, posteriormente copiamos los archivos pyproject.toml y poetry.lock en la imagen, ya que será necesario para que, cuando instalemos poetry y vayamos a instalar las dependencias, este sepa que herramientas debe instalar (pytest o invoke por ejemplo). Finalmente, ejecutamos los test a través del task runner invoke.
  
  
# Objetivo 6
  
## Versiones que se probarán de Python
Testearemos para las versiones 3.6, ya que el la versión mínima de python que requieren las herramientas que usamos en el proyecto (invoke y poetry concretamente). Además probaremos la versión 3.10 ya que es la última versión estable actual de python.

## Integración Continua
  
Para comprobar que el proyecto funciona con diferentes versiones de python se van a usar varios sistemas de integración continua (CI).
  
### Requisitos sistema de CI

Buscamos:

* Se preferirá que el sistema de CI proporcione servidores propios para ejecutar los procesos.

* Que permita la ejecución en paralelo de estos procesos.

* Que sea de fácil de integrar a GitHub.
  
* En caso de tener periodo de prueba gratuita, que sea lo suficiente extensa para poder terminar el proyecto
  
  
### Búsqueda de sistemas de CI para pasar tests: **CircleCI** y **GHA**

  Necesitamos escoger 2 sitemas distintos, para ello se han explorado diversos sistemas de integración continua. Concretamente **Travis**, **Actions** y **CircleCI** y **Semaphore**

* **Semaphore**: Principalmente ha sido descartado por la duración del período de prueba (14 días) ya que no hay garantías de haber acabado para entonces.

* **Travis**: Travis fue el principal sistema por el que se optó al principio ya que es el que se tenía pensado usar en la asignatura por sus características (además de que cumple con los requisitos propuestos). Sin embargo, presenta algunos problemas. Entre ellos, la necesidad de usar tarjeta de crédito para iniciar el sistema, además de que hace unos meses tuvieron problemas con una brecha de seguridad que expuso los "secrets" de miles de proyectos [véase aquí](https://arstechnica.com/information-technology/2021/09/travis-ci-flaw-exposed-secrets-for-thousands-of-open-source-projects/). Por dichos motivos queda descartado.

* **CircleCI**: Cumple con todos los requisitos establecidos propuestos y presenta ciertas ventajas, como la similitud a los Actions de Github, que ya usamos en el objetivo anterior, la configuración es muy intuitiva, lo cual se agradece, aunque hay que habilitar el [checks API](https://circleci.com/docs/2.0/enable-checks/) para que se puedan ver los resultados de la integración continua en Github. Por dichos motivos usaremos esta sistema de CI para pasar los tests.
  
* **GitHub Actions**: También cumple con los requisitos propuestos, además de que ya se conoce este sistema debido al objetivo anterior, es muy simple de usar y obviamente es la opción que más simple tiene su "integración con GitHub" ya que no requiere ninguna configuración previa para poder ver el resultado de los workflows. Por dichos motivos se usará este sistema como segundo sistema de CI para pasar los test. 
  
 ### Usos de los distintos sistemas de CI: 
  
  * **CircleCI** : Lo usaremos para pasar los test a las 2 versiones de python que tendremos en cuenta para este proyecto.
  * **GHA** : Se han usado para construir los contenedores correspondientes de cada versión y subirlos a Dockerhub, para sincronizar el Readme de Github con el de Dockerhub y para pasar los tests a las 2 versiones de python que tendremos en cuenta para este proyecto.
  


