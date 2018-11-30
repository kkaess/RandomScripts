# printFitsComments.py

# usage: python3 printFitsComments.py <space separated list of fits files with sufficient path data to open directly>
# effect: prints 1) the filename passed
# 		 2) the 'COMMENT' field of the fits header of the first HDU in the file associated with that filename
#			*if it exists*
# fails on: no header(?!), no hdu, no fits file at any location specified.

import sys
from astropy.io import fits

for fn in sys.argv[1:]:
	with fits.open(fn) as f:
		print(fn)
		if 'COMMENT' in f[0].header.keys():
			print(f[0].header['COMMENT'])
		print()

 


