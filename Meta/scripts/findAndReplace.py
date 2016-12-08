import fileinput;
import sys
import re 

# Infile and outfile declaration from system arg[0] and arg[1]
filein = sys.argv[1]
fileout = sys.argv[2]

#-----------------------------------------------
textToReplace1 = sys.argv[3]
textToReplace2 = sys.argv[4]
textToReplace3 = sys.argv[5]
textToReplace4 = sys.argv[6]
#------------------------------------------------
textToSearch1 = "!!<Working Dir>!!"
textToSearch2 = "!!<Target Dir>!!"
textToSearch3 = "!!<Number Files>!!"
textToSearch4 = "!!<Size>!!"

# Reads in the data
f = open(filein,'r')
filedata = f.read()
f.close()

# Replaces textToSearch with textToReplace
filedata = filedata.replace(textToSearch1,textToReplace1)
filedata = filedata.replace(textToSearch2,textToReplace2)
filedata = filedata.replace(textToSearch3,textToReplace3)
filedata = filedata.replace(textToSearch4,textToReplace4)

# Writes it out
f = open(fileout,'w')
f.write(filedata)
f.close()
