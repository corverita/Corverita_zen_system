# Notas
Sólo como nota adicional y para dejar en claro los módulos que realicé para la prueba backend se enlistan los módulos implementados:

Usuarios
Perfiles de usuario
Productos
Tickets
Entradas y salidas del inventario
Mecanismo de conexión con algún front-end
Permisos


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

# Ejecución del proyecto

Una vez que tengamos todas las dependencias, entonces podremos ejecutar el comando
docker-compose up -d

Y podremos revisar que levantaremos las instancias correspondientes como lo son la base de datos postgres y el servicio web de manera local.

Una vez que tengamos corriendo el proyecto en docker, entonces ejecutaremos el siguiente comando para crear un super usuario
python manage.py createsuperuser

Nos solicitará un usuario, un correo y una contraseña, estas serán tus credenciales.

# Primeros pasos tras ejecución del setup del proyecto

- Entraremos en nuestra conexión frontend con nuestro superusuario, para poder comenzar a gestionar detalles de primeras implementaciones.
- Registraremos un perfil de usuario, para poder utilizar el sistema con los roles y permisos personalizados.
- Una vez registremos un perfil de usuario, nos asignaremos el rol de Admin, para tener total libertad de permisos y acciones, así como podemos habilitarle a otra gente sus roles.

Ya a partir de aquí tendremos todo el sistema completamente listo y libre.

Los **pain points** que conocemos de la persona son:
- No tener información de manera rápida.
- Poder acceder al sistema únicamente desde su oficina.
- No poder ejecutar los procesos de forma rápida.
- No tener claridad en qué parte del proceso está o si este ya terminó o falló.

Los **deseos** que conocemos de la persona son:
- Tranquilidad y seguridad.
- Tener el control y saber qué es lo que está pasando con el sistema.
- Libertad.
- Sentirse acompañada y atendida.
- Tener tiempo libre.

## Requerimientos Técnicos:
- Sistema desarrollado en Django.
- Base de datos en postgres
- Uso de paquetes y librerías para desarrollo más sencillo y ágil.
- Bajo consumo de recursos computacionales.
- Tiempos de carga menores a 3 segundos.
