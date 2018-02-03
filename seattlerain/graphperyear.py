#!/usr/bin/python3

##
## Make matplotlib graph from data, taking total inches of rain per year
## Uses Python 3, matplotlib, pandas, numpy
## Author: Aiden Woodruff <aiden.woodruff@gmail.com>
##

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

yearsum = [float(0)]*70
nacount = 0

with open('seattleWeather_1948-2017.csv', 'r', newline='') as seattlefile:
  seattleread = csv.DictReader(seattlefile)
  for row in seattleread:
    if (row['PRCP'] == "NA"):
      nacount += 1
    else:
      yearsum[int(row['DATE'][:4])-1948] += float(row['PRCP'])
    # print(int(str(row['DATE'])[:4])-1948)
    # print(str(float(row['PRCP'])) + "  " + row['DATE'])

years = np.arange(1948, 2018, 1, dtype=int)

totalyear = pd.DataFrame(np.column_stack([years, yearsum]), columns=['Year', 'Rainfall (in)'])

ax = totalyear.plot(x='Year', y='Rainfall (in)', label='Rainfall by Year (in)')
plt.title("Yearly Total Rainfall for Seattle")
plt.show()
