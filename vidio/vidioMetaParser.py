import sys
import math;
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

preFinal1 = [];
preFinal2 = [];
for i in range(0, len(open_words)):
	preFinal1.append(open_words[i].split());
	preFinal2.append(close_words[i].split());
	preFinal1[i].pop(9);preFinal1[i].pop(8); preFinal1[i].pop(7); preFinal1[i].pop(5);preFinal1[i].pop(3);preFinal1[i].pop(0); 
	preFinal2[i].pop(9);preFinal2[i].pop(8); preFinal2[i].pop(7); preFinal2[i].pop(5);preFinal2[i].pop(3);  preFinal2[i].pop(0);




last = [];


winner1 = min(float(preFinal1[0][2]), float(preFinal1[1][2]));

if(winner1 == preFinal1[0][2]):
	winner = min(float(preFinal1[0][2]), float(preFinal1[2][2]));
else:
	winner = min(float(preFinal1[1][2]), float(preFinal1[2][2]));

if(winner==preFinal1[0][2]):
	last.append(preFinal1[0]);
elif(winner == preFinal1[1][2]):
	last.append(preFinal1[1]);
else:
	last.append(preFinal1[2]);


winner1 = min(float(preFinal1[3][2]), float(preFinal1[3][2]));

if(winner1 == preFinal1[3][2]):
	winner = min(float(preFinal1[3][2]), float(preFinal1[5][2]));
else:
	winner = min(float(preFinal1[4][2]), float(preFinal1[5][2]));

if(winner==preFinal1[3][2]):
	last.append(preFinal1[3]);
elif(winner == preFinal1[4][2]):
	last.append(preFinal1[4]);
else:
	last.append(preFinal1[5]);


avgOne = (float(preFinal1[6][2]) + float(preFinal1[7][2]) + float(preFinal1[8][2]) + float(preFinal1[9][2]))/4;
avgTwo = (float(preFinal1[10][2]) + float(preFinal1[11][2]) + float(preFinal1[12][2]) + float(preFinal1[13][2]))/4;
avgThree = (float(preFinal1[14][2]) + float(preFinal1[15][2]) + float(preFinal1[16][2]) + float(preFinal1[17][2]))/4;


winner1 = min(avgOne, avgTwo);



if(winner1==avgOne):
	winner = min(avgOne, avgThree);
else:
	winner = min(avgTwo, avgThree);

temp = [];
if(winner == avgTwo):
	#avg2 won 10...13
	temp.append(preFinal1[10][0])
	temp.append(str((float(preFinal1[10][1]) + float(preFinal1[11][1]) + float(preFinal1[12][1]) + float(preFinal1[13][1]))/4));
	temp.append(str((float(preFinal1[10][2]) + float(preFinal1[11][2]) + float(preFinal1[12][2]) + float(preFinal1[13][2]))/4));
	temp.append(str((float(preFinal1[10][3]) + float(preFinal1[11][3]) + float(preFinal1[12][3]) + float(preFinal1[13][3]))/4));
	last.append(temp);
elif(winner == avgThree):
	#avg3 won 14...17
	temp.append(preFinal1[14][0])
	temp.append(str((float(preFinal1[14][1]) + float(preFinal1[15][1]) + float(preFinal1[16][1]) + float(preFinal1[17][1]))/4));
	temp.append(str((float(preFinal1[14][2]) + float(preFinal1[15][2]) + float(preFinal1[16][2]) + float(preFinal1[17][2]))/4));
	temp.append(str((float(preFinal1[14][3]) + float(preFinal1[15][3]) + float(preFinal1[16][3]) + float(preFinal1[17][3]))/4));
	last.append(temp)
else:
	#avg1 won 6..10
	temp.append(preFinal1[6][0])
	temp.append(str((float(preFinal1[6][1]) + float(preFinal1[7][1]) + float(preFinal1[8][1]) + float(preFinal1[9][1]))/4));
	temp.append(str((float(preFinal1[6][2]) + float(preFinal1[7][2]) + float(preFinal1[8][2]) + float(preFinal1[9][2]))/4));
	temp.append(str((float(preFinal1[6][3]) + float(preFinal1[7][3]) + float(preFinal1[8][3]) + float(preFinal1[9][3]))/4));
	last.append(temp);


