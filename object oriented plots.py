import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y
# plt.plot(x,y)

#create another plt with using plt command
fig = plt.figure()
axes  =fig.add_axes([0.1,0.1,0.2,0.3])  #start,end,height,width
axes.plot(x,y)
plt.show()