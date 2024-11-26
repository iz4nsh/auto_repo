# Subir Archivos a GitHub con PyGithub

Este script automatiza el proceso de subir archivos y carpetas a un repositorio de GitHub utilizando la librería `PyGithub`. Permite crear repositorios, comprobar si existen y subir múltiples archivos de manera sencilla, manteniendo la estructura de carpetas si es necesario.

## Características

- **Automatización**: Crea repositorios en GitHub automáticamente si no existen.
- **Subida de Archivos**: Sube archivos individuales o directorios completos, preservando la estructura de carpetas.
- **Soporte de Repositorios Privados**: Permite crear repositorios privados si es necesario.
- **Fácil de usar**: Configuración sencilla con un archivo de token de GitHub o usando variables de entorno.
- **Compatible con múltiples archivos y carpetas**: Puedes subir tanto archivos individuales como carpetas completas con una sola ejecución.

## Requisitos

- Python 3.x
- [PyGithub](https://pypi.org/project/PyGithub/) - Para interactuar con la API de GitHub.
  ```bash
   pip3 install PyGithub

## Instalación

1. Clona el repositorio o descarga los archivos a tu máquina local.

   ```bash
   git clone https://github.com/tuusuario/nombre-del-repositorio.git
   cd nombre-del-repositorio
