import fileinput;
import sys
import re 

# Infile and outfile declaration from system args
filein = sys.argv[1]
fileout = sys.argv[2]
textToReplace1 = sys.argv[3]
textToReplace2 = sys.argv[4]


#-----------------------------------------------------------
textToSearch1 = "!!<client:/server/share>!!"
#textToReplace1 = r"whatever ot os"
textToSearch2 = "!!<user>!!"
#textToReplace2 = r"dtg/adminsitrator"


f = open(filein,'r')
filedata = f.read()
f.close()

filedata = filedata.replace(textToSearch1,textToReplace1)
filedata = filedata.replace(textToSearch2,textToReplace2)
f = open(fileout,'w')
f.write(filedata)
f.close()

