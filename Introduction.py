import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x*x
print(y)
z = x + y
print(z)
plt.plot(x,y)
plt.show()
plt.plot(x,x)  # check the value
plt.show()
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()