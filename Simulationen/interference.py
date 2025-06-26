import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button

# Parameters
x = np.linspace(0, 4 * np.pi, 1000)
k = 2 * np.pi / 1.0
omega = 2 * np.pi / 1.0
amplitude = 1.0
phase_shift = [0.0]  # Use list for mutable reference

# Set up figure and axes
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Make space for buttons

line1, = ax.plot([], [], label="Wave 1")
line2, = ax.plot([], [], label="Wave 2")
line_sum, = ax.plot([], [], label="Sum", color='black', linewidth=2)

ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-2.5, 2.5)
ax.legend()
ax.set_title("Interactive Wave Interference")
ax.set_xlabel("Position (x)")
ax.set_ylabel("Amplitude")

# Init function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line_sum.set_data([], [])
    return line1, line2, line_sum

# Animation function
def animate(t):
    y1 = amplitude * np.sin(k * x - omega * t)
    y2 = amplitude * np.sin(k * x - omega * t + phase_shift[0])
    y_sum = y1 + y2
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    line_sum.set_data(x, y_sum)
    return line1, line2, line_sum

# Button callback functions
def increase_phase(event):
    phase_shift[0] += np.pi / 8

def decrease_phase(event):
    phase_shift[0] -= np.pi / 8

# Buttons
ax_inc = plt.axes([0.7, 0.05, 0.1, 0.075])
ax_dec = plt.axes([0.55, 0.05, 0.1, 0.075])
btn_inc = Button(ax_inc, '+ Phase')
btn_dec = Button(ax_dec, '– Phase')

btn_inc.on_clicked(increase_phase)
btn_dec.on_clicked(decrease_phase)

# Animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 4, 200),
                              init_func=init, blit=True, interval=20)

plt.show()
