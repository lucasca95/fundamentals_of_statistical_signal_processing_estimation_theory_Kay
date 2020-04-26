# matplotlib permite graficar datos.
from matplotlib import pyplot as plt 
import numpy as np 
import sys



x = np.arange(1,11)
y = 2*x

# dibujar una recta
plt.plot(x, y)
plt.show()