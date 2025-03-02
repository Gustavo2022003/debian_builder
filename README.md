<img src="assets/images/debianbuilder-logo-rounded.png">

# Debian Builder

**Debian Builder** is a open-source tool designed to simplify the process of building and managing Debian packages. It allows users to create `.deb` packages from Python scripts, convert Python files into executable binaries, and handle package installation, uninstallation, and reinstallation. With this tool, developers can easily automate common tasks related to packaging, such as setting executable permissions, managing dependencies, and rebuilding packages. The tool supports a variety of options, including building, installing, uninstalling, and fully rebuilding packages, making it a versatile utility for Debian-based systems.

## Features

- **Build Debian packages** from source files
- **Convert Python scripts** to executable files
- **Install, uninstall, and reinstall** Debian packages
- **Supports full rebuilds**, removing old packages before building new ones

## Prerequisites

- Python 3
- Debian-based system (Ubuntu, Debian, etc.)
- `dpkg` and `dpkg-deb` installed

## Installation

1. To get started with **Debian Builder**, donwload the package from [this](./Debian_builder.deb) directory
2. Install the package:
  ```bash
  dpkg -i Debian_builder.deb
  ```
3. Check the installation:
  ```bash
  debian-builder --version
  ```

## Comandos do Debian Builder

| Comando                 | Descrição |
|-------------------------|-----------|
| `-b`, `--build`        | Constrói o pacote Debian (`.deb`). |
| `-p`, `--path` `<caminho>` | Especifica o diretório do pacote. |
| `-n`, `--name` `<nome>` | Define o nome do pacote. |
| `--reinstall`          | Desinstala e reinstala o pacote. |
| `-u`, `--uninstall`    | Desinstala o pacote Debian especificado. |
| `-f`, `--fullbuild`    | Remove o `.deb` existente, converte o arquivo `.py`, desinstala, cria um novo pacote e instala novamente. |
| `-c`, `--convert`      | Converte um arquivo `.py` para um arquivo executável. |
| `-o`, `--output` `<caminho>` | Define o diretório de saída para o pacote gerado. |
| `-v`, `--version`      | Exibe a versão do Debian Builder. |

## Exemplos de Uso:

### 1. Construir um pacote Debian:
```sh
python3 builder.py --build --path /meu/pacote --name meu_pacote
```

### 2. Construir um pacote Debian e mover para um diretório específico:
```sh
python3 builder.py --build --path /meu/pacote --name meu_pacote --output /destino
```

### 3. Converter um arquivo `.py` para executável:
```sh
python3 builder.py --convert --path /caminho/script.py
```

### 4. Desinstalar um pacote:
```sh
python3 builder.py --uninstall --name meu_pacote
```

### 5. Realizar um build completo (recompilar, desinstalar, reinstalar):
```sh
python3 builder.py --fullbuild --path /meu/pacote --name meu_pacote
```

### 6. Reinstalar um pacote:
```sh
python3 builder.py --reinstall --path /meu/pacote --name meu_pacote
```

### 7. Exibir a versão do Debian Builder:
```sh
python3 builder.py --version
```
