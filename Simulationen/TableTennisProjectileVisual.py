import pygame
import numpy as np

def simulate_table_tennis_ball_flight(initial_velocity, launch_angle, time_step=0.01, max_time=5):
    """
    Simuliert den Flug eines Tischtennisballs unter Berücksichtigung von Schwerkraft und Luftwiderstand.
    Gibt die Positionen des Balls in einem Zeitintervall zurück.
    """
    # Konstanten
    g = 9.81  # Schwerkraft in m/s^2
    rho = 1.225  # Luftdichte in kg/m^3
    C_d = 0.47  # Luftwiderstandskoeffizient
    r = 0.02  # Radius des Tischtennisballs in m
    A = np.pi * r**2  # Querschnittsfläche in m^2
    mass = 0.0027  # Masse des Tischtennisballs in kg

    # Anfangswerte
    launch_angle_rad = np.radians(launch_angle)
    vx = initial_velocity * np.cos(launch_angle_rad)  # Anfangsgeschwindigkeit x-Richtung
    vy = initial_velocity * np.sin(launch_angle_rad)  # Anfangsgeschwindigkeit y-Richtung

    x, y = 0, 0  # Startposition

    positions = [(x, y)]

    t = 0

    while y >= 0 and t < max_time:
        # Luftwiderstand berechnen
        v = np.sqrt(vx**2 + vy**2)
        drag_force = 0.5 * rho * C_d * A * v**2

        # Beschleunigungen
        ax = -drag_force * vx / (mass * v)
        ay = -g - (drag_force * vy / (mass * v))

        # Geschwindigkeiten aktualisieren
        vx += ax * time_step
        vy += ay * time_step

        # Positionen aktualisieren
        x += vx * time_step
        y += vy * time_step

        positions.append((x, y))
        t += time_step

    return positions

# Pygame-Initialisierung
pygame.init()

# Fenstergröße (größeres Fenster)
screen_width = 1400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tischtennisball-Flugbahn")

# Farben
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Parameter der Simulation
initial_velocity = 15  # m/s
launch_angle = 45  # Grad
scale = 180  # Maßstab (Pixel pro Meter) - jetzt größer

positions = simulate_table_tennis_ball_flight(initial_velocity, launch_angle)

# Hauptschleife
clock = pygame.time.Clock()
running = True
index = 0

# Hintergrundnetz
def draw_grid():
    for x in range(0, screen_width, 50):
        pygame.draw.line(screen, black, (x, 0), (x, screen_height), 1)
    for y in range(0, screen_height, 50):
        pygame.draw.line(screen, black, (0, y), (screen_width, y), 1)

while running:
    screen.fill(white)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Zeichne Flugbahn (vergangene Positionen)
    for i in range(index):
        x, y = positions[i]
        screen_x = int(x * scale)
        screen_y = screen_height - int(y * scale)
        pygame.draw.circle(screen, blue, (screen_x, screen_y), 3)

    # Zeichne Ball an aktueller Position
    if index < len(positions):
        x, y = positions[index]
        screen_x = int(x * scale)
        screen_y = screen_height - int(y * scale)
        pygame.draw.circle(screen, red, (screen_x, screen_y), 8)  # Ball in Rot, größer dargestellt
        index += 1

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()

