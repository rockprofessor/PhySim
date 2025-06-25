import numpy as np
import matplotlib.pyplot as plt

def simulate_table_tennis_ball_flight(x, y, initial_vel, angle, time_step, max_time):
    g = 9.81  # Schwerkraft in m/s^2
    rho = 1.225  # Luftdichte in kg/m^3
    C_d = 0.47  # Luftwiderstandskoeffizient
    r = 0.02  # Radius des Tischtennisballs in m
    A = np.pi * r**2  # Querschnittsfläche in m^2
    mass = 0.0027  # Masse des Tischtennisballs in kg

    angle_rad = np.radians(angle)
    vx = initial_vel * np.cos(angle_rad)  # Anfangsgeschwindigkeit x-Richtung
    vy = initial_vel * np.sin(angle_rad)  # Anfangsgeschwindigkeit y-Richtung

    pos_x = [x]
    pos_y = [y]

    t = 0

    while y >= 0 and t < max_time:
        v = np.sqrt(vx**2 + vy**2)
        drag_force = 0.5 * rho * C_d * A * v**2

        ax = -drag_force * vx / (mass * v)
        ay = -g - (drag_force * vy / (mass * v))

        vx += ax * time_step
        vy += ay * time_step

        x += vx * time_step
        y += vy * time_step

        pos_x.append(x)
        pos_y.append(y)

        t += time_step
        if x > 3:
            print(v)

    return pos_x, pos_y

initial_vel = 50  # m/s
angle = 15  # Grad
initial_x = 1.25
initial_y = 0
step = 0.01
max_t = 5


pos_x, pos_y = simulate_table_tennis_ball_flight(initial_x, initial_y, initial_vel, angle, step, max_t)

plt.figure(figsize=(10, 5))
plt.plot(pos_x, pos_y, label="Flugbahn")
plt.title("Flugbahn eines Tischtennisballs")
plt.xlabel("Distanz (m)")
plt.ylabel("Höhe (m)")
plt.grid()
plt.legend()
plt.show()

