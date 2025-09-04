#! python3

import numpy as np
import matplotlib.pyplot as plt

# 设置随机种子以确保结果可重现
np.random.seed(42)

# 定义函数g(w) = w^3 - 5
def g(w):
    return w**3 - 5

# Robbins-Monro 算法参数
n_iterations = 50
initial_estimate = 0.0  # 初始估计值

# 初始化nws数组，用于存储迭代结果
nws = np.zeros(n_iterations)
etas = np.zeros(n_iterations)
current_estimate = initial_estimate

# 进行迭代计算
for i in range(n_iterations):
    # 生成当前迭代的噪声：使用[-2, 2]均匀分布替代正态分布[6,7](@ref)
    eta = np.random.normal(loc=0, scale=1)
    
    # 计算当前估计点处的带噪声函数值
    noisy_observation = g(current_estimate) + eta
    
    # Robbins-Monro 更新步骤
    step_size = 1/(i+1)  # 确保不为零
    current_estimate = current_estimate - step_size * noisy_observation
    
    # 存储当前估计值
    nws[i] = current_estimate
    etas[i] = eta

# 打印最终估计值
print(f"Final estimate: {current_estimate}")
print(f"True root: {5**(1/3)}")

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制nws序列的曲线
iterations = np.arange(n_iterations)
plt.plot(iterations, nws, color='green', linewidth=2, label='Robbins-Monro estimate sequence')
#plt.plot(iterations, etas, color='green', linewidth=2, label='Robbins-Monro estimate sequence')
plt.axhline(y=5**(1/3), color='red', linestyle='--', label='True root')

plt.xlabel('Iteration', fontsize=12)
plt.ylabel('Estimate value', fontsize=12)
plt.title('Robbins-Monro Algorithm Estimate Sequence (Uniform Noise [-2, 2])', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# 调整布局并显示
plt.tight_layout()
plt.savefig("robbins_monro.png")