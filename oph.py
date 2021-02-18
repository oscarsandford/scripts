#!/usr/bin/env python3

import os

default_extension = ".jpg"


# Renames all files in "./name/" to "./name/name_<i>.<ext>"
def rename(name, path):
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
