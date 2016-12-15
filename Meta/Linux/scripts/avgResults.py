import fileinput;
import sys
import numpy as np;

# Infile and outfile declaration from system args
filein = sys.argv[1]

f = open(filein,'r')

filedata = f.readline()

times = np.zeros(int(filedata)/2);

for i in range(0, int(filedata)/2):
      a = f.readline();
      b = f.readline();
      times[i] = (int(b) - int(a))


whole = 0;
for j in range(0, int(filedata)/2):
      whole = whole + times[j];

avg = whole / (int(filedata)/2);

print("The avg of all the file creates was " + str(avg) + " milliseconds");


f.close();
