for /l %%x in (1, 1, 16000) do (

fsutil file createnew !!<sharedFolderLocation>!!\Meta\testfiles\dir3\testfile%%x 1048576

)