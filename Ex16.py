__author__ = 'raj'
from sys import argv

script,filename = argv
print "we are going to truncate %r" %filename
print "if you want to execution press ^C"
print "if you do want to truncate, press return"

raw_input('?')

print "opening the file..."
target = open(filename,'w')

print "truncating the file..."
target.truncate()

print "we will add 3 new lines to the file"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "we will write new content in the file"
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "And finally we close it."
target.close()
