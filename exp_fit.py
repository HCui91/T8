import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

time, temp = np.loadtxt('power.txt', unpack=True)

# Newton cooling law fitting
def TEMP_FIT(t, T0, k, Troom):
	print(T0, k, Troom)
	return(T0 * np.exp(-k*t) + Troom)

popt, pcov = curve_fit(TEMP_FIT, time, temp)

# Plotting
plt.figure()
plt.plot(time, temp, 'bo--',label='Heater off', alpha=0.5)
plt.plot(time, TEMP_FIT(time, *popt), label='Newton Cooling Law Fit')
plt.xlim(0, 303)
plt.xlabel('Time (second)')
plt.ylabel('Power (Walt)')
ax = plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.legend(fontsize=8)
plt.savefig('cooling.png', bbox_inches='tight')
plt.show()

print(popt,pcov)