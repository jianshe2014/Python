# -*- coding: utf-8 -*-
from sys import argv

#把 argv 中的东西解包，将所有的参数依次赋予左边的变量名
script,user_name=argv

prompt='1>'

print "hi %s,i'm the %s script." %(user_name,script)

print "Do you like me %s?" %user_name
likes=raw_input(prompt)

prompt='2>'
print "where Do you live %s?" %user_name
lives=raw_input(prompt)

prompt='3>'
print "ab" 
computer=raw_input(prompt)

print """
ab %r
cd %r 
ef %r
""" %(likes,lives,computer)







