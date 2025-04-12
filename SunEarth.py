import matplotlib.pyplot as plt
import numpy as np

# Setting up:
t = 0 # s
dt = 24*3600 # s
G = 6.6743*10**(-11) # N*m^2/kg^2
mZ = 1.9884*10**(30) # kg, sun
mA = 5.972*10**(24) # kg, earth
r = 0.1496*10**(12) + 6.371*10**6 + 6.957*10**8 # m
x = 0
y = r
vX = np.sqrt(G*mZ/r) # m/s, comes from Fmpz = Fg
vY = 0

# for plotting:
xp = [x]
yp = [y]

# main loop:
while True:
    Fg = G * mA * mZ / pow(r, 2)
    # debugging:
    # print("Fg: " + str(Fg) + " vX: " + str(vX) + " vY: " + str(vY) + " x: " + str(x) + " y: " + str(y))
    # x direction:
    Fx = -Fg * x / r
    aX = Fx / mA
    dv = aX * dt
    vX += dv
    dx = vX * dt
    x += dx
    # y direction:
    Fy = -Fg * y / r
    aY = Fy / mA
    dv = aY * dt
    vY += dv
    dy = vY * dt
    y += dy
    # comping it back together:
    r = np.sqrt(pow(x, 2) + pow(y, 2))
    xp.append(x)
    yp.append(y)
    t += dt
    # stop condition:
    if t >= 366*24*3600: # seconds in a year
        break


# Plotting:
fig, ax = plt.subplots()
ax.plot(xp,yp)  
plt.show()
