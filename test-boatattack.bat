D:\program_files\Unity\2020.3.23f1\Editor\Unity.exe -batchmode -projectPath "." -runTests -testResults playmodetests.xml -testPlatform playmode -testCategory "BatchmodeTest"
python TestResultsParse\parseresults.py playmodetests.xml
pause