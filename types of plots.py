import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y

#1.scatter()
plt.scatter(x,y)
plt.show()

#2.hist()
plt.hist(x,y)
plt.show()

#3.bar()
plt.bar(x,y)
plt.show()

#4.fill()
plt.fill(x,y)
plt.show()

#5.pie()
plt.pie(x,y)
plt.show()

# all plots in one
plt.subplot(2,2,1)
plt.plot(x,y)
plt.subplot(2,2,2)
plt.hist(x,y)
plt.subplot(2,2,3)
plt.fill(x,y)
plt.subplot(2,2,4)
plt.bar(x,y)
plt.tight_layout()
plt.show()


#polar form
plt.polar(x,y)
plt.show()

