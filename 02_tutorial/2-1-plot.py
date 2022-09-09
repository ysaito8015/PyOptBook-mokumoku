import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 13, 0.1)
y1 = -x + 10
y2 = -(120/150) * x + (1440/150)
plt.ylim([0, 10])
plt.xlabel('x')
plt.ylabel('y',  rotation=0)
plt.grid()
plt.plot(x, y1, color="blue", label="x + y = 10")
plt.plot(x, y2, color="green", label="120x + 150y = 1440")
plt.legend(loc=0)
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('01.png')
