import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y)
axes.set_xlim([0,6])
axes.set_ylim([0,60])
plt.show()