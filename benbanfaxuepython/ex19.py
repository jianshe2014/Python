# -*- coding: utf-8 -*-
"""
函数与变量
"""

def a_and_c(a_count,boxes):
	print " %d a" % a_count
	print "%d boxes" % boxes
	print "get a blanket.\n"

def t_c(x,y):
	print "%s a" % x
	print "%r a" % y
	
a_and_c(20,30)	

a1=10
b1=50


a_and_c(a1,b1)

a_and_c(10+20,5+6)

a_and_c(a1+100,b1+1000)

a2=raw_input("a2? ")
b2=raw_input("b2? ")

t_c(a2,b2)


	







