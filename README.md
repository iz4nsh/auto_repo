# Subir Archivos a GitHub con PyGithub

Este script automatiza el proceso de subir archivos y carpetas a un repositorio de GitHub utilizando la librería `PyGithub`. Permite crear repositorios, comprobar si existen y subir múltiples archivos de manera sencilla, manteniendo la estructura de carpetas si es necesario.

## Índice

1. [Características](#características)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Configuración](#configuración)
   - [Cómo crear un Token de GitHub](#cómo-crear-un-token-de-github)
5. [Uso](#uso)
6. [Futuras integraciones](#futuras-integraciones)
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
## Configuración

Para que el script funcione correctamente, necesitarás un **token de acceso personal de GitHub**. Este token se utilizará para autenticar las peticiones hacia la API de GitHub.

### Cómo crear un Token de GitHub

1. **Iniciar sesión en GitHub**: Dirígete a [GitHub](https://github.com) y accede a tu cuenta.
2. **Acceder a la configuración**: Haz clic en tu foto de perfil en la esquina superior derecha y selecciona **"Settings"** (Configuración).
3. **Generar un token**:
   - En el menú lateral izquierdo, selecciona **"Developer settings"**.
   - Luego selecciona **"Personal access tokens"**.
   - Haz clic en **"Generate new token"**.
4. **Configurar permisos del token**:
   - Asigna un nombre al token (por ejemplo, `subida-archivos-script`).
   - Selecciona los permisos necesarios. Para este script, asegúrate de marcar al menos los siguientes permisos:
     - **repo**: acceso completo a repositorios privados y públicos.
     - **workflow**: si planeas interactuar con GitHub Actions.
   - Haz clic en **Generate token**.
5. **Guardar el token**: Copia el token generado y guárdalo en un lugar seguro. **No lo compartas con nadie**.

### Configuración del Token

Una vez que tengas el token, puedes configurarlo de dos maneras:

#### Opción 1: Usar la variable de entorno

Puedes configurar la variable de entorno `GITHUB_TOKEN` en tu sistema de la siguiente manera:

```bash
export GITHUB_TOKEN="tu-token-de-github"
```
#### Opción 2: Usar un archivo de token

Coloca el token en un archivo llamado .github_token en tu directorio home (~). Si el archivo no existe, el script te pedirá que lo ingreses manualmente.

## Uso

```
usage: script.py [-h] [--repositorio REPOSITORIO] [--descripcion DESCRIPCION] [--private] archivo_o_carpeta [archivo_o_carpeta ...]
  
Sube archivos o carpetas a un repositorio en GitHub.

positional arguments:
  archivo_o_carpeta     Ruta de uno o más archivos o carpetas.

optional arguments:
  -h, --help            Show this help message and exit.
  --repositorio REPOSITORIO
                        Nombre del repositorio (si no se proporciona, se crea uno nuevo con el nombre del archivo o carpeta).
  --descripcion DESCRIPCION
                        Descripción del repositorio (opcional).
  --private             Crea el repositorio como privado.
```
## Futuras integraciones
En un futuro implementare una función para generar archivos readme.md de forma automatizada, asi como una descripción. Estoy ya trabajando en ello.
