from mpl_toolkits import mplot3d
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

circle_r = 2
circle_x = 0
circle_y = 0
circle_z = 0

N = 2500

theta = np.pi*np.random.rand(N)
phi = 2 * np.pi * np.random.rand(N)
r = circle_r * np.random.rand(N)

ax = plt.axes(projection='3d')

x = r*np.sin(theta)*np.cos(phi)+circle_x
y = r*np.sin(theta)*np.sin(phi)+circle_y
z = r*np.cos(theta)+circle_z


u = np.sqrt(r)*np.sin(theta)*np.cos(phi)+circle_x
v = np.sqrt(r)*np.sin(theta)*np.sin(phi)+circle_y
w = np.sqrt(r)*np.cos(theta)+circle_z

plt.figure()
ax.plot3D(x, y, z, 'o', label='r', markersize=1)
#plt.set_xlim(-2, 2)
#plt.set_ylim(-3, 3)
#plt.zlim(-2,2)
#plt.legend()
ax = plt.axes(projection='3d')
#plt.figure()
ax.plot3D(u, v, w, 'o', label='$r^{1/2}$', markersize=1)
#plt.legend()

plt.show()
