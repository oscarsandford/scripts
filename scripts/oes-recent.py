#!/usr/bin/env python3

"""
oes-recent.py
Recently Modified
List files or directories in given directory and 
subdirectories ordered by their last modified date.


Oscar Sandford
Originally created: 2021-07-17
"""

import os
from time import ctime
import argparse

def display(li: list, max_display: int):
	for i in range(len(li)):
		if i > max_display:
			break
		print(li[i][1]+"\t"+li[i][0])

def organize(mtimes: list, revrs: bool):
	mtimes.sort(reverse=revrs, key=lambda t : t[1])
	for t in mtimes:
		t[1] = ctime(t[1])
	return mtimes

def traverse(directories_only: bool, root: str):
	li = []
	for dirpath, dirnames, filenames in os.walk(root):
		targets = filenames
		if directories_only:
			targets = dirnames
		for t in targets:
			try:
				fpath = os.path.join(dirpath, t)
				mtime = os.path.getmtime(fpath)
				li.append([fpath, mtime])
			except Exception as e:
				print(e)
	return li

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("root", type=str, help="Directory to start traversal.")
	parser.add_argument("-d", "--directories", default=False, action="store_true", help="Display directories instead of files.")
	parser.add_argument("-n", "--number", default=10, type=int, help="The number of files to display.")
	parser.add_argument("-r", "--reverse", action="store_true", help="Display starting with oldest modified date.")
	args = parser.parse_args()

	display(organize(traverse(args.directories, args.root), not args.reverse), args.number)
	

if __name__ == "__main__":
	main()

