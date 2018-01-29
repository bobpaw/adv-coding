##
## Reads file made by the associated `csvdictwrite.py` file and prints
## Author: Aiden Woodruff <aiden.woodruff@gmail.com>
##

#!/usr/bin/python3

import csv

with open('names.csv', 'r', newline='') as names:
  namereader = csv.DictReader(names)
  for row in namereader:
    print("First Name: " + row['first_name'])
    print("Last Name: " + row['last_name'])
    print("Age: " + row['age'])
