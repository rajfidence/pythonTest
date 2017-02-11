__author__ = 'raj'

def cheese_and_crackers(cheese_count,crackers):
    print "You have %d cheese" %cheese_count
    print "You have %d crackers" %crackers
    print "This is enough for the party"
    print "That's enough for the party.\n"

print "We can give numbers directly"
cheese_and_crackers(10,20)

print "We can also use a variable"
amount_cheese = 20
amount_crackers = 40
cheese_and_crackers(amount_cheese,amount_crackers)

print "we can also perform arithematic function"
cheese_and_crackers(10+34,8+45)

print "And we can also combine both"
cheese_and_crackers(amount_cheese+10,amount_crackers+40)





