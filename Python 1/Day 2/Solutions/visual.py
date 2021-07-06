import matplotlib.pyplot as plt
import numpy as np

years = np.arange(80)
deposit = 1000
procent = 5
result1 = deposit * (1 + procent/100) ** years
result2 = deposit + deposit * procent/100 * years
plt.plot(years, result1)
plt.plot(years, result2)
plt.show()