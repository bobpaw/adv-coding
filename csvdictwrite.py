#!/usr/bin/python3

##
## Write data to file to be read by associated reader
## Python 3
## Author: Aiden Woodruff <aiden.woodruff@gmail.com
##

import csv

with open('names.csv', 'w', newline='') as names:
  csvwriter = csv.DictWriter(names, fieldnames=['first_name', 'last_name', 'age'])
  csvwriter.writeheader()
  csvwriter.writerow({'first_name' : 'Aiden', 'last_name' : 'Woodruff', 'age' : 14})
  csvwriter.writerow({'first_name' : 'Jason', 'last_name' : 'Kolbly', 'age' : 14})
  csvwriter.writerow({'first_name' : 'Fiona', 'last_name' : 'Rubiano', 'age' : 13})
  csvwriter.writerow({'first_name' : 'Eleanor', 'last_name' : 'Johnson', 'age' : 13})
