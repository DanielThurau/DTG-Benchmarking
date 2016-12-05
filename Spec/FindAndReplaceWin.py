import fileinput;
import sys
import re 

# Infile and outfile declaration from system args
filein = sys.argv[1]
fileout = sys.argv[2]
textToReplace1 = sys.argv[3]
textToReplace2 = sys.argv[4]
textToReplace3 = sys.argv[5]
# Opening read and write files
textToReplace1 = re.escape(textToReplace1)
textToReplace2 = re.escape(textToReplace2)
textToReplace3 = re.escape(textToReplace3)


#-----------------------------------------------------------
textToSearch1 = r"!!<client:\\server\share>!!"
#textToReplace1 = r"whatever ot os"
textToSearch2 = r"!!<user>!!"
#textToReplace2 = r"dtg/adminsitrator"
textToSearch3 = r"!!<user password>!!"
#textToReplace3 = r"Daystrom@225"


f = open(filein,'r')
filedata = f.read()
f.close()

filedata = filedata.replace(textToSearch1,textToReplace1)
filedata = filedata.replace(textToSearch2,textToReplace2)
filedata = filedata.replace(textToSearch3,textToReplace3)
f = open(fileout,'w')
f.write(filedata)
f.close()

