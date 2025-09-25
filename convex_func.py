#! python3

import numpy as np
import matplotlib.pyplot as plt

# 定义抛物线函数 (开口朝上，a>0)
def f(x):
    return x**2  # 简单二次函数，开口向上

# 生成x值范围
x_vals = np.linspace(-3, 3, 400)
y_vals = f(x_vals)

# 选择两个点x和y
x1 = -2.0
x2 = 2.0
y1 = f(x1)
y2 = f(x2)

# 计算中点坐标
x_mid = 0.5 * x1 + 0.5 * x2
y_mid_curve = f(x_mid)  # 抛物线上的点 f(0.5x+0.5y)
y_mid_line = 0.5 * f(x1) + 0.5 * f(x2)  # 直线上的点 0.5f(x)+0.5f(y)

# 创建连接两点的直线方程
def line_eq(x):
    return ((y2 - y1) / (x2 - x1)) * (x - x1) + y1

y_line = line_eq(x_vals)

# 设置绘图
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='Parabola f(x)=x²', color='blue', linewidth=2)
plt.plot(x_vals, y_line, label='Line between points', color='red', linestyle='--', linewidth=1.5)

# 标记关键点
plt.scatter([x1, x2], [y1, y2], color='green', s=80, zorder=5, label='Points (x,f(x)) and (y,f(y))')
plt.scatter(x_mid, y_mid_curve, color='purple', s=100, zorder=5, label='f(0.5x+0.5y) on parabola', marker='s')
plt.scatter(x_mid, y_mid_line, color='orange', s=100, zorder=5, label='0.5f(x)+0.5f(y) on line', marker='^')

# 添加点标注
plt.annotate(f'({x1}, {y1})', (x1, y1), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
plt.annotate(f'({x2}, {y2})', (x2, y2), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
plt.annotate(f'({x_mid:.1f}, {y_mid_curve:.1f})', (x_mid, y_mid_curve), textcoords="offset points", xytext=(0,-15), ha='center', fontsize=9)
plt.annotate(f'({x_mid:.1f}, {y_mid_line:.1f})', (x_mid, y_mid_line), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# 添加凸性说明箭头
plt.arrow(x_mid, y_mid_line, 0, y_mid_curve - y_mid_line, head_width=0.05, head_length=0.2, 
          fc='black', ec='black', linestyle=':', overhang=0.3, length_includes_head=True)
#plt.text(x_mid+0.3, (y_mid_line + y_mid_curve)/2, 'Convexity: f(tx+(1-t)y) ≤ tf(x)+(1-t)f(y)', 
#         fontsize=10, rotation=90, va='center')

# 设置图形属性
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Demonstration of Convex Function Definition', fontsize=14)
plt.legend(loc='upper center', fontsize=10)
plt.grid(True, alpha=0.3)
plt.axis([-3, 3, -1, 9])  # 设置坐标轴范围

plt.savefig('convex_func.png')