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
<br>

### Setup
```sh
$ git clone https://github.com/oscarsandford/scripts.git
```

### Install Scripts
```sh
# Install all scripts in ./scripts to /usr/local/bin
$ sudo ./install.sh -a
# or install a specific script.
$ sudo ./install.sh script.py
```
Scripts are installed to `/usr/local/bin`, such that they can be executed by the shell anywhere in the file system.
<br>

Some scripts require non-standard libraries, which must be installed with a package library. If you have `pip` you can simply install all the dependencies with
```sh
$ pip install -r requirements.txt
```
<hr>

## Uninstall
```sh
# Uninstall all scripts in ./scripts to /usr/local/bin
$ sudo ./uninstall.sh -a
# or uninstall a specific script.
$ sudo ./uninstall.sh script.py
```
<hr>

## Usage
Execute **any** script with its arguments from **any directory** in a shell terminal. 
Find script-specific usage with 
```sh
$ script.py -h
```
I recommend adding bash aliases for the scripts.
