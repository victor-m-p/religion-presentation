import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(1, 100, 10)
y = np.arange(1, 100, 10)

fig, ax = plt.subplots(dpi = 300)
plt.plot(x, y)
plt.savefig('test.svg')
plt.savefig('test.pdf')