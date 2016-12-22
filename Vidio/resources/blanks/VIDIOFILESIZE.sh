#!/bin/bash
#-------------------------------------------------------------------------
#Single stream writes
echo "Starting Size Testing"
while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/SizeTest.txt
done < <(/opt/vidio -D -f sdtv -q 8 -n 2000 /mnt/!!<Target Dir>!!/vidio/10/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/SizeTest.txt
done < <(/opt/vidio -D -f hdtv -q 8 -n 2000 /mnt/!!<Target Dir>!!/vidio/10/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/SizeTest.txt
done < <(/opt/vidio -D -f fa2k -q 8 -n 2000 /mnt/!!<Target Dir>!!/vidio/10/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/SizeTest.txt
done < <(/opt/vidio -D -f fa4k -q 8 -n 2000 /mnt/!!<Target Dir>!!/vidio/10/)

