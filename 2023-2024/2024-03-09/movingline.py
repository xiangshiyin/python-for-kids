import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.linspace(-10, 10, 1000)
(line,) = ax.plot(x, x)


ax.axvline(x=0, c="red", label="x=0")
ax.axhline(y=0, c="yellow", label="y=0")


def animate(i):
    line.set_ydata(x + i / 10)  # update the data
    return (line,)


ani = animation.FuncAnimation(fig, animate, frames=100, interval=1000, blit=True)
plt.show()
