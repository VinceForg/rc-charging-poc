import numpy as np
import matplotlib.pyplot as mpl
from matplotlib import pyplot as plt

#MACROS
V0 = 5.0                          #SUPPLY VOLTAGE
R = 10e3                          #RESISTANCE
C = 22e-12                        #CAPACITANCE

#VARIABLES
tau = R * C
V_tau = V0 * (1 - np.exp(-1))     #VOLTAGE AT ONE TIME CONSTANT
t = np.linspace(0, 5 * tau, 500)
V = V0 * (1 - np.exp(-t/tau))

#PLOTTING
fig, ax = plt.subplots()

#LINES
ax.plot(t, V, color = "black")
ax.axhline(y=V_tau, color = "red", linestyle = ":", label = "V(tau)")

#GRID, LABELS, TITLE
ax.grid(False)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")
ax.set_title(f"Capacitor charging (R = {R/1e3:.0f}k$\\Omega$, C = {C*1e12:.0f} pF)")

#DISPLAY/SAVE
fig.savefig("figures/generated/rc_charging.pdf")
plt.show()

#print("tau = ", tau, "s; V(tau) = ", V_tau,"V")


