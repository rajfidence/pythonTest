__author__ = 'raj'
formatter = "%r,%r,%r,%r"
print formatter % (1,2,3,4)
print formatter % ('one','two', 'three', 'four')
print formatter % (True,False,True,False)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % ("I had this thing ",
                   "that could write any thing",
                   "But it didnt sing well",
                   "So i said good night")

