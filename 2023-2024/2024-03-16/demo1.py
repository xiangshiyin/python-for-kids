import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(-5, 10, 10000)
y1s = xs
y2s = np.power(xs, 2)
y3s = np.power(xs, 3)
y4s = np.exp(xs)

plt.plot(xs, y1s, label="$y_1 = x$")
plt.plot(xs, y2s, label="$y_2 = x^2$")
plt.plot(xs, y3s, label="$y_3 = x^3$")
plt.plot(xs, y4s, label="$y_4 = e^x$")
# plt.xlim(0, 10)
plt.xlim(0, 3)
plt.ylim(0, 10)
plt.legend()
plt.show()

# matplotlib.pyplot.plot(xs, y1s, label="$y_1 = x$")
# matplotlib.pyplot.plot(xs, y2s, label="$y_2 = x^2$")
# matplotlib.pyplot.plot(xs, y3s, label="$y_3 = x^3$")
# matplotlib.pyplot.plot(xs, y4s, label="$y_4 = e^x$")
# # matplotlib.pyplot.xlim(0, 10)
# matplotlib.pyplot.xlim(0, 3)
# matplotlib.pyplot.ylim(0, 10)
# matplotlib.pyplot.legend()
# matplotlib.pyplot.show()
