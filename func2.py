from turtle import color
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1.0, 1.01, 0.01)
y = 3 * x

plt.plot(x, y)
plt.grid(color='0.8')
plt.show()