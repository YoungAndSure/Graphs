#! python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义二元函数
def g(x, y):
    return x**2 + 4*x*y + 4*y**2

# 生成坐标网格
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = g(X, Y)

# 创建画布和3D坐标轴[1,3](@ref)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制三维曲面图[1,3](@ref)
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, edgecolor='none')

# 设置坐标轴标签和标题[3,5](@ref)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('g(X, Y)')
ax.set_title('3D Surface Plot of g(x, y) = x² + 4xy + 4y²')

# 添加颜色条[1](@ref)
fig.colorbar(surf, shrink=0.5, aspect=10)

# 保存图像[9,10](@ref)
plt.savefig('convex_degree.png', dpi=300, bbox_inches='tight')