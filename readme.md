A collection of scripts I've written for quality of life and productivity boosts.

## Table of Contents
1. Requirements
2. Setup and Installation
3. Uninstallation
4. Usage
<hr>

## Requirements
- Linux / Bourne Shell
- Python 3
<hr>

## Installation

### Setup
```sh
$ git clone https://github.com/oscarsandford/scripts.git
# If necessary, give execute permissions to the installer and uninstaller.
$ chmod 777 install.sh uninstall.sh
```

### Install Scripts
```sh
# Install all scripts in ./scripts to /usr/local/bin
$ ./install.sh --all
# or install a specific script.
$ ./install.sh script.py
```
Scripts are installed to `/usr/local/bin`, such that they can be executed by the shell anywhere in the file system.
<hr>

## Uninstall
```sh
# Uninstall all scripts in ./scripts to /usr/local/bin
$ ./uninstall.sh --all
# or uninstall a specific script.
$ ./uninstall.sh script.py
```
<hr>

## Usage
Execute **any** script with its arguments from **any directory** in a shell terminal. For example:
```sh
$ script.py [args...]
```