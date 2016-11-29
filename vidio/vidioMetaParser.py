import sys
import math;

# Input: Three averages
# Output: The lowest 
def findBestAverage(a,b,c):
	winner = min(float(a), float(b), float(c));
	return winner;

# Input: Three lists, they're master list, and a value to compare
# Insert the list into the master corresponding to the value
def addWinner(a, b, c, array, winner):
	if(winner==a[2]):
		array.append(a);
	elif(winner == b[2]):
		array.append(b);
	else:
		array.append(c);


# Input: Four array indices
# Ouput: A list with the avg by indice of the lists indices
def addWinnerFourStreamA(i, j, k, l):
	temp = [];
	temp.append(preFinal1[i][0])
	temp.append(str((float(preFinal1[i][1]) + float(preFinal1[j][1]) + float(preFinal1[k][1]) + float(preFinal1[l][1]))/4));
	temp.append(str((float(preFinal1[i][2]) + float(preFinal1[j][2]) + float(preFinal1[k][2]) + float(preFinal1[l][2]))/4));
	temp.append(str((float(preFinal1[i][3]) + float(preFinal1[j][3]) + float(preFinal1[k][3]) + float(preFinal1[l][3]))/4));
	return temp;

# Input: Four array indices
# Ouput: A list with the avg by indice of the lists indices
def addWinnerFourStreamB(i, j, k, l):
	temp = [];
	temp.append(preFinal2[i][0])
	temp.append(str((float(preFinal2[i][1]) + float(preFinal2[j][1]) + float(preFinal2[k][1]) + float(preFinal2[l][1]))/4));
	temp.append(str((float(preFinal2[i][2]) + float(preFinal2[j][2]) + float(preFinal2[k][2]) + float(preFinal2[l][2]))/4));
	temp.append(str((float(preFinal2[i][3]) + float(preFinal2[j][3]) + float(preFinal2[k][3]) + float(preFinal2[l][3]))/4));
	return temp;



#-----------------------------------------------------------------------------
# Opens
#-----------------------------------------------------------------------------

# Open infile, outfile from sys arg
infile, outfile = sys.argv[1], sys.argv[2]
inf = open(infile)
outf = open(outfile,"w")
open_words = [];
close_words = [];
for line in inf:
	if ('Opens') in line:
		open_words.append(line);
	if ('Closes') in line:
		close_words.append(line);

# Create Lists or opens and close
# Po unnecessary values
preFinal1 = [];
preFinal2 = [];
for i in range(0, len(open_words)):
	preFinal1.append(open_words[i].split());
	preFinal2.append(close_words[i].split());
	preFinal1[i].pop(9);preFinal1[i].pop(8); preFinal1[i].pop(7); preFinal1[i].pop(5);preFinal1[i].pop(3);preFinal1[i].pop(0); 
	preFinal2[i].pop(9);preFinal2[i].pop(8); preFinal2[i].pop(7); preFinal2[i].pop(5);preFinal2[i].pop(3);  preFinal2[i].pop(0);


last = [];

# Single stream write value
winner = findBestAverage(preFinal1[0][2], preFinal1[1][2], preFinal1[2][2])
addWinner(preFinal1[0], preFinal1[1], preFinal1[2], last, winner);

# Single Stream read value
winner = findBestAverage(preFinal1[3][2], preFinal1[4][2], preFinal1[5][2]);
addWinner(preFinal1[3], preFinal1[4], preFinal1[5], last, winner);

# Four Stream Writes value
avgOne = (float(preFinal1[6][2]) + float(preFinal1[7][2]) + float(preFinal1[8][2]) + float(preFinal1[9][2]))/4;
avgTwo = (float(preFinal1[10][2]) + float(preFinal1[11][2]) + float(preFinal1[12][2]) + float(preFinal1[13][2]))/4;
avgThree = (float(preFinal1[14][2]) + float(preFinal1[15][2]) + float(preFinal1[16][2]) + float(preFinal1[17][2]))/4;
winner = findBestAverage(avgOne, avgTwo, avgThree);

temp = [];
if(winner == avgTwo):
	last.append(addWinnerFourStreamA(10, 11, 12, 13));
elif(winner == avgThree):
	last.append(addWinnerFourStreamA(14, 15, 16, 17))
else:
	last.append(addWinnerFourStreamA(6, 7, 8, 9));


# Four Stream Read Value
avgOne = (float(preFinal1[18][2]) + float(preFinal1[19][2]) + float(preFinal1[20][2]) + float(preFinal1[21][2]))/4;
avgTwo = (float(preFinal1[22][2]) + float(preFinal1[23][2]) + float(preFinal1[24][2]) + float(preFinal1[25][2]))/4;
avgThree = (float(preFinal1[26][2]) + float(preFinal1[27][2]) + float(preFinal1[28][2]) + float(preFinal1[29][2]))/4;
winner = findBestAverage(avgOne, avgTwo, avgThree);

