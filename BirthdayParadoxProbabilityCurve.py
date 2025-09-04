#! python3
import matplotlib.pyplot as plt
import numpy as np

# 初始化概率列表（对应 Mathematica 的 noshare 和 share）
noshare = []    # 存储所有人生日均不同的概率
share = []       # 存储至少两人生日相同的概率
current_noshare = 1.0  # 初始无重复的概率（对应 n=1 的情况）

# 模拟 n 从 1 到 50 人的情况（对应 Mathematica 的 For 循环）
for n in range(1, 51):
    if n == 1:
        # 初始情况：1 个人时无重复概率为 1
        noshare.append((1, 1.0))
        share.append((1, 0.0))
    else:
        # 计算新的乘积因子 (365 - (n-1))/365
        new_factor = (365 - (n - 1)) / 365
        # 更新当前无重复概率（递推公式）
        current_noshare *= new_factor
        
        # 记录当前 n 对应的无重复概率
        noshare.append((n, current_noshare))
        # 计算并记录至少两人生日相同的概率
        share.append((n, 1.0 - current_noshare))

# 提取数据点用于绘图（对应 ListPlot）
n_values = [x[0] for x in share]
prob_values = [x[1] for x in share]

# 绘制概率曲线（带标签和网格）
plt.figure(figsize=(10, 6))
plt.plot(n_values, prob_values, 'b-', linewidth=2)
plt.axhline(y=0.5, color='r', linestyle='--', alpha=0.5)  # 50% 参考线
plt.axvline(x=23, color='g', linestyle=':', alpha=0.5)    # 23人参考线

# 标记关键点（23人处概率 >50%）
plt.text(23, 0.02, 'n=23', rotation=90, verticalalignment='bottom')
plt.plot(23, 0.5073, 'ro')  # 理论值标记点
plt.annotate(f'50.73%', xy=(23, 0.5073), xytext=(30, 0.6),
             arrowprops=dict(arrowstyle="->"))

# 设置坐标轴和标题
plt.xlabel('Number of People (n)')
plt.ylabel('Probability of Shared Birthday')
plt.title('Birthday Paradox Probability Curve')
plt.grid(True, alpha=0.3)
plt.ylim(0, 1)

plt.savefig("BirthdayParadoxProbabilityCurve.png")