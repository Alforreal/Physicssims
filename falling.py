import matplotlib.pyplot as plt
import numpy as np

# Setting up:
t = 0 # s
dt = 0.0001 # s
g = 9.81 # m/s^2
m = 19 # kg
s = 10 # m
v = 0 # m/s
Rho = 1.293 # kg/m^3, air
r = 5*pow(10, -2) # m
Cw = 0.47 # BINAS 28A, sphere

# Info for plots:
x = []
y = []

# Intermediate calculations:
A = 2 * np.pi * pow(r, 2)

# main loop:
while True:
    t += dt
    # Krachten:
    Fz = m * g # zwaartekracht
    Fwl = 1/2 * Rho * Cw * A * pow(v, 2) # luchtwrijving
    Fn = -Fz + Fwl
    a = Fn / m
    # Modelleren:
    dv = a * dt
    v += dv
    ds = v * dt
    s += ds
    # Graphs:
    x.append(t)
    y.append(s)
    # Stop condition:
    if  s <= 0:
        break

# Plotting:
fig, ax = plt.subplots()
ax.plot(x,y)  
plt.show()