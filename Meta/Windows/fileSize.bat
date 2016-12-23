@echo off
SET total1=%time%

du64.exe -v !!<Share folder>!!:\Meta\testfiles\

SET total2=%time%

echo %total2%

echo %total1%
