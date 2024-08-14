# Usar una imagen base oficial de Python
FROM python:3.10

# Evitar el buffering de salida de Python
ENV PYTHONUNBUFFERED=1

# Crear y establecer el directorio de trabajo en el contenedor
WORKDIR /code

# Instalar netcat-openbsd
RUN apt-get update && apt-get install -y netcat-openbsd

# Copiar el archivo de requirements al directorio de trabajo
COPY requirements.txt /code/

# Instalar requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . /code/

# Copiar el script entrypoint y el script de inicio
COPY entrypoint.sh /code/entrypoint.sh
COPY start.sh /code/start.sh

# Hacer que los scripts sean ejecutables
RUN chmod +x /code/entrypoint.sh /code/start.sh

# Establecer el entrypoint
ENTRYPOINT ["/code/entrypoint.sh"]

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "inventory.wsgi:application"]