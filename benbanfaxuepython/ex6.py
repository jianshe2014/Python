# -*- coding: utf-8 -*-

x="Therer are %d types of people." % 10

binary="binary"
do_not="don't"

y="Those who know %s and those who %s." %(binary,do_not)

print x
print y

#%r,将所有内容都打印出来,打印字符串
print "I said:%r." %x
print "I alos said:'%s'." %y

hi=False
joke_eval="isn't that joke so funny?! %r"

print joke_eval % hi
w="this is the left ..."
e="a string with"

#字符串连接
print w+e

