import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

circle_r = 2
circle_x = 0
circle_y = 0

N = 5000

phi = 2 * np.pi * np.random.rand(N)
r = circle_r * np.random.rand(N)

x = r * np.cos(phi) + circle_x
y = r * np.sin(phi) + circle_y

w = np.sqrt(r) * np.cos(phi) + circle_x
z = np.sqrt(r) * np.sin(phi) + circle_y


#plt.scatter(x, y)
plt.figure()
plt.plot(x, y, 'o', label='r', markersize=1)
plt.xlabel(r"x", fontsize = 15)
plt.ylabel(r"y", fontsize = 15)
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.legend()

plt.figure()
plt.plot(w, z, 'o', label='$r^{1/2}$', markersize=1)
plt.xlabel(r"x", fontsize = 15)
plt.ylabel(r"y", fontsize = 15)
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.legend()

plt.show()
