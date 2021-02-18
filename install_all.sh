#/bin/sh
for fname in "."/*.py; do 
	echo "Installing $fname in /usr/local/bin/"
	sudo cp $fname /usr/local/bin/
done
echo "Done."