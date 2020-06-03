import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y

# for plots
fig = plt.figure(figsize=(2,3)) #width,height
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y)
plt.show()

# for subplots
fig,axes = plt.subplots(1,2,figsize=(5,5))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.show()