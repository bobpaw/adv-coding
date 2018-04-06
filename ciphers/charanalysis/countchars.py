#!/usr/bin/python3

##
## Pull pages and write character statistics to JSON file.
## Runs in Python 3
## Author: Aiden Woodruff <aiden.woodruff@gmail.com>
##

from bs4 import BeautifulSoup
import requests
import string
import json
import sys

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = "percent.json"

alphabet_dict = dict.fromkeys(list(string.ascii_uppercase), 0)
total = 0

for pages in ['https://en.wikipedia.org/wiki/String_theory', 'https://sallysbakingaddiction.com/homemade-salted-caramel-recipe/', 'https://en.wikipedia.org/wiki/Richard_Nixon', 'https://en.wikipedia.org/wiki/Caramel', 'https://en.wikipedia.org/wiki/Abraham_Lincoln']:
	r = requests.get(pages)
	soup = BeautifulSoup(r.content, 'html.parser')
	text = soup.get_text().strip(' \n').upper()
	for i in alphabet_dict.keys():
		alphabet_dict[i] += text.count(i)
		total += text.count(i)

for i in alphabet_dict.keys():
	alphabet_dict[i] /= total
	alphabet_dict[i] *= 100
	alphabet_dict[i] = str(alphabet_dict[i])[:str(alphabet_dict[i]).index('.')+3] + "%"

with open(filename, "w") as f:
	json.dump(alphabet_dict, f)
