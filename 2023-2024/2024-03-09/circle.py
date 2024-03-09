import numpy as np
import matplotlib.pyplot as plt

plt.axes().set_aspect("equal", "datalim")  # set the aspect ratio
thetas = np.linspace(0, 2 * 3.1416, 1000)
xs = np.cos(thetas)
ys = np.sin(thetas)

plt.plot(xs, ys)
plt.show()
