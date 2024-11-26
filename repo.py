#!/usr/bin/env python3

import os
import sys
import github
import argparse

# Función para obtener el token de GitHub desde un archivo o variable de entorno
def obtener_token():
    token = os.getenv("GITHUB_TOKEN")
    if token:
        return token
    home_dir = os.path.expanduser("~")
    token_file = os.path.join(home_dir, ".github_token")

    if not os.path.exists(token_file):
        print("No se encontró un token de GitHub guardado.")
        token = input("Por favor, ingresa tu token de GitHub: ")
        with open(token_file, "w") as f:
            f.write(token)
        print("Token guardado exitosamente.")
    else:
        with open(token_file, "r") as f:
            token = f.read().strip()
        print("Token cargado exitosamente.")
    return token

# Función para obtener el usuario de GitHub usando PyGithub
def obtener_usuario_github(g):
    user = g.get_user()
    return user.login

# Función para verificar si el repositorio ya existe en GitHub
def repositorio_existe(g, nombre_repo):
    user = g.get_user()
    try:
        repo = user.get_repo(nombre_repo)
        return True
    except github.GithubException as e:
        if e.status == 404:
            return False
        else:
            print(f"Error al verificar el repositorio: {e}")
            return False

# Función para crear el repositorio en GitHub usando PyGithub
def crear_repositorio(g, nombre_repo, descripcion, privado=False):
    user = g.get_user()
    repo = user.create_repo(
        nombre_repo,
        description=descripcion,
        private=privado  # Repositorio privado si 'privado' es True
    )
    print(f"Repositorio '{nombre_repo}' creado correctamente.")

# Función para subir un archivo específico a un repositorio
def subir_archivo_a_github(g, nombre_repo, archivo_path, ruta_repo, commit_message="Subiendo archivo"):
    # Relativa la ruta dentro del repositorio
    archivo_relativo = os.path.join(ruta_repo, os.path.basename(archivo_path))
    
    with open(archivo_path, "rb") as f:
        contenido_archivo = f.read()

    user = g.get_user()
    repo = user.get_repo(nombre_repo)

    try:
        archivo = repo.get_contents(archivo_relativo)
        # Si el archivo existe, lo actualizamos
        repo.update_file(archivo.path, commit_message, contenido_archivo, archivo.sha)
        print(f"Archivo '{archivo_relativo}' actualizado.")
    except github.GithubException:
        # Si el archivo no existe, lo creamos
        repo.create_file(archivo_relativo, commit_message, contenido_archivo)
        print(f"Archivo '{archivo_relativo}' subido al repositorio.")

# Función para obtener todos los archivos de una carpeta, preservando la estructura
def obtener_archivos_de_carpeta(carpeta):
    archivos = []
    for root, dirs, files in os.walk(carpeta):
        for file in files:
            archivos.append(os.path.join(root, file))
    return archivos

# Función principal
def main():
    parser = argparse.ArgumentParser(description="Sube archivos o carpetas a un repositorio en GitHub.")
    
    parser.add_argument("archivo_o_carpeta", nargs='+', help="Ruta de uno o más archivos o carpetas.")  # Ahora acepta varios archivos o carpetas
    parser.add_argument("-r", "--repositorio", help="Nombre del repositorio existente al cual añadir los archivos.")
    parser.add_argument("-d", "--descripcion", default="Repositorio creado automáticamente.", help="Descripción del repositorio (opcional).")
    parser.add_argument("--private", action="store_true", help="Crea el repositorio como privado.")

    args = parser.parse_args()

    repositorio = args.repositorio
    descripcion = args.descripcion
    archivos = []  # Lista para almacenar los archivos

    # Procesar cada archivo o carpeta
    for item in args.archivo_o_carpeta:
        if os.path.isdir(item):
            # Si es una carpeta, obtenemos todos los archivos dentro de ella
            archivos.extend(obtener_archivos_de_carpeta(item))
        else:
            archivos.append(item)  # Agregar archivo individual

    # Si no se pasa un repositorio, se crea uno nuevo con el nombre del primero de los archivos o carpetas
    if not repositorio:
        if archivos:
            # Usar el nombre del primer archivo o carpeta como el nombre del repositorio
            repositorio = os.path.splitext(os.path.basename(archivos[0]))[0]
        else:
            print("Error: No se pudo determinar el nombre del repositorio.")
            sys.exit(1)

    # Verificar si el repositorio existe
    token_github = obtener_token()
    g = github.Github(token_github)

    # Si el repositorio no existe, crearlo
    if repositorio_existe(g, repositorio):
        print(f"El repositorio '{repositorio}' ya existe. Procediendo a subir los archivos...")
    else:
        crear_repositorio(g, repositorio, descripcion, privado=args.private)

    # Subir cada archivo al repositorio
    for archivo_path in archivos:
        if os.path.isdir(archivo_path):
            # Si es una carpeta, subimos los archivos dentro de ella en una carpeta dentro del repositorio
            ruta_repo = os.path.basename(archivo_path)  # El nombre de la carpeta se usará como nombre de la subcarpeta en el repo
            for file in obtener_archivos_de_carpeta(archivo_path):
                subir_archivo_a_github(g, repositorio, file, ruta_repo)
        else:
            # Si es un archivo individual, simplemente lo subimos al repositorio
            subir_archivo_a_github(g, repositorio, archivo_path, "")

if __name__ == "__main__":
    main()
