#! python3

import numpy as np
import matplotlib.pyplot as plt

# Set annulus parameters: inner radius and outer radius
inner_radius = 2
outer_radius = 5
center = (0, 0)

# Generate boundary points of the annulus (non-convex set)
angles = np.linspace(0, 2 * np.pi, 100)
# Outer circle
x_outer = center[0] + outer_radius * np.cos(angles)
y_outer = center[1] + outer_radius * np.sin(angles)
# Inner circle
x_inner = center[0] + inner_radius * np.cos(angles)
y_inner = center[1] + inner_radius * np.sin(angles)

# Select two points on the outer boundary of the annulus (e.g., at 30 and 150 degrees)
theta1 = np.pi / 6  # 30 degrees
theta2 = 5 * np.pi / 6  # 150 degrees (corrected)

point1 = (center[0] + outer_radius * np.cos(theta1), center[1] + outer_radius * np.sin(theta1))
point2 = (center[0] + outer_radius * np.cos(theta2), center[1] + outer_radius * np.sin(theta2))

# Calculate the midpoint of the line connecting the two points
midpoint = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# 生成开口向下的抛物线数据点
# 使用抛物线方程 y = -0.2*(x)^2 + 4，确保y值始终大于内圆半径(2)且小于外圆半径(5)
x_parabola = np.linspace(-4, 4, 200)  # 调整x范围以适应开口向下的抛物线
y_parabola = 0.2 * (x_parabola)**2 - 4  # 顶点在(0,4)，位于环形区域内

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 8))

# Draw the annulus (filled area represents the non-convex set)
# Draw outer circle boundary
ax.plot(x_outer, y_outer, 'b-')
# Draw inner circle boundary
ax.plot(x_inner, y_inner, 'b-')
# Fill the annular region (area between outer and inner circles)
ax.fill_between(x_outer, y_outer, color='blue', alpha=0.1, edgecolor=None) # First fill the entire outer circle area
ax.fill_between(x_inner, y_inner, color='white', alpha=1, edgecolor=None) # Then fill the inner circle area with white to "dig" out the hole

# 绘制抛物线 (红色曲线)
ax.plot(x_parabola, y_parabola, 'r-', linewidth=2, label='Parabola: y=-0.2x²+4')

# Set graph properties
ax.set_aspect('equal')  # Ensure the graph doesn't deform
ax.set_xlim(-outer_radius-1, outer_radius+1)
ax.set_ylim(-outer_radius-1, outer_radius+1)
ax.set_title('Non-Convex Set Example: Annulus with Downward-Opening Parabola', fontsize=14)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend(loc='upper right')
ax.grid(True, linestyle='--', alpha=0.7)

plt.savefig("not_convex_set_with_parabola.png")