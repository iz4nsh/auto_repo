#!/bin/bash

# Asegúrate de que el script se esté ejecutando con privilegios de superusuario
if [[ $EUID -ne 0 ]]; then
    echo "Este script debe ejecutarse como superusuario (sudo)." 
    exit 1
fi

# Define la ubicación del archivo
DEST_PATH="/usr/local/bin/repo"

# Verifica si el archivo existe en la ubicación de destino
if [[ -f "$DEST_PATH" ]]; then
    echo "Eliminando $DEST_PATH..."
    rm "$DEST_PATH"
    echo "¡Desinstalación completada! El archivo 'repo' ha sido eliminado de /usr/local/bin."
else
    echo "No se encontró el archivo $DEST_PATH. El programa ya podría estar desinstalado o nunca instalado."
fi
