#/bin/sh

if [ $# -ne 1 ]; then
	echo "[!] usage: ./install.sh <script-name>"
	exit 1
fi

sudo cp $1 /usr/local/bin/
echo "Done: $1 installed in /usr/local/bin/"
echo "Type $1 in the shell anywhere in the filesystem to execute."