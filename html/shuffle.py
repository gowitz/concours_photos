#!/usr/bin/python
import random
import string

list = list(string.ascii_lowercase)

random.shuffle(list)
print "Reshuffled list : ",  list
