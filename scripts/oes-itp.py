#!/usr/bin/env python3

"""
oes-itp.py
Images to PDF

Uses img2pdf as a library to combine images to a PDF. 
Mainly used for quickly compiling images of homework assignments 
to a single PDF for submission in online classes.

Currently only works best on images without an alpha channel (i.e JPG).
TODO: add support for PNG.

Example Usages:
	$ oes-itp.py
		# Use every other image file in the current directory for the PDF.
	$ oes-itp.py -d path/to/images/
		# Use every image file in the specified directory for the PDF.
	$ oes-itp.py -i img1.jpg img2.png
		# Create a PDF with img1.jpg and img2.png.
	$ oes-itp.py -o outp.pdf
		# Renames output file to outp.pdf

Oscar Sandford
Originally created: 2021-02-25
"""

import img2pdf
import os
import argparse

def create_pdf(dir, images, outfname, extns):
	try:
		for dpath, _, fnames in os.walk(dir):
			for fname in fnames:
				for ext in extns:
					if fname.endswith(ext):
						imagepath = os.path.join(dpath, fname)
						print(f"Adding {imagepath}...")
						images.append(imagepath)
			if len(images) > 0:
				outfile = open(outfname, "wb")
				outfile.write(img2pdf.convert(images))
				outfile.close()
				print("Done!")
			else:
				print("No images found.")
	except Exception as e:
		outfile.close()
		exit("Something bad happened:",e)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--images", action="extend", default=[], nargs="+", type=str, 
		help="Add specific images to the PDF separated by spaces.")
	parser.add_argument("-d", "--directory", default=os.getcwd(), 
		help="Specify directory to find input files.")
	parser.add_argument("-o", "--output", default="out.pdf", 
		help="Specify an output file name. Be careful to add .pdf.")
	parser.add_argument("-e", "--extensions", action="extend", default=[".jpg"], 
		help="Only take files with these extensions separated by spaces (i.e .jpg .png .bmp)")
	args = parser.parse_args()
	
	create_pdf(args.directory, args.images, args.output, args.extensions)
	

if __name__ == '__main__':
	main()
