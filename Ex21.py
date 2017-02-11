__author__ = 'raj'

def add(a,b):
    print "Adding %d and %d: " %(a,b)
    return a+b

def substract(a,b):
    print "Substracting %d and %d" %(a,b)
    return a-b

def multiply(a,b):
    print "Multiplying %d and %d" %(a,b)
    return a*b

def divide(a,b):
    print "Dividing %d and %d" %(a,b)
    return a/b

a = int(raw_input('Please enter number A: '))
b = int(raw_input('Please enter number B: '))
age = add(a,b)
sub = substract(a,b)
mul = multiply(a,b)
div = divide(a,b)

# A ppuzzle here for understanding the functions

print "Here's the puzzle\n"
what = add(age,substract(sub,multiply(mul,divide(div,2))))
print what











