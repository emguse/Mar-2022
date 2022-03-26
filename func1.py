import matplotlib.pyplot as plt

x = list(range(1,11))
y = []
for i in range(10):
    y.append(3 * x[i] -24)

plt.plot(x, y)
plt.grid(color='0.8')
plt.show()