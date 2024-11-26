# Upload Files to GitHub with PyGithub

This script automates the process of uploading files and folders to a GitHub repository using the `PyGithub` library. It allows you to create repositories, check if they exist, and upload multiple files easily, maintaining folder structure if needed.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Configuration](#configuration)
   - [How to create a GitHub Token](#how-to-create-a-github-token)
5. [Usage](#usage)
6. [Future Integrations](#future-integrations)

## Features

- **Automation**: Automatically creates GitHub repositories if they do not exist.
- **File Upload**: Uploads individual files or entire directories, preserving folder structure.
- **Support for Private Repositories**: Allows creating private repositories if needed.
- **Easy to Use**: Simple setup with a GitHub token file or using environment variables.
- **Supports Multiple Files and Folders**: You can upload both individual files and entire folders with a single execution.

## Requirements

- Python 3.x
- [PyGithub](https://pypi.org/project/PyGithub/) - For interacting with the GitHub API.

  To install `PyGithub`, run:

  ```bash
  pip3 install PyGithub

## Installation

1. Clone the repository or download the files to your local machine.

   ```bash
   git clone https://github.com/iz4nsh/auto_repo
   cd auto_repo
   chmod +x install_repo.sh
   sudo ./install_repo.sh
   
## Configuration

For the script to work correctly, you will need a **GitHub personal access token**. This token will be used to authenticate requests to the GitHub API.

### How to Create a GitHub Token

1. **Log in to GitHub**: Go to [GitHub](https://github.com) and log into your account.
2. **Access Settings**: Click on your profile picture in the top right corner and select **"Settings"**.
3. **Generate a Token**:
   - In the left sidebar, select **"Developer settings"**.
   - Then select **"Personal access tokens"**.
   - Click on **"Generate new token"**.
4. **Configure token permissions**:
   - Give your token a name (e.g., `file-upload-script`).
   - Select the necessary permissions. For this script, make sure to check at least the following:
     - **repo**: full access to both private and public repositories.
     - **workflow**: if you plan to interact with GitHub Actions.
   - Click **Generate token**.
5. **Save the token**: Copy the generated token and store it in a safe place. **Do not share it with anyone**.
### Token Configuration

Once you have the token, you can configure it in two ways:

#### Option 1: Use an Environment Variable

You can set the `GITHUB_TOKEN` environment variable on your system like this:

```bash
export GITHUB_TOKEN="your-github-token"

```
## Usage
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
## Future Integrations
I plan to introduce a feature to implement AI in the program. With it, a description and a Readme.md can be generated automatically. It will work for small repositories but will be a great help in documenting the code you upload automatically. I'm already working on it
