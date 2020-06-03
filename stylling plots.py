import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y,color='r',lw=10,alpha=0.5,linestyle='--')   #b-blue #r-red #lw=linewidth #alpha=opcity
plt.tight_layout()
plt.show()