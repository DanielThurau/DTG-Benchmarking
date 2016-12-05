# Results parser for benchmarking at Daystrom Technology Group
# after 16 tests

import sys

# Infile and outfile declaration from system args
infile, outfile = sys.argv[1], sys.argv[2]

# Opening read and write files
inf = open(infile)
outf = open(outfile,"w")

# Declaration of the array to hold lines containing the
# information needed
line_words = [];

# Parse every line that contains this keyword
for line in inf:
	if 'N/A' in line:
		line_words.append(line);

# Declaration of the array to hold parsed strings 
currentOne = [];

# Takes each line and appends an array of each value without whitespace
for text in line_words:
	currentTwo = text.split();
	currentOne.append(currentTwo)

# Declaration of the array to hold the final values
final = [];

# Loop iterators
j = 8;
i = 0;

# Loop that determines which line its on and depending on that
# Grabs IOPS or throughput, then takes the greater of the two tests
while(j > 0):
	if (i == 0 or i == 2 or i == 4):
		if(float(currentOne[i][4]) < float(currentOne[i+1][4])):
			final.append(currentOne[i+1][4]);
		else:
			final.append(currentOne[i][4]);
	elif(i==6):
		if(float(currentOne[i][2]) < float(currentOne[i+1][2])):
			final.append(currentOne[i+1][2]);
		else:
			final.append(currentOne[i][2]);
	elif(i == 8 or i == 10 or i == 12): 	
		if(float(currentOne[i][4]) < float(currentOne[i+1][4])):
			final.append(currentOne[i+1][4]);
		else:
			final.append(currentOne[i][4]);
	elif(i == 14):
		if(float(currentOne[i][2]) < float(currentOne[i+1][2])):
			final.append(currentOne[i+1][2]);
		else:
			final.append(currentOne[i][2]);
	j = j-1;
	i = i + 2;


# Iterates through the final array and adds labels to the final values for 
# human readability
for i in range(0,len(final)):
	if(i < 3):
		final[i] = "Throughput of one stream (MB/s) = " + final[i];
	elif(i == 3):
		final[i] = "Meta-data ops of one stream = " + final[i];
	elif(i > 3 and i < 7):
		final[i] = "Throughput of four streams (MB/s) = " + final[i];
	elif(i==7):
		final[i] = "Meta-data ops of four streams = " + final[i];

# Writes the final answers to the outfile
for i in final:
	outf.write("%s\n" % i);
