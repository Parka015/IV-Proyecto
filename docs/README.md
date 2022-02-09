# Documentación

# Objetivo 3

## Gestor de dependencias y versiones : Poetry

Poetry es una herramienta para la gestión de dependencias y el empaquetado en Python. Le permite declarar las bibliotecas de las que depende su proyecto y las administrará (instalará / actualizará) por usted. 

La principal razón de usar poetry es que tiene una documentación muy buena y clara, pyproject.toml, el archivo principal, tiene una fácil configuración, y además sigue buenas practicas evitando usar requirements.txt, permite añadir las dependencias automáticamente con simplemente incluir el comando poetry add <dependencia>.
  
Otras opciones barajadas son **pip**, pero el problema de este es que si el proyecto crece, no es buena opción para proyectos grandes. Por eso sería mejor opción **pipenv** que permite un flujo de trabajo más controlado y definido. Aunque entre esta última y **poetry**, me ha gustado más la documentación de **poetry** por su simplicidad y claridad
Además podremos ajustarnos a las buenas prácticas de Python las cuales ya no hacen uso de requirements.txt sino de pyproject.toml.


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
  
  Se ha elegido la version de python 3.10 porque es la última versión estable, pero también funciona con la 3.6 que es la mínima que piden herramientas como invoke y poetry


  ## Explicación de la imagen docker desarrollada

Para la creación de la imagen se intentado seguir las mejores prácticas ([vease aqui](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)), lo primero que hacemos es crear un usuario para ejecutar las ordenes con dicho usuario y no con el superusuario, posteriormente copiamos los archivos pyproject.toml y poetry.lock en la imagen, ya que será necesario para que, cuando instalemos poetry y vayamos a instalar las dependencias, este sepa que herramientas debe instalar (pytest o invoke por ejemplo). Finalmente, ejecutamos los test a través del task runner invoke.



# Objetivo 6
  
## Versiones que se probarán de Python
Se probarán las versiones desde la 3.6 (porque es la versión minima que requieren las herramientas de la aplicación (invoke y poetry concretamente) ) a la 3.10 (por ser la la última versión estable actual de python)


## Integración Continua
  
Para comprobar que el proyecto funciona con diferentes versiones de python se van a usar 2 sistemas de integración continua (CI).
  
### Requisitos sistema de CI
Son aquellos criterios que se usarán para seleccionar a los principales sistemas candidatos para el proyecto.
Aquellos que no los cumplan no serán considerados como opción para el proyecto.

Requisitos principales:

* Se preferirá que el sistema de CI proporcione servidores propios para ejecutar los procesos.

* Que permita la ejecución en paralelo de estos procesos.

* Que sea de fácil de integrar a GitHub.

* Que sea gratuito.

Requisitos valorables:
  
* Que el periodo de prueba gratuito sea lo suficiente extenso como para poder terminar el proyecto

### Sistemas de CI encontrados ###

Necesitamos escoger 2 sitemas distintos, para ello se han explorado diversos sistemas de integración continua que cumplan con los requisitos de búsqueda. Concretamente **Travis**, **GitHub Actions**, **CircleCI**, **Azure Pipelines** y **Semaphore**.
  Hay que añadir que aquellos que se han probado son similares en cuanto a dificultad para integrar en Github, a excepción e las GHA que obviamente ha sido la más sencilla de realizar. Además todos son gratuitos y permiten paralelismo y hosting aunque de eso habrá ciertas diferencias que se tratarán más abajo específicamente.

