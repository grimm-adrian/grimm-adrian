import matplotlib.pyplot as plt
import numpy as np
  
x = np.arange(0, 11)
y = np.sqrt((((6.67430*10**-11))*(1.498*10**10))/x)
plt.xlabel('r [meters]')
plt.ylabel('v [m/s]')
plt.title('Dependence of Orbital Speed on Distance')
plt.grid()
  
plt.plot(x, y, c='darkred')
plt.show()
plt.close()
