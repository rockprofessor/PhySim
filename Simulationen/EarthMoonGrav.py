import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M_earth = 5.972e24  # Mass of Earth, kg
M_moon = 7.348e22   # Mass of Moon, kg
distance = 384400e3  # Initial distance between Earth and Moon, m
moon_velocity = 0    # Moon initial velocity (stopped), m/s

# Time parameters
dt = 60  # Time step, seconds
total_time = 10 * 24 * 3600  # Total simulation time: 10 days, seconds

# Initial conditions
pos_earth = np.array([0.0, 0.0])  # Earth at the origin
pos_moon = np.array([distance, 0.0])  # Moon starts on the x-axis
vel_earth = np.array([0.0, 0.0])
vel_moon = np.array([0.0, moon_velocity])

# Lists to store position data
earth_positions = [pos_earth.copy()]
moon_positions = [pos_moon.copy()]

def gravitational_force(pos1, pos2, m1, m2):
    """Calculate the gravitational force between two masses."""
    r = np.linalg.norm(pos2 - pos1)
    if r == 0:
        return np.array([0.0, 0.0])  # Avoid division by zero
    force_magnitude = G * m1 * m2 / r**2
    direction = (pos2 - pos1) / r
    return force_magnitude * direction

# Simulation loop
steps = int(total_time / dt)
for _ in range(steps):
    # Calculate gravitational force
    force = gravitational_force(pos_earth, pos_moon, M_earth, M_moon)
    
    # Update velocities
    vel_earth += force / M_earth * dt
    vel_moon -= force / M_moon * dt  # Newton's third law: equal and opposite forces
    
    # Update positions
    pos_earth += vel_earth * dt
    pos_moon += vel_moon * dt
    
    # Store positions
    earth_positions.append(pos_earth.copy())
    moon_positions.append(pos_moon.copy())

# Convert position lists to numpy arrays
earth_positions = np.array(earth_positions)  # Shape: (frames, 2)
moon_positions = np.array(moon_positions)  # Shape: (frames, 2)

# Visualization setup
fig, ax = plt.subplots(figsize=(8, 8))

# Reduce frames to speed up animation
frames_to_skip = 100  # Use every 100th frame (can reduce this to slow down more)
earth_positions = earth_positions[::frames_to_skip]
moon_positions = moon_positions[::frames_to_skip]

# Animation objects
earth_dot, = ax.plot([], [], 'o', color='blue', label="Earth", markersize=10)
moon_dot, = ax.plot([], [], 'o', color='gray', label="Moon", markersize=5)
trail, = ax.plot([], [], '-', color='gray', lw=0.5, alpha=0.5)

# Animation update function
def update(frame):
    """Update animation for the current frame."""
    earth_x, earth_y = earth_positions[frame]
    moon_x, moon_y = moon_positions[frame]
    
    # Calculate the center of mass
    com_x = (M_earth * earth_x + M_moon * moon_x) / (M_earth + M_moon)
    com_y = (M_earth * earth_y + M_moon * moon_y) / (M_earth + M_moon)
    
    # Update axis limits to center the COM
    view_radius = 1.5 * distance
    ax.set_xlim(com_x - view_radius, com_x + view_radius)
    ax.set_ylim(com_y - view_radius, com_y + view_radius)
    
    # Update the positions of Earth and Moon
    earth_dot.set_data([earth_x], [earth_y])
    moon_dot.set_data([moon_x], [moon_y])
    trail.set_data(moon_positions[:frame, 0], moon_positions[:frame, 1])
    return earth_dot, moon_dot, trail

# Create the animation
anim = FuncAnimation(fig, update, frames=len(earth_positions), interval=50, blit=True)  # Adjusted speed
ax.legend()
plt.show()

