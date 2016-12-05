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
 
i = 6;
preFinal[6][0] = preFinal[6][0] + preFinal[7][0] + preFinal[8][0] + preFinal[9][0];
preFinal[7][0] = preFinal[10][0] + preFinal[11][0] + preFinal[12][0] + preFinal[13][0];
preFinal[8][0] = preFinal[14][0] + preFinal[15][0] + preFinal[16][0] + preFinal[17][0];
preFinal[10][0] = preFinal[18][0] + preFinal[19][0] + preFinal[20][0] + preFinal[21][0];
preFinal[11][0] = preFinal[22][0] + preFinal[23][0] + preFinal[24][0] + preFinal[25][0];
preFinal[12][0] = preFinal[26][0] + preFinal[27][0] + preFinal[28][0] + preFinal[29][0];

semiFinal = preFinal[0:13];
final = [];
j = 4;
i = 0;
spacing = [0.0,0.0,0.0];
while (j > 0):
	one = semiFinal[i][0];
	two = semiFinal[i+1][0];
	three = semiFinal[i+2][0];

	spacing[0] = math.fabs(one - two);
	spacing[1] = math.fabs(one - three);
	spacing[2] = math.fabs(two - three);

	finalSpacing = min(spacing);
	if(finalSpacing==spacing[0]):
		final.append(max(one,two));
	elif(finalSpacing == spacing[1]):
		final.append(max(one,three));
	elif(finalSpacing == spacing[2]):
		final.append(max(two, three));

	i = i + 3;
	j = j -1;


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

for i in final:
	outf.write("%s\n" % i);