* **Azure**: Desarrollado por Microsoft ofrece unas características muy tentadoras para proyectos open sourcce, y es que permite minutos ilimitados con hasata 10 parallel jobs gratuitos. Tambien tiene ofertas gratuitas para proyectos privados pero no tan tentadoras (1 parallel job gratuito y 1.800 minutos por mes).
O al menos eso era hasta que por el abuso del servicio, se redujo a 0 el nº de parallel jobs para repositorios públicos y privados, mas información pulsando [aquí](https://stackoverflow.com/questions/68033977/errorno-hosted-parallelism-has-been-purchased-or-granted). Ahora para solicitar que se reactive para nuestro proyecto hay que ponerse en contacto con ellos y es un proceso que lleva tiempo. Otra opción es ejecutarlo en local, pero no es lo que buscamos para el proyecto. Su configuración no ha sido muy laboriosa, ni ha hecho falca crearse una cuenta (ya que se usa la propia cuenta de Google).
**Nota: Este CI he llegado a probarlo (ejecutándo los pipelines en local).** 

* **Travis**: Travis fue el principal sistema por el que se optó al principio , ya que cumple con todos los requisitos propuestos y además es el que se tenía pensado usar en la asignatura. Sin embargo, presenta algunos problemas. Entre ellos, la necesidad de usar tarjeta de crédito para iniciar el sistema, además de que hace unos meses tuvieron problemas con una brecha de seguridad que expuso los "secrets" de miles de proyectos [véase aquí](https://arstechnica.com/information-technology/2021/09/travis-ci-flaw-exposed-secrets-for-thousands-of-open-source-projects/). Por dichos motivos es la opción menos tentadora, ya que tarjeta de crédito y vulnerabilidades no es que inspire mucha confianza.
  Dispone de 10.000 creditos en su versión gratuita (que aparentemente son 1.000 minutos si se usa una MV con Linux )
**Nota: Este CI NO he podido llegar a probarlo.** 

* **CircleCI**: Presenta ciertas ventajas, como la similitud a los Actions de Github, que ya usamos en el objetivo anterior, proporciona creditos más que suficientes y una configuración muy intuitiva, lo cual se agradece. Requiere que se habilite el [checks API](https://circleci.com/docs/2.0/enable-checks/) para que se puedan ver los resultados de la integración continua en Github. La única pega que le encuentro ha sido el setup, que ha sido laborioso de realizar.
Proporciona 30.000 creditos (6,000 minutos aparentemente) y hasta 30 trabajos en paralelo lo cual es lo mejor en comparación a las otras opciones
**Nota: Este CI he llegado a probarlo.** 

* **Semaphore**: Afirma ser más veloz que algunos de los principales sistemas de CI, haciendo una comparación sobre una web app con **GHA**, **CircleCI** y **Travis CI**. También se hace una comparación con las GHA en el siguiente [enlace](https://knapsackpro.com/ci_comparisons/semaphore-ci/vs/github-actions). 
No ha sido muy complicado de configurar aunque los templates que proporciona contienen algún que otro error (tal vez es porque estan desactualizados), pero se ha podido paliar gracias a que tiene una documentación bastante clara en comparación a Azure por ejemplo.
La única pega es la duración del período de prueba (14 días), pasado este tiempo quedaria limitado a 1 job a la vez (se pierde el paralelismo) y 1.300 minutos por lo que no es una buena idea a largo plazo.
**Nota: Este CI he llegado a probarlo.** 

* **GitHub Actions**: También cumple con los requisitos propuestos, además de que ya se conoce este sistema debido al objetivo anterior, es muy simple de usar y obviamente es la opción que tiene la "integración con GitHub" mas simple, ya que no requiere ninguna configuración previa para poder ver el resultado de los workflows.
 No hay limite en el número de minutos para proyectos open source como este.
**Nota: Este CI he llegado a probarlo.**  


 ### Sistemas CI escogidos y su uso: 

 Lo primero aclarar todo el trabajo realizado, ya había usado CircleCI y las GHA en la entrega anterior, pero como se ha pedido el uso de un CI distinto de estos he tenido que ampliar la búsqueda ya que no me convencía Semaphore por el breve periodo de prueba ni Travis, por no querer dejar la tarjeta bancaría. Entonces encontré AzureCI que cumplía con los requisitos de búsqueda y aparentemente iba a disponer de minutos ilimitados. Una vez que todo estuvo puesto a punto obtuve un error de Azure avisando de que no disponía de parallel jobs, que es el problema que ya he comentado arriba. Probándolo en local, funcionaba pero ahora se abría un dilema, CircleCI y GHA funcionan pero no puedo usarlas conjuntamente, Travis pide tarjeta, Azure solo se ejecuta en local (mientras que no se solicite el que se nos activen los parallel jobs) y Semaphore tiene solo 14 dias de prueba. 
 Dicho esto, creo que configurar 4 sistemas de CI es prueba suficiente de que se han probado diversas opciones, además de que 3 de ellos (CircleCI, GHA y Semaphore) están operativos para llevar a cabo las tareas con los requisitos de búsqueda que se piden (no incluyo a Azure porque había que ponerse en contacto con ellos para que nos permitan ejecutar en sus servidores y no en local) por lo que no creo que sea necesario seguir buscando.
 Pero hay que tomar una decisión sobre que hacer. Personalmente preferiría seguir con CircleCI pero debido a la condición para pasar el objetivo no me queda otra que usar Semaphore, a pesar de que no es una opción a largo plazo, pero Travis no es mejor opción para mi y para activar lo de Azure lleva un tiempo que no dispongo.
 Por lo que, aunque ahora se escoja Semaphore, en un futuro se tendría que elegir entre Azure Pipeline y CircleCI. Azure tiene además más servicios que son muy fáciles de integrar una vez ya asociada la cuenta de Google con GitHub (como boards para sprints y algunas cosas más), por lo que puede ser una opción interesante y habría que valorar si se prefieren estas características por encima de la superioridad en paralelismo que nos ofrece CircleCI. 
 ¿Y por qué usar GHA por encima de CircleCI?, básicamente porque el poder trabajar sin preocuparse del número de minutos es lo mejor para poder trabajar tranquilo, además de que hay muchos Actions ya creadas que nos pueden facilitar el trabajo que podamos llegar necesitar (como fue el caso de actualizar el readme y publicar imagenes en DockerHub).
  
  * **Semaphore** : Lo usaremos para testear las versiones de python intermedias entre la 3.6 y 3.10 resolviendo así el issue [#30](https://github.com/Parka015/serie-motion/issues/30).

  * **GHA** : Se han usado para probar las 2 versiones de python (mínima y máxima) con el contenedor docker del objetivo anterior resolviendo así el issue [#31](https://github.com/Parka015/serie-motion/issues/31).
