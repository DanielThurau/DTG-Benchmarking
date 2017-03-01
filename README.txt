DTG-Benchmarking Documentation:

Windows Machines:

	We typically use Diskspd for benchmarking purposes revolving around throughput.

	You can download it at this link: https://gallery.technet.microsoft.com/DiskSpd-a-robust-storage-6cd2f223

	Diskspd is very well documented, but the commands we usually go something like this:

		diskspd.exe -c(64G - 100G) -b1M -C10 -d300 -o16 -t4 -si -Su -w0 -W10 testfile1.dat .... testfile4.dat

		diskspd.exe -c(64G - 100G) -b1M -C10 -d300 -o16 -t4 -si -Su -w100 -W10 testfile1.dat .... testfile4.dat

	The first parameter is the size of the .dat files you'll be writing to.  We typically do sizes larger than cache size to force swapping.

	-b is block size and typically we experiment with different sizes to test which values wil result in better testing.  

	-C is cool down time and we pick some arbritrary number.

	The -d flag is the duration of the test.  We typically are running many tests a day so the standard is a five minute test.  

	-o is outstanding I/o requests per thread, and like -t and -b, we play with those values to see how the system performs. 

	-si means the test will do sequential strides, and removing it will run the test using random strides.  

	-Su disables software caching, and is the default that DTG uses. The Diskspd documentation has a slew of other possible caching options that can be toggled. 

	-w(0-100) is how many writes are perfromed during the test.  100 is all writes and 0 is all reads.

	-W is warmup time and is an arbritrary number we choose.

	The final paramaeters are the test files. If these files haven't already been created, -c will populate them for you, but they must be touched by the user.