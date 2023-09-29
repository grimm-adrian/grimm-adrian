import matplotlib.pyplot as plt
import numpy as np

def bn(n):
    bn = 2*n-(1/3)+(4/(405*n))+(46/(25515*n**2))+(131/(1148175*n**3))-(2194697/(30690717750*n**4))
    return bn

x = np.arange(0.1, 6)
y = np.exp(-(bn(0.5))*(x**0.5-1))
plt.xlabel('r')
plt.ylabel('I(r)')
plt.title('Variation of I(r) in the Range 0.1 < r < 5')
plt.grid()
  
plt.plot(x, y, c='midnightblue')
plt.show()
plt.close()
