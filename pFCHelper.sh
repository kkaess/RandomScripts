#!/bin/bash

# A bash script to automate comment extraction from a 
# parent folder that contains AIDA run folders and a SingleScans folder.  
# This is unique to AIDA, so only useful for our project.

# Usage: pFCHelper.sh <1: path of data folder> <2: (optional) path of printFitsComment.py>

# both parameters should be terminated with a / if used.

python3 $2printFitsComments.py $(ls $1*/Picture_*/Frame_*.fits $1SingleScans/*.fits)
