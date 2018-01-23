##
## Copy of family toolkit functions for 1/(x^2)
## Python version... shouldn't? matter for this one
## Requires pandas and matplotlib to be installed
## Author: Aiden Woodruff <aiden.woodruff@gmail.com>
##


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
x = np.linspace(-20, 20, 1000)
y = np.reciprocal(np.square(x))
a = 1
b = 1
c = 1
d = 1
modx = np.subtract(np.multiply(x, b), c)
mody = np.add(np.multiply(np.reciprocal(np.square(modx)), a), d)
invsqr = pd.DataFrame(
        np.column_stack([x, y, mody]),
        columns=['x', 'y', 'transformed'])

ax = invsqr.plot(x='x', y='y', label='f(x)=1/x^2')
ax.plot([0,0], [-10, 30], '--')
ax.plot([-20,20],[0,0],'--')
plt.xlim(-20, 20)
plt.ylim(-10, 30)
plt.xticks(np.arange(-20, 21, 2))
plt.yticks(np.arange(-10, 31, 2))
plt.axhline(y = 0,linewidth=1, color='k', linestyle='-')
plt.axvline(x = 0,linewidth=1, color='k', linestyle='-')
plt.grid(True)
plt.savefig('graph1.png')
plt.show()
ax2 = invsqr.plot(x='x', y='transformed', label='a*f(bx-c)+d=1/x^2')
ax2.plot([1, 1], [-10,30],'--')
ax2.plot([-20,20],[1,1],'--')
plt.xlim(-20, 20)
plt.ylim(-10, 30)
plt.xticks(np.arange(-20, 21, 2))
plt.yticks(np.arange(-10, 31, 2))
plt.axhline(y = 0,linewidth=1, color='k', linestyle='-')
plt.axvline(x = 0,linewidth=1, color='k', linestyle='-')
plt.grid(True)


plt.savefig('graph2.png')
plt.show()
