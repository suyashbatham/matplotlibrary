import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y
plt.subplot(3,2,1) #1-row #2-column #3no of curves
plt.plot(x,y)
plt.subplot(3,2,2)
plt.plot(x,x)
plt.subplot(3,2,3)
plt.subplot(3,2,4)
plt.subplot(3,2,5)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.subplot(3,2,6)
plt.plot(x,x)
plt.tight_layout() # it is a matplotlib method
plt.show()