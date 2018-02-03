#!/usr/bin/python3

##
## Copy of family toolkit functions for 1/(x^2)
## Python 3 (or 2?), matplotlib, pandas, numpy
## Author: Aiden Woodruff <aiden.woodruff@gmail.com>
##


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Initialize variables
x = np.linspace(-20, 20, 1000)
y = np.reciprocal(np.square(x))
a = 1
b = 1
c = 1
d = 1

# modx = bx - c
modx = np.subtract(np.multiply(x, b), c)

# mody = a(mod^2)^-1 - d
mody = np.add(np.multiply(np.reciprocal(np.square(modx)), a), d)

# Create dataframe from variables
invsqr = pd.DataFrame(
        np.column_stack([x, y, mody]),
        columns=['x', 'y', 'transformed'])

# Graph Data
ax = invsqr.plot(x='x', y='y', label='f(x)=1/x^2')

# Graph asymptotes
ax.plot([0,0], [-10, 30], '--')
ax.plot([-20,20],[0,0],'--')

# Graph dimensions
plt.xlim(-20, 20)
plt.ylim(-10, 30)

# Graph scale
plt.xticks(np.arange(-20, 21, 2))
plt.yticks(np.arange(-10, 31, 2))

# Axes
plt.axhline(y = 0,linewidth=1, color='k', linestyle='-')
plt.axvline(x = 0,linewidth=1, color='k', linestyle='-')
plt.grid(True)

# Save as png and show
plt.savefig('graph1.png')
plt.show()

# Graph data
ax2 = invsqr.plot(x='x', y='transformed', label='a*f(bx-c)+d=1/x^2')

# Graph asymptotes
ax2.plot([1, 1], [-10,30],'--')
ax2.plot([-20,20],[1,1],'--')

# Set graph size
plt.xlim(-20, 20)
plt.ylim(-10, 30)

# Set scale
plt.xticks(np.arange(-20, 21, 2))
plt.yticks(np.arange(-10, 31, 2))

# Axes
plt.axhline(y = 0,linewidth=1, color='k', linestyle='-')
plt.axvline(x = 0,linewidth=1, color='k', linestyle='-')
plt.grid(True)

# Save as png and show
plt.savefig('graph2.png')
plt.show()
