import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def external_force(x, v):
    ro = 1.025
    g = 9.81
    drag_coefficient = 10  
    pressure = ro * 9.81 * x[2]
    velocity_magnitude = np.linalg.norm(v)
    cross_sectional_area = 1.0 
    fluid_drag_force = -0.5 * drag_coefficient * velocity_magnitude**2 * cross_sectional_area * pressure / velocity_magnitude

    # Calculate gravitational force
    gravity_force = np.array([0.0, 0.0, -m * g])   

    # Add gravity force to the vector
    external_force_vector = fluid_drag_force + gravity_force
    
    return external_force_vector

def rk4_step(x, v, dt, m, external_force):

    k1_vx, k1_vy, k1_vz = external_force(x, v)
    k1_vx /= m
    k1_vy /= m
    k1_vz /= m
    k1_x = v[0]
    
    k2_vx, k2_vy, k2_vz = external_force(x + 0.5 * dt * k1_x, v + 0.5 * dt * np.array([k1_vx, k1_vy, k1_vz]))
    k2_vx /= m
    k2_vy /= m
    k2_vz /= m
    k2_x = v[0] + 0.5 * dt * k1_vx
    
    k3_vx, k3_vy, k3_vz = external_force(x + 0.5 * dt * k2_x, v + 0.5 * dt * np.array([k2_vx, k2_vy, k2_vz]))
    k3_vx /= m
    k3_vy /= m
    k3_vz /= m
    k3_x = v[0] + 0.5 * dt * k2_vx

    k4_vx, k4_vy, k4_vz = external_force(x + dt * k3_x, v + dt * np.array([k3_vx, k3_vy, k3_vz]))
    k4_vx /= m
    k4_vy /= m
    k4_vz /= m
    k4_x = v[0] + dt * k3_vx
    
    x_new = x + (dt / 6) * (k1_x + 2 * (k2_x + k3_x) + k4_x)
    v_new = v + (dt / 6) * np.array([k1_vx + 2 * (k2_vx + k3_vx) + k4_vx,
                                     k1_vy + 2 * (k2_vy + k3_vy) + k4_vy,
                                     k1_vz + 2 * (k2_vz + k3_vz) + k4_vz])
    
    return x_new, v_new

#Test
x0 = np.array([0.0, 0.0, 0.0]) 
v0 = np.array([1.0, 0.1, 2.0]) 
dt = 0.1 
m = 1.0 

num_steps = 100

positions = [x0]
velocities = [v0]

x = x0
v = v0
for i in range(num_steps):
    x, v = rk4_step(x, v, dt, m, external_force)
    positions.append(x)
    velocities.append(v)
    v[1] += dt * v[1]

positions = np.array(positions)
velocities = np.array(velocities)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], label='Trajectory')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