avgOne = (float(preFinal1[18][2]) + float(preFinal1[19][2]) + float(preFinal1[20][2]) + float(preFinal1[21][2]))/4;
avgTwo = (float(preFinal1[22][2]) + float(preFinal1[23][2]) + float(preFinal1[24][2]) + float(preFinal1[25][2]))/4;
avgThree = (float(preFinal1[26][2]) + float(preFinal1[27][2]) + float(preFinal1[28][2]) + float(preFinal1[29][2]))/4;

if(winner1==avgOne):
	winner = min(avgOne, avgThree);
else:
	winner = min(avgTwo, avgThree);

temp = [];
if(winner == avgTwo):
	#avg2 won 22..25
	temp.append(preFinal1[22][0])
	temp.append(str((float(preFinal1[22][1]) + float(preFinal1[23][1]) + float(preFinal1[24][1]) + float(preFinal1[25][1]))/4));
	temp.append(str((float(preFinal1[22][2]) + float(preFinal1[23][2]) + float(preFinal1[24][2]) + float(preFinal1[25][2]))/4));
	temp.append(str((float(preFinal1[22][3]) + float(preFinal1[23][3]) + float(preFinal1[24][3]) + float(preFinal1[25][3]))/4));
	last.append(temp);
elif(winner == avgThree):
	#avg3 won 26..29
	temp.append(preFinal1[26][0])
	temp.append(str((float(preFinal1[26][1]) + float(preFinal1[27][1]) + float(preFinal1[28][1]) + float(preFinal1[29][1]))/4));
	temp.append(str((float(preFinal1[26][2]) + float(preFinal1[27][2]) + float(preFinal1[28][2]) + float(preFinal1[29][2]))/4));
	temp.append(str((float(preFinal1[26][3]) + float(preFinal1[27][3]) + float(preFinal1[28][3]) + float(preFinal1[29][3]))/4));
	last.append(temp);
else:
	temp.append(preFinal1[18][0])
	temp.append(str((float(preFinal1[18][1]) + float(preFinal1[19][1]) + float(preFinal1[20][1]) + float(preFinal1[21][1]))/4));
	temp.append(str((float(preFinal1[18][2]) + float(preFinal1[19][2]) + float(preFinal1[20][2]) + float(preFinal1[21][2]))/4));
	temp.append(str((float(preFinal1[18][3]) + float(preFinal1[19][3]) + float(preFinal1[20][3]) + float(preFinal1[21][3]))/4));
	last.append(temp)
	#avg1 won 18..21


last2 = [];



winner1 = min(float(preFinal2[0][2]), float(preFinal2[1][2]));

if(winner1 == preFinal2[0][2]):
	winner = min(float(preFinal2[0][2]), float(preFinal2[2][2]));
else:
	winner = min(float(preFinal2[1][2]), float(preFinal2[2][2]));

if(winner==preFinal2[0][2]):
	last2.append(preFinal2[0]);
elif(winner == preFinal2[1][2]):
	last2.append(preFinal2[1]);
else:
	last2.append(preFinal2[2]);


winner1 = min(float(preFinal2[3][2]), float(preFinal2[3][2]));

if(winner1 == preFinal2[3][2]):
	winner = min(float(preFinal2[3][2]), float(preFinal2[5][2]));
else:
	winner = min(float(preFinal2[4][2]), float(preFinal2[5][2]));

if(winner==preFinal2[3][2]):
	last2.append(preFinal2[3]);
elif(winner == preFinal2[4][2]):
	last2.append(preFinal2[4]);
else:
	last2.append(preFinal2[5]);


avgOne = (float(preFinal2[6][2]) + float(preFinal2[7][2]) + float(preFinal2[8][2]) + float(preFinal2[9][2]))/4;
avgTwo = (float(preFinal2[10][2]) + float(preFinal2[11][2]) + float(preFinal2[12][2]) + float(preFinal2[13][2]))/4;
avgThree = (float(preFinal2[14][2]) + float(preFinal2[15][2]) + float(preFinal2[16][2]) + float(preFinal2[17][2]))/4;


winner1 = min(avgOne, avgTwo);



if(winner1==avgOne):
	winner = min(avgOne, avgThree);
else:
	winner = min(avgTwo, avgThree);

