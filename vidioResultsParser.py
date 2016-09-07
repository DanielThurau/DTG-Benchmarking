# Pareser for VIDIO tests ran at Daystrom Technology Group

import sys
import math;

# Takes args infile (results from a script that takes output from
# VIDIO test and writes them to a file) and opens outfile
infile, outfile = sys.argv[1], sys.argv[2]

# Opens files for reading and writing
inf = open(infile)
outf = open(outfile,"w")

# Declaration of array to hold lines
line_words = [];

# Parses the meaningful files from the file
for line in inf:
	if 'MBytes/sec' in line:
		line_words.append(line);

# Declaration of array to hold just the values 
preFinal = [];

# Removes white space
for text in line_words:
	preFinal.append(text.split())

# Pops the first element in each array within array
# Converts the numbers to floats
for each in preFinal:
	each.pop(0);
	each[0] = float(each[0])

# Adds the four stream test results over each stream and copies them downward through
# the array to conserve space
preFinal[6][0] = preFinal[6][0] + preFinal[7][0] + preFinal[8][0] + preFinal[9][0];
preFinal[7][0] = preFinal[10][0] + preFinal[11][0] + preFinal[12][0] + preFinal[13][0];
preFinal[8][0] = preFinal[14][0] + preFinal[15][0] + preFinal[16][0] + preFinal[17][0];
preFinal[10][0] = preFinal[18][0] + preFinal[19][0] + preFinal[20][0] + preFinal[21][0];
preFinal[11][0] = preFinal[22][0] + preFinal[23][0] + preFinal[24][0] + preFinal[25][0];
preFinal[12][0] = preFinal[26][0] + preFinal[27][0] + preFinal[28][0] + preFinal[29][0];

# Splices old array to just have values that matter
preFinal = preFinal[0:13];
# Declares the array that holds the finals values
final = [];
# while loop iterators
j = 4;
i = 0;

# Makes life easier since there will only be 
# three values ever
spacing = [0.0,0.0,0.0];


while (j > 0):

	# Declare variables that will hold the comparable values
	one = preFinal[i][0];
	two = preFinal[i+1][0];
	three = preFinal[i+2][0];

	# Find the spacing between the values
	spacing[0] = math.fabs(one - two);
	spacing[1] = math.fabs(one - three);
	spacing[2] = math.fabs(two - three);

	# Pop the minimum difference and check which it belongs to.
	# afterwards find the maximum of the two closest 
	finalSpacing = min(spacing);
	if(finalSpacing==spacing[0]):
		final.append(max(one,two));
	elif(finalSpacing == spacing[1]):
		final.append(max(one,three));
	elif(finalSpacing == spacing[2]):
		final.append(max(two, three));

	i = i + 3;
	j = j -1;


# Change the float to a string and give it its label
for i in range(0,len(final)):
	final[i] = str(final[i]);
	if(i==0):
		final[i] = "Write throughput for 1 stream = " + final[i];
	elif(i==1):
		final[i] = "Read throughput for 1 stream = " + final[i];
	elif(i==2):
		final[i] = "Write throughput for 4 streams = " + final[i];
	elif(i==3):
		final[i] = "Read throughput for 4 streams = " + final[i];


# Write it out to a file
for i in final:
	outf.write("%s\n" % i);
