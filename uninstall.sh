#!/bin/sh

Uninstall() {
	# Check if file exists
	if [ -f "scripts/$1" ]; then
		echo "Removing $1 from /usr/local/bin/"
		sudo rm /usr/local/bin/$1
		echo "Done."
	else 
		echo "[!] File does not exist."
	fi
}

UninstallAll() {
	# Removes all scripts in ./scripts from the local bin
	for fname in scripts/*; do 
		script_name=${fname##*/}
		echo "Removing $script_name from /usr/local/bin/"
		sudo rm /usr/local/bin/$script_name
	done
	echo "Done."
}

# Argument count check
if [ $# -ne 1 ]; then
	echo "[!] usage: "
	echo " ./uninstall.sh script.py"
	echo "        (removes script.py)"
	echo " ./uninstall.sh --all"
	echo "        (removes all scripts)"
	exit 1
fi

if [ $1 = "--all" ]; then
	UninstallAll
else
	Uninstall $1
fi
