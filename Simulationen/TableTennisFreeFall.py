import numpy as np
import matplotlib.pyplot as plt

# Parameter
g = 9.81  # Erdbeschleunigung (m/s^2)
m = 0.0027  # Masse des Tischtennisballs (kg)
rho = 1.225  # Luftdichte (kg/m^3)
r = 0.02  # Radius des Tischtennisballs (m)
A = np.pi * r**2  # Querschnittsfläche (m^2)
cd = 0.47  # Luftwiderstandskoeffizient

# Simulationseinstellungen
dt = 0.01  # Zeitschritt (s)
dv = 100

# Initialwerte
v = 0  # Anfangsgeschwindigkeit (m/s)
t = 0  # Startzeit (s)

# Listen für die Ergebnisse
times = [t]
velocities = [v]

# Simulation des freien Falls
while dv > 0.0005:
    F_gravity = m * g  # Gravitationskraft (N)
    F_drag = 0.5 * cd * rho * A * v**2  # Luftwiderstand (N)
    F_net = F_gravity - F_drag  # Nettokraft (N)
    a = F_net / m  # Beschleunigung (m/s^2)
    
    # Aktualisierung von Geschwindigkeit und Zeit
    v = v + a * dt
    t = t + dt

    # Ergebnisse speichern
    velocities.append(v)
    times.append(t)
    dv = velocities[-1] - velocities[-2]

# Plotten der Ergebnisse
plt.plot(times, velocities, label="Geschwindigkeit", color="blue")
plt.title("Zeitlicher Verlauf der Geschwindigkeit beim freien Fall")
plt.xlabel("Zeit (s)")
plt.ylabel("Geschwindigkeit (m/s)")
plt.grid(True)
plt.legend()
plt.show()

