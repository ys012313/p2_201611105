%%writefile python.txt
Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language.[23][24] 
Its design philosophy emphasizes code readability, and 
its syntax allows programmers to express concepts in fewer lines of code 
than would be possible in languages such as C++ or Java.[25][26] 
The language provides constructs intended to enable clear programs on 
both a small and large scale.[27]

import os
mydir=os.getcwd()

def fileA():
    mydir=os.getcwd()
    filename='python.txt'
    myfilename=os.path.join(mydir,filename)

try:
    myfile=open(myfilename,'r')
    contents=myfile.readlines()
    for content in contents:
        if content.lower().find('python')!=-1:
            print content
except IOError as e:
        print e
        myfile.close()

def fileB():
    myfile=open('output.txt','w')
    line1='first line'
    myfile.write(line1)
    line2='second line'
    myfile.write(line2)
    line3='third line'
    myfile.write(line3)
    myfile.close()

mydir=os.getcwd()
filename='output.txt'
myfilename=os.path.join(mydir,filename)
print myfilename

try:
    myfile=open(myfilename,'r')
    contents=myfile.readlines()
    for i in contents:
        if (-1< i.find("line")):
            print i.upper()
except IOError as e:
        print 'error'

def lab12():
    fileA()
    fileB()

def main():
    lab12()

main()