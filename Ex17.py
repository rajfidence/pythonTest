__author__ = 'raj'
from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "Copying file %s to %s" %(from_file,to_file)

in_file = open(from_file)
in_data = in_file.read()

print "we will be copying %d bytes of data" %len(in_data)

print "Does the output file exist? %r" %exists(to_file)
print "Ready to copy the content? "
raw_input()

out_file = open(to_file,'w')
out_file.write(in_data)

print "All done"
out_file.close()
in_file.close()





