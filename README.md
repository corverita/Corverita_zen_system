Este es un documento que muestra paso por paso cómo levantar el sistema.

# Primeros Pasos
De inicio es necesario instalar python 3.10, esto debido a que el ejemplo fue desarrollado con base a este.

Tras tenerlo instalado, podemos proceder a crear un ambiente virtual por medio de la instalación del mismo

Para esto ejecutaremos el siguiente comando de python, para instalar el ambiente virtual.
pip install venv

Entonces crearemos el ambiente virtual que utilizaremos
python -m venv env

Para el caso de Windows, el sistema donde fue desarrollado este sistema utilizaremos el siguiente comando
env/Scripts/activate

Una vez que estemos con el ambiente activo, podremos instalar nuestras dependencias en el siguiente paso

# Instalación de recursos y dependencias

Para instalar los requerimientos del sistema utilizaremos el siguiente comando
pip install -r requirements.txt