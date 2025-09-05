#! python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 设置随机种子以确保结果可重现
np.random.seed(42)

# 定义函数g(w) = w^3 - 5
def g(w):
    return w**3 - 5

# Robbins-Monro 算法参数
n_iterations = 51
initial_estimate = 0.0  # 初始估计值

# 初始化nws数组，用于存储迭代结果
nws = np.zeros(n_iterations)
etas = np.zeros(n_iterations)
nws[1] = 0.0

# 进行迭代计算
for i in range(2, n_iterations):
    eta = np.random.normal(loc=0, scale=1)
    
    noisy_observation = g(nws[i-1]) + eta
    
    step_size = 1/(i)
    step = step_size * noisy_observation
    nws[i] = nws[i-1] - step
    
    etas[i] = eta

# 打印最终估计值
print(f"Final estimate: {nws[n_iterations - 1]}")
print(f"True root: {5**(1/3)}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# 左图：绘制nws序列的收敛过程
iterations = np.arange(n_iterations)
ax1.plot(iterations, nws, color='green', linewidth=2, label='Robbins-Monro estimate sequence')
ax1.axhline(y=5**(1/3), color='red', linestyle='--', label='True root')
ax1.set_xlabel('Iteration', fontsize=12)
ax1.set_ylabel('Estimate value', fontsize=12)
ax1.set_title('Robbins-Monro Algorithm Convergence', fontsize=14)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# 右图：绘制g(w)函数和迭代点
w_range = np.linspace(-2, 3, 400)
g_values = g(w_range)
ax2.plot(w_range, g_values, 'b-', label='g(w) = w³ - 5', linewidth=2)
ax2.axhline(y=0, color='gray', linestyle='--', linewidth=1)

# 创建颜色映射以显示迭代过程
colors = cm.viridis(np.linspace(0, 1, n_iterations))

# 标注迭代点
for i in range(n_iterations):
    # 跳过初始点(0,0)
    if i == 0:
        continue
        
    # 绘制点
    ax2.scatter(nws[i], g(nws[i]), color=colors[i], s=50, alpha=0.7, zorder=5)
    
    # 每5次迭代或最后几次迭代添加标注
    if i % 5 == 0 or i > n_iterations - 5:
        ax2.annotate(f'{i}', xy=(nws[i], g(nws[i])), xytext=(5, 5), 
                    textcoords='offset points', fontsize=8, color=colors[i],
                    arrowprops=dict(arrowstyle='->', color=colors[i], alpha=0.7))

# 标注起点和终点
ax2.scatter(nws[1], g(nws[1]), color='red', s=100, marker='o', label='Start point', zorder=6)
ax2.scatter(nws[-1], g(nws[-1]), color='darkgreen', s=100, marker='s', label='End point', zorder=6)

ax2.set_xlabel('w', fontsize=12)
ax2.set_ylabel('g(w)', fontsize=12)
ax2.set_title('Function g(w) with Iteration Points', fontsize=14)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

# 调整布局并显示
plt.tight_layout()
plt.savefig("robbins_monro.png", dpi=300, bbox_inches='tight')
plt.show()

# 额外输出迭代信息
print("\nIteration details:")
for i in [0, 1, 2, 3, 4, 5, 10, 20, 30, 40, 49]:
    if i < n_iterations:
        print(f"Iteration {i}: w = {nws[i]:.6f}, g(w) = {g(nws[i]):.6f}")