#!/usr/bin/env python3

"""
oes-oph.py
Order Photos

On execution, type the names of the subdirectories that will have 
their contents updated to be an incremented integer concatenated 
to the name of the subdirectory.

As an example, consider the folder "alaska":

alaska
 |-- boat.jpg
 |-- mountains.jpg
 |-- river.png
 |-- wildlife.jpg

Executing `oes-oph.py -d alaska changes its contents to`

alaska
 |-- alaska_1.jpg
 |-- alaska_2.jpg
 |-- alaska_3.png
 |-- alaska_4.jpg

Oscar Sandford
Originally created: 2020-10-14
"""

import os
import argparse

# Renames all files in "./name/" to "./name/name_<i>.<ext>"
def rename(name, path):
	try:
		for i, filename in enumerate(os.listdir(path)):
			if "desktop" not in filename:
				dst = path + name + "_" + str(i)
				if ".jpg" in filename:
					dst += ".jpg"
				elif ".png" in filename:
					dst += ".png"
				else:
					dst += ".jpg"
				src = path + filename
				print(src, "-->", dst)
				os.rename(src, dst)
	except Exception as e:
		exit("[!] Something went wrong: "+str(e)+"\nExiting...")

# Receive directories and do processes depending on args
def receive(args, dirs):
	if not args.noupdate:
		for d in dirs:
			path = d + "/"
			print("Updating ...")
			rename("tmp", path)
			print("Renaming ...")
			rename(d, path)
	else:
		for d in dirs:
			path = d + "/"
			rename(d, path)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--directories", action="extend", nargs="+", type=str, required=True, help="Specify folder(s) to target.")
	parser.add_argument("-y", "--yestoall", action="store_true", help="Release without asking for further user input.")
	parser.add_argument("-nu", "--noupdate", action="store_true", help="Does not reset all filenames to incremental order if specified.")

	args = parser.parse_args()
	receive(args, args.directories)

	# We await user input because it is convenient to also open the script from a file 
	# explorer. If we don't wait for user input, the terminal window will die instantly.
	while (not args.yestoall):
		dirs = str(input("Exit with ENTER. Order more directories? Type them here, separated with spaces:\n")).split(" ")
		# Break on ENTER press
		if len(dirs) < 2:
			exit("Exiting..")
		receive(args, dirs)
	

if __name__ == '__main__':
	main()
