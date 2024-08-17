#!/bin/bash

# Ejecutar el script setUp.sh
/code/setUp.sh

# Ejecutar el comando por defecto (manage.py)
exec "$@"