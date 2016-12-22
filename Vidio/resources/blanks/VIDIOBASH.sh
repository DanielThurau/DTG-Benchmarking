#!/bin/bash
rm !!<Working Dir>!!/resources/test.txt
touch !!<Working Dir>!!/resources/test.txt


best="$(cat !!<Working Dir>!!/resources/BestDepth.txt)"
frame="$(cat !!<Working Dir>!!/resources/BestSize.txt)"

#-------------------------------------------------------------------------
#Single stream writes
echo "Starting single stream writes"
while read -r line
do
	echo "$line">>!!<Working Dir>!!/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 /mnt/!!<Target Dir>!!/vidio/0/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 /mnt/!!<Target Dir>!!/vidio/1/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 /mnt/!!<Target Dir>!!/vidio/2/)

echo "Finished Single Stream writes"
#-------------------------------------------------------------------------
# flush
#echo 3 > /proc/sys/vm/drop_caches; sleep 2


#Single stream reads

echo "Starting single stream reads"

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 -r /mnt/!!<Target Dir>!!/vidio/0/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 -r /mnt/!!<Target Dir>!!/vidio/1/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 -r /mnt/!!<Target Dir>!!/vidio/2/)

echo "Finishing single stream reads"

#-------------------------------------------------------------------------
# Four stream writes

echo "Starting four stream writes"


while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 /mnt/!!<Target Dir>!!/vidio/3/ /mnt/!!<Target Dir>!!/vidio/4/ /mnt/!!<Target Dir>!!/vidio/5/ /mnt/!!<Target Dir>!!/vidio/6/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 /mnt/!!<Target Dir>!!/vidio/3/ /mnt/!!<Target Dir>!!/vidio/4/ /mnt/!!<Target Dir>!!/vidio/5/ /mnt/!!<Target Dir>!!/vidio/6/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 /mnt/!!<Target Dir>!!/vidio/3/ /mnt/!!<Target Dir>!!/vidio/4/ /mnt/!!<Target Dir>!!/vidio/5/ /mnt/!!<Target Dir>!!/vidio/6/)


echo "Finishing four stream writes"

#--------------------------------------------------------------------------

# flush
#echo 3 > /proc/sys/vm/drop_caches; sleep 2

# Four stream reads

echo "Starting four stream reads"

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 -r /mnt/!!<Target Dir>!!/vidio/3/ /mnt/!!<Target Dir>!!/vidio/4/ /mnt/!!<Target Dir>!!/vidio/5/ /mnt/!!<Target Dir>!!/vidio/6/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 -r /mnt/!!<Target Dir>!!/vidio/3/ /mnt/!!<Target Dir>!!/vidio/4/ /mnt/!!<Target Dir>!!/vidio/5/ /mnt/!!<Target Dir>!!/vidio/6/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 -r /mnt/!!<Target Dir>!!/vidio/3/ /mnt/!!<Target Dir>!!/vidio/4/ /mnt/!!<Target Dir>!!/vidio/5/ /mnt/!!<Target Dir>!!/vidio/6/)

echo "Finished four stream reads"

#------------------------------------------------------------------------
#Clean up and print results

sudo rm -rf /mnt/!!<Targer Dir>!!/vidio/
