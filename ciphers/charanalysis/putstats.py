#!/usr/bin/python3

##
## Print stats. Runs in Python 3.
## Author: Aiden Woodruff <aiden.woodruff@gmail.com>
##

import json
import sys

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = "percent.json"

with open(filename, "r") as r:
	a = json.load(r)
for i in a.keys():
	print(i, ":", a[i])

