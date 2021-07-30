#!/bin/sh

Install() {
	# Check if file exists
	if [ -f "scripts/$1" ]; then
		echo "Installing $1 in /usr/local/bin/"
		chmod 777 scripts/$1
		sudo cp scripts/$1 /usr/local/bin/
		echo "Done."
		echo "You may type $1 anywhere in the filesystem to execute."
	else 
		echo "[!] File does not exist."
	fi
}

InstallAll() {
	# Installs all scripts in ./scripts to the local bin
	for fname in scripts/*; do 
		echo "Installing $fname in /usr/local/bin/"
		chmod 777 $fname
		sudo cp $fname /usr/local/bin/
	done
	echo "Done."
}

# Argument count check
if [ $# -ne 1 ]; then
	echo "[!] usage: "
	echo " ./install.sh script.py"
	echo "        (install script.py)"
	echo " ./install.sh --all"
	echo "        (install all scripts)"
	exit 1
fi

if [ $1 = "-a" ]; then
	InstallAll
else
	Install $1
fi
