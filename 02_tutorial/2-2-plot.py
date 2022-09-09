import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 40, 1)
y1 = -2 * x + 40
y2 = -(1/3) * x + (30/3)
plt.ylim([-1, 40])
plt.xlabel('x')
plt.ylabel('y',  rotation=0)
plt.grid()
plt.plot(x, y1, color="blue", label="2x + y <= 40")
plt.plot(x, y2, color="green", label="x + 3y <= 30")
plt.legend(loc=0)
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('02.png')
