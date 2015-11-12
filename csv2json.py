#!/usr/bin/python
#-*- mode: python -*-

import csv
import json
import os
import sys

d = {}
#c = open('data/'+sys.argv[1]+'.csv', 'rtU')
c = open('data/data.csv', 'rtU')

# only encodes project name, table/expo, sponsors, and link.
# and yes, unicode sucks and so i'm clobbering all the impossible / trouble maker characters.

try:
    reader = csv.reader(c)
    for row in reader:
        d[row[2].decode('utf-8', 'ignore').encode('ascii', 'ignore')] = {"expo": row[0].decode('utf-8', 'ignore').encode('ascii', 'ignore'), "table": row[1].decode('utf-8', 'ignore').encode('ascii'), "sponsors": row[3].decode('utf-8', 'ignore').encode('ascii', 'ignore'), "link": row[4].decode('utf-8', 'ignore').encode('ascii')}

finally:
    c.close()

print json.dumps(d)

#with open('data/'+sys.argv[1]+'.json', 'w') as j:
with open('data/json', 'w') as j:
    json.dump(d, j)
