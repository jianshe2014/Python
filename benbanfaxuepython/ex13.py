# -*- coding: utf-8 -*-
from sys import argv

#把 argv 中的东西解包，将所有的参数依次赋予左边的变量名
script,first=argv

first=raw_input("first? ")

print "The script is called:",script
print "Your first variable is:",first

second=raw_input("second? ")

print "Your second variable is:",second




