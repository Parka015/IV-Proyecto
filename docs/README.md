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

## Framework de tests : pytest

Para el framework de test en python, he encontrado a **Unittest** y a **Pytest**.
Unittest es el marco de tests establecido en python de forma predeterminada. Para usarlo, creamos clases que se derivan del módulo unittest.TestCase.
Pytest tiene ricas características incorporadas que requieren menos código en comparación con unittest. En el caso de unittest, tenemos que importar un módulo, crear una clase y luego definir funciones de prueba dentro de la clase. Pero en el caso de pytest, tenemos que definir las funciones y asserts dentro de ellas.
Por simplicidad he decidido hacer uso de pytest ya que no hay ninguna estructura compleja en el proyecto que requiera hacer uso de una clase de test.

## Justificación de uso de los principios F.I.R.S.T

He desarrollado un test para la regresión lineal, que comprueba que se devuelve un numero entre 0 y 5 tal y como se especifica en el M1, que sigue los principios F.I.R.S.T, porque es un test **rápido**, ya que usamos numpy para agilizar los cálculos y usamos un conjunto de datos muy reducido, **independiente**, porque no depende de ningún otro test, **repetible** porque se puede replicar en cualquier otro ordenador ya que todo lo que se necesita viene en el proyecto. Responde con una assert (o pasa o no pasa) y se ha creado de manera independiente a la implementación de la regresión lineal
