#! python3

import numpy as np
import matplotlib.pyplot as plt

# 设置圆的参数
radius = 5
center = (0, 0)

# 生成圆上的点[5](@ref)
angles = np.linspace(0, 2 * np.pi, 100)
x_circle = center[0] + radius * np.cos(angles)
y_circle = center[1] + radius * np.sin(angles)

# 选择圆上两个点（例如对应角度30度和120度的位置）
theta1 = np.pi / 6  # 30度
theta2 = np.pi / 3  # 60度

point1 = (center[0] + radius * np.cos(theta1), center[1] + radius * np.sin(theta1))
point2 = (center[0] + radius * np.cos(theta2), center[1] + radius * np.sin(theta2))

# 计算两点连线的中点
midpoint = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# 创建图形和坐标轴[6](@ref)
fig, ax = plt.subplots(figsize=(8, 8))

# 绘制圆[6](@ref)
ax.plot(x_circle, y_circle, 'b-', label='convex set')

# 绘制两个点
ax.plot(point1[0], point1[1], 'ro', markersize=8, label='x')
ax.plot(point2[0], point2[1], 'go', markersize=8, label='y')

# 绘制两点之间的连线
ax.plot([point1[0], point2[0]], [point1[1], point2[1]], 'k-', linewidth=2, label='cx + (1-c)y')

# 绘制中点
ax.plot(midpoint[0], midpoint[1], 'mo', markersize=8, label='c=0.5')

# 添加标注
ax.annotate('x', xy=point1, xytext=(point1[0]+0.3, point1[1]+0.3), fontsize=12, color='red')
ax.annotate('y', xy=point2, xytext=(point2[0]+0.3, point2[1]+0.3), fontsize=12, color='green')
ax.annotate('c=0.5', xy=midpoint, xytext=(midpoint[0]+0.3, midpoint[1]+0.3), fontsize=12, color='purple')

# 设置图形属性
ax.set_aspect('equal')  # 确保圆不会变形[5](@ref)
ax.set_xlim(-radius-1, radius+1)
ax.set_ylim(-radius-1, radius+1)
ax.set_title('convex set example', fontsize=14)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend(loc='upper right')
ax.grid(True, linestyle='--', alpha=0.7)

plt.savefig("convex_set.png")