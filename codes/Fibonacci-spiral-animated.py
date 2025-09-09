## This code uses matplotlib to animate particles radiating outward from the origin in a golden-angle spiral, spaced by Fibonacci numbers.
## To run this:

# Make sure you have matplotlib installed (pip install matplotlib)

# Run the script in a Python environment that supports GUI (e.g., Jupyter Notebook or local IDE)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_particles = 100
golden_angle = np.pi * (3 - np.sqrt(5))  # ≈ 137.5 degrees in radians
fibonacci = [0, 1]
for i in range(2, num_particles):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# Generate spiral coordinates
radii = np.array(fibonacci[:num_particles])
angles = np.arange(num_particles) * golden_angle
x = radii * np.cos(angles)
y = radii * np.sin(angles)

# Animation setup
fig, ax = plt.subplots()
scat = ax.scatter([], [], s=50, c='cyan')
ax.set_xlim(-max(radii)*1.1, max(radii)*1.1)
ax.set_ylim(-max(radii)*1.1, max(radii)*1.1)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.set_title("Fibonacci Spiral Radiation", color='white')
ax.tick_params(colors='white')

def update(frame):
    scat.set_offsets(np.c_[x[:frame], y[:frame]])
    return scat,

ani = animation.FuncAnimation(fig, update, frames=num_particles, interval=100, blit=True)
plt.show()
