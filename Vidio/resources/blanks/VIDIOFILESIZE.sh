#!/bin/bash
#-------------------------------------------------------------------------
#Single stream writes
echo "Starting Size Testing"
while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/SizeTest.txt
done < <(/opt/vidio -D -f sdtv -q 8 -n 2000 /mnt/!!<Target Dir>!!/Vidio/1/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/SizeTest.txt
done < <(/opt/vidio -D -f hdtv -q 8 -n 2000 /mnt/!!<Target Dir>!!/Vidio/2/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/SizeTest.txt
done < <(/opt/vidio -D -f fa2k -q 8 -n 2000 /mnt/!!<Target Dir>!!/Vidio/3/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/SizeTest.txt
done < <(/opt/vidio -D -f fa4k -q 8 -n 2000 /mnt/!!<Target Dir>!!/Vidio/4/)

sudo rm -rf /mnt/!!<Target Dir>!!/Vidio/1/* /mnt/!!<Target Dir>!!/Vidio/2/* /mnt/!!<Target Dir>!!/Vidio/3/* /mnt/!!<Target Dir>!!/Vidio/4/*