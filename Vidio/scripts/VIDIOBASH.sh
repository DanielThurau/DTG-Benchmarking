#!/bin/bash
rm /home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt
touch /home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt


best="$(cat /home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/BestDepth.txt)"
frame="$(cat /home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/BestSize.txt)"

#-------------------------------------------------------------------------
#Single stream writes
echo "Starting single stream writes"
while read -r line
do
	echo "$line">>/home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 /mnt/rfs2/Vidio/0/)

while read -r line
do
        echo "$line">>/home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 /mnt/rfs2/Vidio/1/)

while read -r line
do
        echo "$line">>/home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 /mnt/rfs2/Vidio/2/)

echo "Finished Single Stream writes"
#-------------------------------------------------------------------------
# flush
#echo 3 > /proc/sys/vm/drop_caches; sleep 2


#Single stream reads

echo "Starting single stream reads"

while read -r line
do
        echo "$line">>/home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 -r /mnt/rfs2/Vidio/0/)

while read -r line
do
        echo "$line">>/home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 -r /mnt/rfs2/Vidio/1/)

while read -r line
do
        echo "$line">>/home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 -r /mnt/rfs2/Vidio/2/)

echo "Finishing single stream reads"

#-------------------------------------------------------------------------
# Four stream writes

echo "Starting four stream writes"


while read -r line
do
        echo "$line">>/home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 /mnt/rfs2/Vidio/3/ /mnt/rfs2/Vidio/4/ /mnt/rfs2/Vidio/5/ /mnt/rfs2/Vidio/6/)

while read -r line
do
        echo "$line">>/home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 /mnt/rfs2/Vidio/3/ /mnt/rfs2/Vidio/4/ /mnt/rfs2/Vidio/5/ /mnt/rfs2/Vidio/6/)

while read -r line
do
        echo "$line">>/home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 /mnt/rfs2/Vidio/3/ /mnt/rfs2/Vidio/4/ /mnt/rfs2/Vidio/5/ /mnt/rfs2/Vidio/6/)


echo "Finishing four stream writes"

#--------------------------------------------------------------------------

# flush
#echo 3 > /proc/sys/vm/drop_caches; sleep 2

# Four stream reads

echo "Starting four stream reads"

while read -r line
do
        echo "$line">>/home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 -r /mnt/rfs2/Vidio/3/ /mnt/rfs2/Vidio/4/ /mnt/rfs2/Vidio/5/ /mnt/rfs2/Vidio/6/)

while read -r line
do
        echo "$line">>/home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 -r /mnt/rfs2/Vidio/3/ /mnt/rfs2/Vidio/4/ /mnt/rfs2/Vidio/5/ /mnt/rfs2/Vidio/6/)

while read -r line
do
        echo "$line">>/home/daniel/Documents/Programming/DTG-Benchmarking/Vidio/resources/test.txt
done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 -r /mnt/rfs2/Vidio/3/ /mnt/rfs2/Vidio/4/ /mnt/rfs2/Vidio/5/ /mnt/rfs2/Vidio/6/)

echo "Finished four stream reads"

#------------------------------------------------------------------------
#Clean up and print results

sudo rm -rf /mnt/!!<Targer Dir>!!/Vidio/
