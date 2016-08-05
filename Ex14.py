__author__ = 'raj'

from sys import argv
script,user_name = argv
prompt = '>'
print "Hi %s, I'm %s script" %(user_name,script)
print "I will ask you couple of questions."
print "Do you like me %s" %(user_name)
likes = raw_input(prompt)

print """
Hello %s, welcome to python
Do you like python = %s
""" %(user_name,likes)

