# printFitsComments.py

# usage: python3 printFitsComments.py <space separated list of fits files with sufficient path data to open directly>
# effect: prints 1) the filename passed
# 		 2) the 'COMMENT' field of the fits header of the first HDU in the file associated with that filename
#			*if it exists*
# fails on: no header(?!), no hdu, no fits file at any location specified.

import sys
from astropy.io import fits
from datetime import datetime

def printFitsComment(fileList,orderByTimestamp=False):
	stringListList = []
	for filename in fileList:
		with fits.open(filename) as f:
			stringList = [filename]
			if 'COMMENT' in f[0].header.keys():
				stringList.append(f[0].header['COMMENT'])
			else:
				stringList.append('')
			if 'DATE' in f[0].header.keys():
				stringList.append(datetime.strptime(f[0].header['DATE'],"%Y-%m-%dT%H:%M:%S")
			else:
				stringList.append(datetime.now()))
		stringListList.append(stringList)
	if orderByTimestamp:
		stringListList.sort(key = lamda tup: tup[1])
			
	#Insert printout stuff
	

if __name__ = "__main__":

	for fn in sys.argv[1:]:
		with fits.open(fn) as f:
			print(fn)
			if 'COMMENT' in f[0].header.keys():
				print(f[0].header['COMMENT'])
			print()

 


