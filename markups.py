import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y,marker='o',markersize=20,markerfacecolor='yellow',markeredgecolor='green',markeredgewidth=10)  # mark the particular point
plt.show()