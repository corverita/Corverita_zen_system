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

# Primeros pasos

- Entraremos en nuestra conexión frontend con nuestro superusuario, para poder comenzar a gestionar detalles de primeras implementaciones.
- Registraremos un perfil de usuario, para poder utilizar el sistema con los roles y permisos personalizados.
- Una vez registremos un perfil de usuario, nos asignaremos el rol de Admin, para tener total libertad de permisos y acciones, así como podemos habilitarle a otra gente sus roles.

Ya a partir de aquí tendremos todo el sistema completamente listo y libre.


# Pruebas Back End

## Introducción
La prueba tiene como objetivo evaluar tus conocimientos acerca de los distintos procesos que se llevan a cabo para poder crear experiencias positivas a nuestros usuarios, que les ayuden a cumplir con sus tareas y que generen un impacto en él para que quiera regresar. Todo está basado en un caso hipotético usado para estos fines exclusivamente. Lee el documento completo antes de iniciar con tu trabajo.

Cuentas con 5 días para hacer la entrega de la prueba técnica y posteriormente nos pondremos en contacto contigo para agendar la presentación de 30 minutos.

## Proyecto:
El proyecto es para un público principalmente femenino en el ámbito profesional con una edad entre 25 y 35 años. Esta persona se desarrolla en el ámbito empresarial y le gusta que los procesos que tiene que hacer sean muy claros, rápidos y puntuales.

Pueden usar el sistema desde su computadora, tableta o teléfono, aunque principalmente se usará en la computadora, debe poder realizar las tareas en los demás entornos.

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

Derivado de lo anterior, nuestra empresa, La Más Exitosa S. A. de C.V. ha decidido hacer un sistema que ayude a resolver estas necesidades y para ello te está buscando como el genio que le ayudará a materializarlo.

El sistema debe controlar los inventarios de productos que se tienen disponibles para la venta al público, se tienen más de 100 productos y nuestro usuario debe ser capaz de poder identificar cuando hay que resurtir alguno y poder entregar reportes de las existencias, entradas y salidas de los productos bajo demanda.

## Requerimientos Técnicos:
- Sistema desarrollado en Django.
- Base de datos en postgres
- Uso de paquetes y librerías para desarrollo más sencillo y ágil.
- Bajo consumo de recursos computacionales.
- Tiempos de carga menores a 3 segundos.

## Requerimientos Funcionales:
A continuación, te ponemos una lista de distintos requerimientos funcionales, **NO esperamos que los hagas todos**, elige los que quieras **(al menos 6)**, con los que creas que puedes presentarnos una propuesta de valor impactante, si hay alguna otra sección que quieras agregar que no esté en la lista también es bienvenida.

### Módulos del Back End
- Se requiere un módulo de usuarios.
- Se requiere un módulo de permisos.
- Se requiere un módulo para el perfil del usuario.
- Se requiere un módulo para los productos.
- Se requiere un mecanismo de conexión con algún Front End.
- Se requiere que se pueda consumir información de la base de datos desde otros sistemas.
- Se requiere un módulo para guardar y enviar notificaciones del sistema.
- Se requiere un mecanismo para enviar mensajes de alerta en pantalla con distintos mensajes dependiendo del contexto de lo que esté haciendo el usuario.
- Se requiere un módulo de ayuda con documentos y videotutoriales
- Se requiere un módulo para levantamiento de tickets
- Se requiere un mecanismo para permitir registrar las entradas y salidas de inventario.

### Pantallas que tendrá el Front End (Informativo, no es necesario realizar nada de aquí a menos que así lo desees.)
- Se requiere un apartado para ingresar.
- Se requiere un apartado para registrarse.
- Se requiere un apartado para editar mis preferencias.
- Se requiere un apartado con información general en forma de tablero (dashboard).
- Se requiere un apartado para ver de manera general todos los elementos (considerar más de 100 elementos).
- Se requiere un apartado para ver el detalle de un elemento.
- Se requiere un apartado para cargar/editar información de los elementos.
- Se requiere un apartado para realizar búsquedas de información o secciones.
- Se requiere un apartado para obtener reportes.
- Se requiere un apartado para recibir notificaciones.
- Se requiere que el sistema tenga alertas informativas.
- Se requiere que el sistema tenga diálogos de confirmación.
- Se requiere un apartado para manejar permisos.
- Se requiere un apartado para que el usuario pueda recibir ayuda.
- Se requiere un apartado para que el usuario pueda resolver sus dudas de forma autodidacta.

## Criterios mínimos de evaluación:
**Desarrollo**

- Tiempo de carga
- Utilización de recursos en consultas y operación
- Rendimiento
- Orden en el código
- Reutilización de código
- Documentación
- Pruebas unitarias
- Diseño de la base de datos
- API

## Entregables:
En una presentación de no más de 15 minutos, queremos ver:

**Introducción**:

- Motivaciones y fundamentos de las técnicas y tecnologías que utilizaste.

**Modelo de base de datos**:

- Saber por qué ese es el modelo más óptimo que elegiste

**Sistema**:

- Ya sea por medio de postman, pantallas simples (sin diseño) o por medio de Django Admin, nos muestres cómo funciona el sistema y las capacidades que le desarrollaste.

Al final tendremos otros 15 minutos para preguntas y respuestas.

Tienes total libertad de usar las herramientas y tecnologías que desees para cumplir con el objetivo (todo basado principalmente en Django), lo que nos interesa saber, son tus conocimientos en la materia.
