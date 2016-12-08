import fileinput;
import sys
import numpy as np;

# Infile and outfile declaration from system args
filein = sys.argv[1]
f = open(filein,'r')

# Reads first line of file
filedata = f.readline()

# Fills array with zeros 
times = np.zeros(int(filedata)/2);

# Reads line and subtracts the two.
# Inputs it into the array
for i in range(0, int(filedata)/2):
      a = f.readline();
      b = f.readline();
      times[i] = (int(b) - int(a))

# Averages the array
whole = 0;
for j in range(0, int(filedata)/2):
      whole = whole + times[j];

avg = whole / (int(filedata)/2);

print("The avg of all the file creates was " + str(avg) + " milliseconds");


f.close();
