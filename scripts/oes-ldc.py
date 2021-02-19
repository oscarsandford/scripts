#!/usr/bin/env python3

"""
oes-ldc.py
List Directory Contents

Considers subdirectories in the directory tree rooted at the execution 
directory. Outputs an unsorted list of subdirectories and the number of 
files in their respective subdirectory.

Does not consider files in the current directory.
"""

import os
from sys import platform, argv


def print_tree(sts, arg, root):
	print("--------- Start of directory tree contents ---------")
	if arg == "u":
		for s in sts:
			print(" {:>4} files\t".format(sts[s]), s[len(root):])
	elif arg == "s":
		sorted_sts = sorted(sts.items(), key=lambda x: x[1])
		for i in sorted_sts:
			print(" {:>4} files\t".format(i[1]), i[0][len(root):])
	print("---------- End of directory tree contents ----------")

def make_tree(root):
	sts = {}
	for dirname, dirnames, filenames in os.walk(root):
		# all subdirs
		for subdirname in dirnames:
			path = str(os.path.join(dirname, subdirname))
			flcount = 0
			# Count files
			for fl in os.listdir(path):
				flcount += 1
			sts[path] = flcount

			# Remove redundant paths by checking if a path exists in the 
			# dict with the segment of the path discluding the leaf
			if platform == "win32":
				segs = path.split("\\")
			else:
				segs = path.split("/")
			upper_path = path[:len(path)-len(segs[len(segs)-1])-1]
			if upper_path in sts.keys():
				del sts[upper_path]
	return sts

# List contents of directory tree then wait for exit queue
def main():
	root = os.getcwd()
	# Option to pass a directory
	if len(argv) == 2:
		root = argv[1]
	sts = make_tree(root)
	valid_args = ["u", "s"]
	
	print_tree(sts, "u", root)
	while (1):
		x = input("Type s to see sorted, u to see unsorted. Or just ENTER to exit.")
		exit(0) if x not in valid_args else print_tree(sts, "s", root)
		

if __name__ == '__main__':
	main()
