import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y

fig , axes = plt.subplots(1,2)   # row,column
axes[0].plot(x,y)
axes[1].plot(y,x)


fig , axes = plt.subplots(2,2)
axes[(1,1)].plot(x,y)  #row,column
axes[(0,1)].plot(y,x)
plt.tight_layout()
plt.show()