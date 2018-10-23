#!/bin/python

import sqlite3
import json
import sys

connection = sqlite3.connect('sample.db')
cursor = connection.cursor()
query = "SELECT * FROM sample"
result = cursor.execute(query)

items = []

items = [dict(zip([key[0] for key in cursor.description], row)) for row in result]

connection.close()

# ouvre le fichier de sortie et redirige la sortie standard

orig_stdout = sys.stdout
f = open("myfile.json", "w")
sys.stdout = f

print json.dumps(items)

# reset la sortie standard et ferme le fichier de sortie
sys.stdout = orig_stdout
f.close()
