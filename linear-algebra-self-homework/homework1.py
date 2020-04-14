import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1.920,2.080,160)

y1 = (x**9) - (18 * (x**8)) + (144 * (x**7)) - (672 * (x**6)) + (2016 * (x**5)) - (4032 * (x**4)) + (5376 * (x**3)) - (4608 * (x**2)) + (2304 * (x)) - 512

plt.plot(x, y1, label = 'method 1')


y2 = (x-2)**9
plt.plot(x, y2, label = 'method 2')
plt.legend()
plt.show()


# suppose this has to do with the stability of the algorithm based on
# what kind of floating point operations are being done.

