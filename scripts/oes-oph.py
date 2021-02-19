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

Executing and typing `alaska -u` will change its contents to:

alaska
 |-- alaska_1.jpg
 |-- alaska_2.jpg
 |-- alaska_3.png
 |-- alaska_4.jpg
"""

import os

default_extension = ".jpg"


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
					dst += default_extension
				src = path + filename
				print(src, "-->", dst)
				os.rename(src, dst)
	except Exception as e:
		exit("[!] Something went wrong: "+str(e)+"\nExiting...")

def main():
	print("Usage: <folder_name> <options..>")
	print("-u : Update folder")
	cmds = str(input("Enter the folder name(s) and args, separated with spaces: ")).split(" ")
	# syntax <name> <-options..>

	if "-u" in cmds:
		cmds.remove("-u")
		for name in cmds:
			path = name + "/"
			print("Updating ...")
			rename("tmp", path)
			print("Renaming ...")
			rename(name, path)
	else:
		for name in cmds:
			path = name + "/"
			rename(name, path)
	

if __name__ == '__main__':
	main()
