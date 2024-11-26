#!/bin/bash

# Asegúrate de que el script se esté ejecutando con privilegios de superusuario
if [[ $EUID -ne 0 ]]; then
    echo "Este script debe ejecutarse como superusuario (sudo)." 
    exit 1
fi

# Define las ubicaciones de los archivos
SRC_FILE="repo.py"
DEST_PATH="/usr/local/bin/repo"

# Verifica si el archivo existe en la ubicación actual
if [[ ! -f "$SRC_FILE" ]]; then
    echo "El archivo $SRC_FILE no se encuentra en el directorio actual."
    exit 1
fi

# Copiar el archivo a /usr/local/bin y renombrarlo como 'repo'
echo "Copiando $SRC_FILE a $DEST_PATH..."
cp "$SRC_FILE" "$DEST_PATH"

# Asegúrate de que el archivo copiado tenga permisos de ejecución
echo "Asignando permisos de ejecución a $DEST_PATH..."
chmod +x "$DEST_PATH"

# Confirmación final
echo "¡Instalación completada! Ahora puedes ejecutar el programa con el comando 'repo'."
