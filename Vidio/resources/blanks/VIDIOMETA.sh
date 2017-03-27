#!/bin/bash
rm !!<Working Dir>!!/resources/metaTest.txt
touch !!<Working Dir>!!/resources/metaTest.txt


best="$(cat !!<Working Dir>!!/resources/BestDepth.txt)"


#-------------------------------------------------------------------------
#Single stream writes
echo "Starting single stream writes"
while read -r line
do
	echo "$line">>!!<Working Dir>!!/resources/metaTest.txt
done < <(/opt/vidio -D -f !!<File Type>!! -q $best -v -n !!<Num Frames>!! /mnt/!!<Target Dir>!!/Vidio/0/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/metaTest.txt
done < <(/opt/vidio -D -f !!<File Type>!! -q $best -v -n !!<Num Frames>!! /mnt/!!<Target Dir>!!/Vidio/1/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/metaTest.txt
done < <(/opt/vidio -D -f !!<File Type>!! -q $best -v -n !!<Num Frames>!! /mnt/!!<Target Dir>!!/Vidio/2/)

echo "Finished Single Stream writes"
#-------------------------------------------------------------------------
#Single stream reads

echo "Starting single stream reads"

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/metaTest.txt
done < <(/opt/vidio -D -f !!<File Type>!! -q $best -v -n !!<Num Frames>!! -r /mnt/!!<Target Dir>!!/Vidio/0/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/metaTest.txt
done < <(/opt/vidio -D -f !!<File Type>!! -q $best -v -n !!<Num Frames>!! -r /mnt/!!<Target Dir>!!/Vidio/1/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/metaTest.txt
done < <(/opt/vidio -D -f !!<File Type>!! -q $best -v -n !!<Num Frames>!! -r /mnt/!!<Target Dir>!!/Vidio/2/)

echo "Finishing single stream reads"

#-------------------------------------------------------------------------
# Four stream writes

echo "Starting four stream writes"


while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/metaTest.txt
done < <(/opt/vidio -D -f !!<File Type>!! -q $best -v -n !!<Num Frames>!! /mnt/!!<Target Dir>!!/Vidio/3/ /mnt/!!<Target Dir>!!/Vidio/4/ /mnt/!!<Target Dir>!!/Vidio/5/ /mnt/!!<Target Dir>!!/Vidio/6/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/metaTest.txt
done < <(/opt/vidio -D -f !!<File Type>!! -q $best -v -n !!<Num Frames>!! /mnt/!!<Target Dir>!!/Vidio/3/ /mnt/!!<Target Dir>!!/Vidio/4/ /mnt/!!<Target Dir>!!/Vidio/5/ /mnt/!!<Target Dir>!!/Vidio/6/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/metaTest.txt
done < <(/opt/vidio -D -f !!<File Type>!! -q $best -v -n !!<Num Frames>!! /mnt/!!<Target Dir>!!/Vidio/3/ /mnt/!!<Target Dir>!!/Vidio/4/ /mnt/!!<Target Dir>!!/Vidio/5/ /mnt/!!<Target Dir>!!/Vidio/6/)


echo "Finishing four stream writes"

#--------------------------------------------------------------------------
# Four stream reads

echo "Starting four stream reads"

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/metaTest.txt
done < <(/opt/vidio -D -f !!<File Type>!! -q $best -v -n !!<Num Frames>!! -r /mnt/!!<Target Dir>!!/Vidio/3/ /mnt/!!<Target Dir>!!/Vidio/4/ /mnt/!!<Target Dir>!!/Vidio/5/ /mnt/!!<Target Dir>!!/Vidio/6/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/metaTest.txt
done < <(/opt/vidio -D -f !!<File Type>!! -q $best -v -n !!<Num Frames>!! -r /mnt/!!<Target Dir>!!/Vidio/3/ /mnt/!!<Target Dir>!!/Vidio/4/ /mnt/!!<Target Dir>!!/Vidio/5/ /mnt/!!<Target Dir>!!/Vidio/6/)

while read -r line
do
        echo "$line">>!!<Working Dir>!!/resources/metaTest.txt
done < <(/opt/vidio -D -f !!<File Type>!! -q $best -v -n !!<Num Frames>!! -r /mnt/!!<Target Dir>!!/Vidio/3/ /mnt/!!<Target Dir>!!/Vidio/4/ /mnt/!!<Target Dir>!!/Vidio/5/ /mnt/!!<Target Dir>!!/Vidio/6/)

echo "Finished four stream reads"

#------------------------------------------------------------------------
#Clean up and print results

