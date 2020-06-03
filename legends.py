import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y
plt.plot(x,y,label='first example')
# plt.legend()  # for title
plt.legend(loc=10)   #loc  value from  1-10 in which place you plcae the label
plt.show()