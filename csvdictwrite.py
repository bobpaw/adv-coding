##
## Write data to file to be read by associated reader
## Author: Aiden Woodruff <aiden.woodruff@gmail.com
##

#!/usr/bin/python3

import csv

with open('names.csv', 'w', newline='') as names:
  csvwriter = csv.DictWriter(names, fieldnames=['first_name', 'last_name', 'age'])
  csvwriter.writeheader()
  csvwriter.writerow({'first_name' : 'Aiden', 'last_name' : 'Woodruff', 'age' : 14})
  csvwriter.writerow({'first_name' : 'Jason', 'last_name' : 'Kolbly', 'age' : 14})
  csvwriter.writerow({'first_name' : 'Fiona', 'last_name' : 'Rubiano', 'age' : 13})
  csvwriter.writerow({'first_name' : 'Eleanor', 'last_name' : 'Johnson', 'age' : 13})
