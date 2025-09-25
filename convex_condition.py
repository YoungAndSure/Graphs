#!python3

import matplotlib.pyplot as plt
import numpy as np

# 定义函数 f(x) = x^2
def f(x):
    return x**2

# 生成x轴数据点
x = np.linspace(-10, 10, 400)  # 在[-10, 10]区间生成400个等距点[1,2](@ref)
y = f(x)

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制函数曲线
ax.plot(x, y, label='y = x^2', color='blue', linewidth=2)

# 选择两个点 x1 和 x2
x1 = -5
x2 = 7.5

# 计算对应的y值
y1 = f(x1)
y2 = f(x2)

# 计算 f(y)-f(x) 和 2x*(y-x)
# 注意：这里用户表述可能有歧义，按照数学惯例，应该是 f(x2)-f(x1) 和 f'(x1)*(x2-x1)
f_diff = f(x2) - f(x1)  # f(y)-f(x)
tangent_approx = 2 * x1 * (x2 - x1)  # 2x*(y-x)，这是f在x处的切线在y点的近似值

# 绘制选中的两个点
ax.scatter([x1, x2], [y1, y2], color='red', s=50, zorder=5)
ax.annotate(f'x1={x1}', (x1, y1), textcoords="offset points", xytext=(0,10), ha='center')
ax.annotate(f'x2={x2}', (x2, y2), textcoords="offset points", xytext=(0,10), ha='center')

# 绘制连接两点的线段
ax.plot([x1, x2], [y1, y2], color='green', linestyle='--', linewidth=2, label=f'f(x2)-f(x1) = {f_diff}')

# 绘制在x1处的切线（用于表示2x*(y-x)的含义）
tangent_x = np.array([x1 - 5, x1 + 5])
tangent_y = 2*x1*tangent_x - x1**2  # 切线方程: y = f'(x1)(x - x1) + f(x1)
ax.plot(tangent_x, tangent_y, color='orange', linestyle=':', linewidth=2, 
        label=f'Tangent at x1 (slope = {2*x1})')

# 标记 2x*(y-x) 的值
ax.annotate(f'2x1*(x2-x1) = {tangent_approx}', 
            xy=((x1+x2)/2, (y1+y2)/2), 
            xytext=((x1+x2)/2, (y1+y2)/2 - 5),
            arrowprops=dict(arrowstyle="->", color='orange'),
            color='orange', ha='center')

# 添加标签和标题
ax.set_title('Function y = x^2 with Selected Points')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)

# 显示图像
plt.savefig('convex_condition.png')