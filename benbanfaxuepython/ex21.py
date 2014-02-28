# -*- coding: utf-8 -*-
"""
函数可以返回东西
"""

def add(a,b):
	print "add %d + %d" %(a,b)
	return a + b

def substract(a,b):
	print "subrracting %d -%d" %(a,b)
	return a-b

def multiply(a,b):
	print "mu %d * %d" %(a,b)
	return a*b

def divide(a,b):
	print "dividing %d /%d" %(a,b)
	return a/b

age=add(30+5)	

height=substract(78,4)
weight=multiply(45,3)

what=add(age,substract(height,multiply(weight,divide(iq,2))))

print "That becomes:",what,"Can you do it by hand?"




	







