#!/bin/bash

# Clears and re-creates file that data is written too
rm !!<Working Dir>!!/resources/test.txt
touch !!<Working Dir>!!/resources/test.txt

# Results of the DepthTester is stored in this file
# Parse for Best Depth to run at
best="$(cat !!<Working Dir>!!/resources/BestDepth.txt)"
# Results of the Frame size is stored in this file
# Parse for Best Frame size to run at
frame="$(cat !!<Working Dir>!!/resources/BestSize.txt)"

echo "Tests use $best Queue Depth and $frame size frames"
echo "Tests use $best Queue Depth and $frame size frames" |  sudo tee -a !!<Working Dir>!!/results/vidioResults.txt 


# Single Stream Bench Marking
benchSingleStream() {
	
	# Arg[0] is either -w or -r (write or read respectively)
	IO=$1
	
	echo "Staring a single stream $1 test"

	# Three tests are outputted to test.txt
	for i in range {0..2}
	do
		# Run a single test and output data to test.txt
		while read -r line
		do
        		echo "$line">>!!<Working Dir>!!/resources/test.txt
		done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 $1 /mnt/!!<Target Dir>!!/vidio/$i/)
	done

	echo "Finished a single Stream test"
	
	# Flush cache 
	# Taken from Pierre Evenou
	echo 3 > /proc/sys/vm/drop_caches; sleep 2;

}

# Calls
benchSingleStream -w;
benchSingleStream -r;


# Four Stream Bench Marking
benchFourStream (){
	IO=$1
	
	echo "Starting a four stream $1 test"

	for i in range{0..2};
	do
		while read -r line
		do
        		echo "$line">>!!<Working Dir>!!/resources/test.txt
		done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 $1 /mnt/!!<Target Dir>!!/vidio/3/ /mnt/!!<Target Dir>!!/vidio/4/ /mnt/!!<Target Dir>!!/vidio/5/ /mnt/!!<Target Dir>!!/vidio/6/)

	done;
	
	echo 3 > /proc/sys/vm/drop_caches; sleep 2


}


benchFourMount (){
        IO=$1

        echo "Starting a four stream $1 test"

        for i in range{0..2};
        do
                while read -r line
                do
                        echo "$line">>!!<Working Dir>!!/resources/test.txt
                done < <(/opt/vidio -D -f $frame -q $best -v -n 2000 $1 /mnt/!!<Target Dir>!!A/vidio/3/ /mnt/!!<Target Dir>!!B/vidio/4/ /mnt/!!<Target Dir>!!C/vidio/5/ /mnt/!!<Target Dir>!!D/vidio/6/)

        done;

        echo 3 > /proc/sys/vm/drop_caches; sleep 2


}

#benchFourMount -w
#benchFourMount -r

#--------------------------------------------------------------------------

