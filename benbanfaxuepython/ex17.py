# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists
"""
将一个文件中的内容拷贝到另个一个文件中。
exists 判断文件是否存在
"""

script,from_file,to_file = argv

print "copying from %s to %s" %(from_file,to_file)

in_file=open(from_file)
indata=in_file.read()
print indata

print "The input file is %d bytes long" %len(indata)

#看文件是否存在？
print "Does the output file exist?%r" %exists(to_file)

raw_input()

out_file=open(to_file,'w')
out_file.write(indata)

print "alright,all done."

out_file.close()
in_file.close()










