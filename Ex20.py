from sys import argv
script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_number,file):
	print line_number,file.readline()

current_file = open(input_file)
print "Let's read the whole file : \n"
print_all(current_file)

print "Now lets rewind, kind of like a tape"
rewind(current_file)

print "Lets print 3 lines"
current_line = 1
print_a_line(current_line,current_file)
current_line = 2
print_a_line(current_line,current_file)
current_line = 3
print_a_line(current_line,current_file)