#!/bin/bash
#-------------------------------------------------------------------------
#Single stream writes
echo "Starting Depth Testing"
while read -r line
do
	echo "$line">>!!<Working Dir>!!/resources/DepthTest.txt
done < <(/opt/vidio -D -f fa4k -q 4 -n 2000 /mnt/!!<Target Dir>!!/Vidio/0/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/DepthTest.txt
done < <(/opt/vidio -D -f fa4k -q 8 -n 2000 /mnt/!!<Target Dir>!!/Vidio/1/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/DepthTest.txt
done < <(/opt/vidio -D -f fa4k -q 16 -n 2000 /mnt/!!<Target Dir>!!/Vidio/2/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/DepthTest.txt
done < <(/opt/vidio -D -f fa4k -q 32 -n 2000 /mnt/!!<Target Dir>!!/Vidio/3/)

sudo rm -rf /mnt/!!<Target Dir>!!/Vidio/0/ /mnt/!!<Target Dir>!!/Vidio/1/ /mnt/!!<Target Dir>!!/Vidio/2/ /mnt/!!<Target Dir>!!/Vidio/3/ 
