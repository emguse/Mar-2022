import matplotlib.pyplot as plt
import numpy as np

# Base line segment
a1 = (5 - 1) / (6 - 0)
b1 = 1

# Middle point
cx = (0 + 6) / 2
cy = (1 + 5) / 2

# Slope perpendicular to the line segment
a2 = -1 / a1

# Intercept of a line perpendicular to the line segment
b2 = cy - a2 * cx

x = np.arange(0, 7)
y1 = a1 * x + b1
y2 = a2 * x + b2

plt.plot(x, y1)
plt.plot(x, y2)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()