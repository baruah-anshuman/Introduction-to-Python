import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants and Parameters
length = 2
k = 0.466
temp_left = 200
temp_right = 200
total_time = 4

dx = 0.1
x_vec = np.linspace(0, length, int(length / dx))

dt = 0.0001
t_vec = np.linspace(0, total_time, int(total_time / dt))

u = np.zeros([len(t_vec), len(x_vec)])
u[:, 0] = temp_left
u[:, -1] = temp_right

# Time Integration
for t in range(1, len(t_vec) - 1):
    for x in range(1, len(x_vec) - 1):
        u[t + 1, x] = k * (dt / dx**2) * (u[t, x + 1] - 2 * u[t, x] + u[t, x - 1]) + u[t, x]

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlabel('Distance Along Rod (m)')
ax.set_ylabel('Time (s)')
ax.set_title('Temperature Distribution Along the Rod Over Time')

# Initialize the heatmap plot
heatmap = ax.imshow(u[0:2], aspect='auto', cmap='hot', origin='lower',
                     extent=[x_vec[0], x_vec[-1], t_vec[0], t_vec[1]])

# Update function for animation
def update(frame):
    heatmap.set_array(u[frame:frame+2])
    return heatmap,

# Create animation
ani = FuncAnimation(fig, update, frames=len(t_vec)-1, interval=10, blit=True)

plt.colorbar(heatmap, label='Temperature (°C)')
plt.show()
