# printFitsComments.py

# usage: python3 printFitsComments.py <space separated list of fits files with sufficient path data to open directly>
# effect: prints 1) each filename passed
# 		 2) the 'COMMENT' field of the fits header of the first HDU in the file associated with that filename
#			*if it exists*
# fails on: So many things. Too many to list. Bad code, bad. 

import sys
from astropy.io import fits
from datetime import datetime

def printFitsComment(fileList,orderByTimestamp=False):
	stringListList = [] #container to store the information
	for filename in fileList:
		try:
			with fits.open(filename,ignore_missing_end=True) as f:
				stringList = [filename] #enter filename as first element in entry
				if 'COMMENT' in f[0].header.keys():
					stringList.append(f[0].header['COMMENT']) #enter COMMENT as second element in entry
				else:
					stringList.append('')
				if 'DATE' in f[0].header.keys():
				# parse header DATE field and enter as third element in entry
					stringList.append(datetime.strptime(f[0].header['DATE'],"%Y-%m-%dT%H:%M:%S"))
				else:
					stringList.append(datetime.today()+datetime.day)
				stringListList.append(stringList)
		except OSError:
			print('Failed to open '+filename, file=sys.stderr)
	if orderByTimestamp:
		stringListList.sort(key = lambda x: x[2]) #sorts by the date
			
	#Currently outputs as plain-text - may update later to output in markdown or similar
	for entry in stringListList:
		
		print(entry[0])
		print(entry[2])
		print("\n"+str(entry[1])+"\n\n")
	

if __name__ == "__main__":

	printFitsComment(sys.argv[1:],orderByTimestamp=True)

 


