D:\program_files\Unity\2020.3.23f1\Editor\Unity.exe -projectPath "." -runTests -testResults playmodetests.xml -testPlatform StandaloneWindows64 -testCategory "BatchmodeTest"
python UTFReport\parseresults.py playmodetests.xml
pause