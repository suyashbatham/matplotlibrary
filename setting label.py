import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y

#simple graph
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.set_xlabel('x-axis')
axes.set_ylabel('y-axis')
axes.set_title('the graph')  # the title
axes.plot(x,y)
plt.show()

# multiple graph
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.set_xlabel('x-axis')
axes.set_ylabel('y-axis')
axes.set_title('the graph outside')
axes2 = fig.add_axes([0.4,0.4,0.3,0.2])
axes2.set_xlabel('x-axis')
axes2.set_ylabel('y-axis')
axes2.set_title('the graph inside')
axes.plot(x,y)
axes2.plot(y,x)
plt.show()

# for subplots
fig,axes = plt.subplots(1,2)
axes[0].plot(x,y)
axes[0].set_xlabel('x-axis')
axes[0].set_ylabel('y-axis')
axes[0].set_title('the first graph')
axes[1].plot(y,x)
axes[1].set_xlabel('x-axis')
axes[1].set_ylabel('y-axis')
axes[1].set_title('the second graph')
plt.tight_layout()
plt.show()