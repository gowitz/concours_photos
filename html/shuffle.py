#!/usr/bin/python
import random
import string

#list = list(string.ascii_lowercase)
list = range(01, 43)

print ", ".join('%02d'%x for x in list)
random.shuffle(list)
print ", ".join('%02d'%x for x in list)