temp = [];
if(winner == avgTwo):
	#avg2 won 10...13
	temp.append(preFinal2[10][0])
	temp.append(str((float(preFinal2[10][1]) + float(preFinal2[11][1]) + float(preFinal2[12][1]) + float(preFinal2[13][1]))/4));
	temp.append(str((float(preFinal2[10][2]) + float(preFinal2[11][2]) + float(preFinal2[12][2]) + float(preFinal2[13][2]))/4));
	temp.append(str((float(preFinal2[10][3]) + float(preFinal2[11][3]) + float(preFinal2[12][3]) + float(preFinal2[13][3]))/4));
	last2.append(temp);
elif(winner == avgThree):
	#avg3 won 14...17
	temp.append(preFinal2[14][0])
	temp.append(str((float(preFinal2[14][1]) + float(preFinal2[15][1]) + float(preFinal2[16][1]) + float(preFinal2[17][1]))/4));
	temp.append(str((float(preFinal2[14][2]) + float(preFinal2[15][2]) + float(preFinal2[16][2]) + float(preFinal2[17][2]))/4));
	temp.append(str((float(preFinal2[14][3]) + float(preFinal2[15][3]) + float(preFinal2[16][3]) + float(preFinal2[17][3]))/4));
	last2.append(temp)
else:
	#avg1 won 6..10
	temp.append(preFinal2[6][0])
	temp.append(str((float(preFinal2[6][1]) + float(preFinal2[7][1]) + float(preFinal2[8][1]) + float(preFinal2[9][1]))/4));
	temp.append(str((float(preFinal2[6][2]) + float(preFinal2[7][2]) + float(preFinal2[8][2]) + float(preFinal2[9][2]))/4));
	temp.append(str((float(preFinal2[6][3]) + float(preFinal2[7][3]) + float(preFinal2[8][3]) + float(preFinal2[9][3]))/4));
	last2.append(temp);


avgOne = (float(preFinal2[18][2]) + float(preFinal2[19][2]) + float(preFinal2[20][2]) + float(preFinal2[21][2]))/4;
avgTwo = (float(preFinal2[22][2]) + float(preFinal2[23][2]) + float(preFinal2[24][2]) + float(preFinal2[25][2]))/4;
avgThree = (float(preFinal2[26][2]) + float(preFinal2[27][2]) + float(preFinal2[28][2]) + float(preFinal2[29][2]))/4;

if(winner1==avgOne):
	winner = min(avgOne, avgThree);
else:
	winner = min(avgTwo, avgThree);

temp = [];
if(winner == avgTwo):
	#avg2 won 22..25
	temp.append(preFinal2[22][0])
	temp.append(str((float(preFinal2[22][1]) + float(preFinal2[23][1]) + float(preFinal2[24][1]) + float(preFinal2[25][1]))/4));
	temp.append(str((float(preFinal2[22][2]) + float(preFinal2[23][2]) + float(preFinal2[24][2]) + float(preFinal2[25][2]))/4));
	temp.append(str((float(preFinal2[22][3]) + float(preFinal2[23][3]) + float(preFinal2[24][3]) + float(preFinal2[25][3]))/4));
	last2.append(temp);
elif(winner == avgThree):
	#avg3 won 26..29
	temp.append(preFinal2[26][0])
	temp.append(str((float(preFinal2[26][1]) + float(preFinal2[27][1]) + float(preFinal2[28][1]) + float(preFinal2[29][1]))/4));
	temp.append(str((float(preFinal2[26][2]) + float(preFinal2[27][2]) + float(preFinal2[28][2]) + float(preFinal2[29][2]))/4));
	temp.append(str((float(preFinal2[26][3]) + float(preFinal2[27][3]) + float(preFinal2[28][3]) + float(preFinal2[29][3]))/4));
	last2.append(temp);
else:
	temp.append(preFinal2[18][0])
	temp.append(str((float(preFinal2[18][1]) + float(preFinal2[19][1]) + float(preFinal2[20][1]) + float(preFinal2[21][1]))/4));
	temp.append(str((float(preFinal2[18][2]) + float(preFinal2[19][2]) + float(preFinal2[20][2]) + float(preFinal2[21][2]))/4));
	temp.append(str((float(preFinal2[18][3]) + float(preFinal2[19][3]) + float(preFinal2[20][3]) + float(preFinal2[21][3]))/4));
	last2.append(temp)
	#avg1 won 18..21







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


for i in final:
	outf.write("%s\n" % i);
