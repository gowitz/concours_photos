#!/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import os.path
import sys
reload(sys)
sys.setdefaultencoding('utf8')

db = "sample.db"
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect(db)
connection.row_factory = dict_factory

cursor = connection.cursor()

cursor.execute("select * from sample")

# fetch all or one we'll go for all.

results = cursor.fetchall()

print results

connection.close()

# ouvre le fichier de sortie et redirige la sortie standard

orig_stdout = sys.stdout
f = open("myfile.json", "w")
sys.stdout = f

print results

# reset la sortie standard et ferme le fichier de sortie
sys.stdout = orig_stdout
f.close()
