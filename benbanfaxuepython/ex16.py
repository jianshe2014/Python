# -*- coding: utf-8 -*-
from sys import argv

script,filename=argv

txt=open(filename)

print "here's your file %r:" % filename

raw_input("?")

print "opening the file ..."
target =open(filename,'w')

#清空文件
target.truncate()

#写入文件
line1=raw_input("line1:")
line2=raw_input("line2:")

#write需要接收一个字符串作为参数
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.close()

#读取当前文件打印的内容
filename2 = raw_input("filename2 ")
target2 = open(filename2)
print target2.read()

target2.close()






