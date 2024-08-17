#!/bin/bash

# Espera a que la base de datos esté disponible
echo "Esperando a que la base de datos esté disponible..."
while ! nc -z db 5432; do
  sleep 1
done

echo "La base de datos está disponible."

# Aplicar migraciones a la base de datos
echo "Aplicando migraciones..."
python manage.py makemigrations
python manage.py migrate

# Cargar datos de los dumps
echo "Cargando datos de los dumps..."
python manage.py loaddata fixtures/estatus.json
python manage.py loaddata fixtures/prioridad.json
python manage.py loaddata fixtures/tipo_movimiento.json
python manage.py loaddata fixtures/permisos.json
python manage.py loaddata fixtures/rol.json

# Iniciar el servidor de desarrollo
echo "Iniciando el servidor de desarrollo..."
exec python manage.py runserver 0.0.0.0:8000