temp = [];
if(winner == avgTwo):
	last.append(addWinnerFourStreamA(22, 23, 24, 25));
elif(winner == avgThree):
	last.append(addWinnerFourStreamA(26, 27, 28, 29));
else:
	last.append(addWinnerFourStreamA(18, 19, 20, 21))


#-------------------------------------------------------------------
# Closes
#-------------------------------------------------------------------

last2 = [];

# Single Stream Write
winner = findBestAverage(preFinal2[0][2], preFinal2[1][2], preFinal2[2][2])
addWinner(preFinal2[0], preFinal2[1], preFinal2[2], last2, winner);

# Single Stream Reads
winner = findBestAverage(preFinal2[3][2], preFinal2[4][2], preFinal2[5][2]);
addWinner(preFinal2[3], preFinal2[4], preFinal2[5], last2, winner);

# Four Stream Write 
avgOne = (float(preFinal2[6][2]) + float(preFinal2[7][2]) + float(preFinal2[8][2]) + float(preFinal2[9][2]))/4;
avgTwo = (float(preFinal2[10][2]) + float(preFinal2[11][2]) + float(preFinal2[12][2]) + float(preFinal2[13][2]))/4;
avgThree = (float(preFinal2[14][2]) + float(preFinal2[15][2]) + float(preFinal2[16][2]) + float(preFinal2[17][2]))/4;
winner = findBestAverage(avgOne, avgTwo, avgThree);

temp = [];

if(winner == avgTwo):
	last2.append(addWinnerFourStreamA(10, 11, 12, 13));
elif(winner == avgThree):
	last2.append(addWinnerFourStreamA(14, 15, 16, 17))
else:
	last2.append(addWinnerFourStreamA(6, 7, 8, 9));

# Four Stream Read
avgOne = (float(preFinal2[18][2]) + float(preFinal2[19][2]) + float(preFinal2[20][2]) + float(preFinal2[21][2]))/4;
avgTwo = (float(preFinal2[22][2]) + float(preFinal2[23][2]) + float(preFinal2[24][2]) + float(preFinal2[25][2]))/4;
avgThree = (float(preFinal2[26][2]) + float(preFinal2[27][2]) + float(preFinal2[28][2]) + float(preFinal2[29][2]))/4;
winner = findBestAverage(avgOne, avgTwo, avgThree);

temp = [];

if(winner == avgTwo):
	last2.append(addWinnerFourStreamA(22, 23, 24, 25));
elif(winner == avgThree):
	last2.append(addWinnerFourStreamA(26, 27, 28, 29));
else:
	last2.append(addWinnerFourStreamA(18, 19, 20, 21))


# Format Output
final = [];
for i in range(0,len(last)):
	if(i==0):
		final.append("For opening " + last[0][0] + " files")
		final.append("1 Stream writes min: " + last[0][1])
		final.append("1 Stream writes avg: " + last[0][2])
		final.append("1 Stream writes max: " + last[0][3])
	elif(i==1):
		final.append("1 Stream reads min: " + last[1][1])
		final.append("1 Stream reads avg: " + last[1][2])
		final.append("1 Stream reads max: " + last[1][3])
	elif(i==2):
		final.append("4 Stream writes min: " + last[2][1])
		final.append("4 Stream writes avg: " + last[2][2])
		final.append("4 Stream writes max: " + last[2][3])
	elif(i==3):
		final.append("4 Stream reads min: " + last[2][1])
		final.append("4 Stream reads avg: " + last[2][2])
		final.append("4 Stream reads max: " + last[2][3])


for i in range(0,len(last2)):
	if(i==0):
		final.append("For closing " + last2[0][0] + " files ")
		final.append("1 Stream writes min: " + last2[0][1])
		final.append("1 Stream writes avg: " + last2[0][2])
		final.append("1 Stream writes max: " + last2[0][3])
	elif(i==1):
		final.append("1 Stream reads min: " + last2[1][1])
		final.append("1 Stream reads avg: " + last2[1][2])
		final.append("1 Stream reads max: " + last2[1][3])
	elif(i==2):
		final.append("4 Stream writes min: " + last2[2][1])
		final.append("4 Stream writes avg: " + last2[2][2])
		final.append("4 Stream writes max: " + last2[2][3])
	elif(i==3):
		final.append("4 Stream reads min: " + last2[2][1])
		final.append("4 Stream reads avg: " + last2[2][2])
		final.append("4 Stream reads max: " + last2[2][3])


# Write to Outfile
for i in final:
	outf.write("%s\n" % i);




