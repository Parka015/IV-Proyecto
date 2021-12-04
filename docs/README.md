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

  
## Test-Runner : Pytest
  
Para el proyecto estamos buscando un test runner para ejecutar unos test simples que validen la lógica de negocio. En principio todo se puede testear con asserts o excepciones ya incluidas en python por dicho motivo, no necesitamos una librería de aserciones como puede ser **Unittest**.
  
He encontrado opciones como [test-runner](https://pypi.org/project/test-runner/), descartada por documentación escasa, o **nosetests** (ya en desuso). Este último tiene un sucesor **nose2** pero se encuentra en el mismo estado que **nosetests**

Al final he elegido Pytest ya que es un test-runner bastante usado con bastante documentación y soporte. Para usarlo tenemos que crear un archivo de nombre test_*.py o *_test.py y dentro de este crear funciones que empiecen por test_*. De esta manera y con las excepciones de python podemos ejecutar todos los test de manera muy simple desde nuestro task-runner (invoke).

## Justificación de uso de los principios F.I.R.S.T

He desarrollado un test para la regresión lineal, que comprueba que se devuelve un numero entre 0 y 5 tal y como se especifica en el M1, que sigue los principios F.I.R.S.T, porque es un test **rápido**, ya que usamos numpy para agilizar los cálculos y usamos un conjunto de datos muy reducido, **independiente**, porque no depende de ningún otro test, **repetible** porque se puede replicar en cualquier otro ordenador ya que todo lo que se necesita viene en el proyecto. Responde con una assert (o pasa o no pasa) y se ha creado de manera independiente a la implementación de la regresión lineal
