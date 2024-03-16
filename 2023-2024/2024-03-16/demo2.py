import matplotlib.pyplot as plt

# import numpy as np
## patten-1
# from numpy import linspace
# from numpy import power
# from numpy import exp
## patten-2
# from numpy import linspace, power, exp
from numpy import (
    linspace,
    power,
    exp
)

## patten-3
from numpy import linspace, power, exp

xs = linspace(-5, 10, 10000)
y1s = xs
y2s = power(xs, 2)
y3s = power(xs, 3)
y4s = exp(xs)

plt.plot(xs, y1s, label="$y_1 = x$")
plt.plot(xs, y2s, label="$y_2 = x^2$")
plt.plot(xs, y3s, label="$y_3 = x^3$")
plt.plot(xs, y4s, label="$y_4 = e^x$")
# plt.xlim(0, 10)
plt.xlim(0, 3)
plt.ylim(0, 10)
plt.legend()
plt.show()
