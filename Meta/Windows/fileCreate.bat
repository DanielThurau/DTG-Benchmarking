@echo off
mkdir !!<Shared Folder>!!:\Meta\testfiles\dir1\dir5;
mkdir !!<Shared Folder>!!:\Meta\testfiles\dir2\dir6;
mkdir !!<Shared Folder>!!:\Meta\testfiles\dir3\dir7;
mkdir !!<Shared Folder>!!:\Meta\testfiles\dir4\dir8;

SET tota1=%time%

start \resources\fileMake1.bat /c
start \resources\fileMake2.bat /c
start \resources\fileMake3.bat /c
start \resources\fileMake4.bat /c
start \resources\fileMake5.bat /c
start \resources\fileMake6.bat /c
start \resources\fileMake7.bat /c
start /wait \resources\fileMake8.bat /c




SET total2=%time%

echo %total2%

echo %total1%
