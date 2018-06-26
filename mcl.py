import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([-1, 0.2, 0.9, 2.1, 3.5, 4.2, 5.6])

z=sum (x*y)
w=sum(x**2)
r=sum(x)
s=sum(y)

a=((7*z)-(r*s))/((7*w)-(r**2))

b= ((s*w)-(r*z))/((7*w)-(r	**2))
print ("Pendiente =",a)
print ("Ordenada al origen =",b)

plt.plot(x, y, 'o', label='Datos', markersize=10)
plt.plot(x, a*x + b, 'r', label='Ajuste')
plt.xlabel(r"x", fontsize = 15)
plt.ylabel(r"y(x)", fontsize = 15)
plt.legend()
plt.show()
