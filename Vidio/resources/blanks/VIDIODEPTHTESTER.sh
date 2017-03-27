#!/bin/bash
#-------------------------------------------------------------------------
#Single stream writes
echo "Starting Depth Testing"
while read -r line
do
	echo "$line">>!!<Working Dir>!!/resources/DepthTest.txt
done < <(/opt/vidio -D -f fa4k -q 4 -n 2000 /mnt/!!<Target Dir>!!/Vidio/10/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/DepthTest.txt
done < <(/opt/vidio -D -f fa4k -q 8 -n 2000 /mnt/!!<Target Dir>!!/Vidio/10/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/DepthTest.txt
done < <(/opt/vidio -D -f fa4k -q 16 -n 2000 /mnt/!!<Target Dir>!!/Vidio/10/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/DepthTest.txt
done < <(/opt/vidio -D -f fa4k -q 32 -n 2000 /mnt/!!<Target Dir>!!/Vidio/10/)

