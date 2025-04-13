import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from qbstyles import mpl_style
from time import sleep
from rich.console import Console

plt.style.use('dark_background')
mpl_style(True)

x = [1,3,5,7]
y = [0.024, 0.0242, 0.026, 0.0265]

plt.plot(x[0:2],y[0:2], c='orange', ls='--', alpha=0.6)
plt.plot(x[1:3],y[1:3], c='orange')
plt.scatter(x[1:3],y[1:3],c='orange')
plt.plot(x[2:4],y[2:4], c='orange', ls='--', alpha=0.6)

plt.annotate("$y_{i}^{''}$", (x[1],y[1]), textcoords="offset points", xytext=(18,-8), ha='right', fontsize='x-large', fontweight='bold')
plt.annotate("$y_{i+1}^{''}$", (x[2],y[2]), textcoords="offset points", xytext=(30,-15), ha='right', fontsize='x-large', fontweight='bold')


plt.ylim(0.023,0.0275)
plt.savefig('imgs/piecewise_linear.svg')
plt.show()
