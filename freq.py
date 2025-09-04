#! python3

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 1. 符号计算导数（SymPy）
x_sym = sp.symbols('x')
y_sym = x_sym**(3/4)  # 定义符号函数
y_prime_sym = sp.diff(y_sym, x_sym)  # 符号导数计算

# 将符号函数转换为数值计算函数（NumPy）
y_func = sp.lambdify(x_sym, y_sym, 'numpy')
y_prime_func = sp.lambdify(x_sym, y_prime_sym, 'numpy')

# 2. 生成数据（优化精度与性能）
x_vals = np.linspace(0.01, 1000, 5000)  # 避免x=0的奇点
y_vals = y_func(x_vals)
y_prime_vals = y_prime_func(x_vals)

# 3. 创建图形对象（高清画布+多子图）
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), dpi=120, sharex=True)
plt.subplots_adjust(hspace=0.3)

# 4. 绘制原函数曲线
ax1.plot(x_vals, y_vals, 
         label=r'$y = x^{3/4}$', 
         color='#FF6D00',  # 橙色主曲线
         linewidth=2,
         alpha=0.8)
ax1.set_ylabel('Function Value', fontsize=12)
ax1.set_title(r'Function and Derivative: $y = x^{3/4}$', fontsize=14, pad=20)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper left', fontsize=12)

# 5. 绘制导数曲线
ax2.plot(x_vals, y_prime_vals, 
         label=r"$\frac{dy}{dx} = \frac{3}{4}x^{-1/4}$", 
         color='#2962FF',  # 蓝色导数曲线
         linewidth=2,
         alpha=0.8)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('Derivative Value', fontsize=12)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper right', fontsize=12)

# 6. 动态调整坐标轴范围
ax1.set_xlim(0, 1000)
ax1.set_ylim(0, np.max(y_vals)*1.05)
ax2.set_ylim(0, np.max(y_prime_vals)*1.1)

# 7. 添加关键点注释
critical_x = 100  # 选择典型点标注
ax1.annotate(f'Slope = {y_prime_func(critical_x):.2f}',
             xy=(critical_x, y_func(critical_x)),
             xytext=(critical_x+50, y_func(critical_x)/2),
             arrowprops=dict(arrowstyle="->", color='gray', lw=1.5),
             fontsize=10)

# 8. 保存高清图像
plt.savefig('freq.png', bbox_inches='tight', dpi=300)