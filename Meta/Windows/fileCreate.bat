SET tota1=%time%

for /l %%x in (1, 1, !!<numOfFiles>!!) do (

fsutil file createnew !!<sharedFolderLocation>!!\Meta\testfiles\testfile%%x !!<sizeOfFile>!!

)

SET total2=%time%

echo %total2%

echo %total1%
