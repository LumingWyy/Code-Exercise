'''
Created on 2017/07/22
student id 1710245
@author: WangLuming
'''

#coding:Shift_JIS

file1 = raw_input('Enter file name 1 ')
file2 = raw_input('Enter file name 2 ')
inputFile=open(file1)
outputFile=open(file2)
content=inputFile.readlines();
for eachLine in content:
    outputFile.write(eachLine);
inputFile.close()
outputFile.close()