#! python3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置随机种子保证可复现
np.random.seed(42)

# 创建3x3矩阵
A = np.array([[2, 1, 0],
              [1, 2, 1],
              [0, 1, 2]])

# 生成单位球面上的点
theta = np.linspace(0, np.pi, 30)
phi = np.linspace(0, 2*np.pi, 30)
theta, phi = np.meshgrid(theta, phi)
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)
sphere_points = np.vstack([x.flatten(), y.flatten(), z.flatten()])

# 应用原始矩阵变换
transformed_points = A @ sphere_points

# 进行SVD分解
U, S, VT = np.linalg.svd(A)
S_matrix = np.diag(S)

# 计算分解后的变换步骤
step1 = VT @ sphere_points           # 第一步：旋转/反射（V^T）
step2 = S_matrix @ step1             # 第二步：缩放（Σ）
step3 = U @ step2                    # 第三步：旋转/反射（U）

# 创建图形
fig = plt.figure(figsize=(20, 15))
plt.suptitle('SVD分解的几何解释：3x3矩阵的空间变换', fontsize=20)

# 1. 原始单位球面
ax1 = fig.add_subplot(231, projection='3d')
ax1.scatter(sphere_points[0], sphere_points[1], sphere_points[2], 
           alpha=0.3, c='b', marker='o')
ax1.set_title('1. 原始单位球面', fontsize=14)
ax1.quiver(0, 0, 0, 1, 0, 0, color='r', length=1.2)
ax1.quiver(0, 0, 0, 0, 1, 0, color='g', length=1.2)
ax1.quiver(0, 0, 0, 0, 0, 1, color='b', length=1.2)

# 2. 分解第一步：V^T旋转
ax2 = fig.add_subplot(232, projection='3d')
ax2.scatter(step1[0], step1[1], step1[2], 
           alpha=0.3, c='g', marker='o')
ax2.set_title('2. 旋转/反射 (V$^T$)', fontsize=14)
ax2.quiver(0, 0, 0, VT[0,0], VT[1,0], VT[2,0], color='r', length=1.2)
ax2.quiver(0, 0, 0, VT[0,1], VT[1,1], VT[2,1], color='g', length=1.2)
ax2.quiver(0, 0, 0, VT[0,2], VT[1,2], VT[2,2], color='b', length=1.2)

# 3. 分解第二步：Σ缩放
ax3 = fig.add_subplot(233, projection='3d')
ax3.scatter(step2[0], step2[1], step2[2], 
           alpha=0.3, c='m', marker='o')
ax3.set_title('3. 缩放 (Σ)', fontsize=14)
ax3.quiver(0, 0, 0, S[0], 0, 0, color='r', length=S[0]*1.2)
ax3.quiver(0, 0, 0, 0, S[1], 0, color='g', length=S[1]*1.2)
ax3.quiver(0, 0, 0, 0, 0, S[2], color='b', length=S[2]*1.2)

# 4. 分解第三步：U旋转
ax4 = fig.add_subplot(234, projection='3d')
ax4.scatter(step3[0], step3[1], step3[2], 
           alpha=0.3, c='c', marker='o')
ax4.set_title('4. 旋转/反射 (U)', fontsize=14)
ax4.quiver(0, 0, 0, U[0,0], U[1,0], U[2,0], color='r', length=1.2)
ax4.quiver(0, 0, 0, U[0,1], U[1,1], U[2,1], color='g', length=1.2)
ax4.quiver(0, 0, 0, U[0,2], U[1,2], U[2,2], color='b', length=1.2)

# 5. 原始矩阵变换结果
ax5 = fig.add_subplot(235, projection='3d')
ax5.scatter(transformed_points[0], transformed_points[1], transformed_points[2], 
           alpha=0.3, c='r', marker='o')
ax5.set_title('5. 原始矩阵变换结果 (A·X)', fontsize=14)

# 6. 分解后变换结果
ax6 = fig.add_subplot(236, projection='3d')
ax6.scatter(step3[0], step3[1], step3[2], 
           alpha=0.3, c='y', marker='o')
ax6.set_title('6. SVD分解后变换结果 (U·Σ·V$^T$·X)', fontsize=14)

# 设置视角和标签
for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.view_init(elev=20, azim=30)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.imsave("svd.png")

# 打印分解结果
print("原始矩阵 A:")
print(A)
print("\nSVD分解结果:")
print("U 矩阵:")
print(U)
print("\n奇异值矩阵 Σ:")
print(S_matrix)
print("\nV^T 矩阵:")
print(VT)
