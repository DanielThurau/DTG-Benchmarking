import sys
import math;
infile, outfile = sys.argv[1], sys.argv[2]

inf = open(infile)
outf = open(outfile,"w")
line_words = [];

for line in inf:
        if 'MBytes/sec' in line:
                line_words.append(line);
preFinal = [];
for text in line_words:
        preFinal.append(text.split())

for each in preFinal:
        each.pop(0);
        each[0] = float(each[0])

best = max(preFinal);
if(preFinal[0]==best):
	outf.write("sdtv");
elif(preFinal[1] == best):
	outf.write("hdtv");
elif(preFinal[2] == best):
	outf.write("fa2k");
elif(preFinal[3] == best):
	outf.write("fa4k");

