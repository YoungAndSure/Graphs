#! python3

import numpy as np
import matplotlib.pyplot as plt
import math
import random

def birthdaycdf(num, days):
    # 初始化 numpeople 数组
    numpeople = [0] * (days + 1)
    
    # 模拟实验
    for n in range(num):
        share = False
        bdaylist = []
        k = 0
        
        while not share:
            # 生成随机生日
            x = random.randint(1, days)
            
            # 检查生日是否已存在
            if x in bdaylist:
                share = True
            else:
                bdaylist.append(x)
                
            k += 1
            
            # 记录重复生日事件
            if share:
                # 假如某次实验中当加到第100个人的时候，出现了两个人生日相同。
                # 那意味着101-365人，都会出现两个人生日相同。
                # 这个numpeople记录了第x天至少有两个人生日相同，在num次实验中的次数
                for d in range(k, days + 1):
                  numpeople[d] += 1
                        
    # 计算最大绘图范围
    max_val = int(3 * (0.5 + math.sqrt(days * math.log(4))))
    print(max_val)
    
    # 准备观测数据
    bdaylistplot = []
    for d in range(1, max_val + 1):
        prob = numpeople[d] / num
        bdaylistplot.append((d, prob))
    
    # 绘制观测概率图
    d_vals, probs = zip(*bdaylistplot)
    plt.figure(figsize=(10, 6))
    plt.plot(d_vals, probs, 'bo-', markersize=3)
    plt.xlabel('People')
    plt.ylabel('Probability')
    plt.title('Observed Probability of Birthday Sharing')
    plt.grid(True)
    plt.savefig("birthday2.png")

    # 计算并显示特定人数的概率
    target = math.floor(0.5 + math.sqrt(days * math.log(4)))
    if target <= days:
        target_prob = numpeople[target] * 100.0 / num
        print(f"Observed probability of success with 1/2 + sqrt(D·log(4)) people ({target} people) is {target_prob:.2f}%")
    else:
        print("Target value exceeds simulation range")
    
    # 定义理论函数
    def f(x):
        x_floor = math.floor(x)
        if x_floor >= days:
            return 1.0
        product = 1.0
        for k in range(0, x_floor + 1):
            product *= (1 - k / days)
        return 1 - product
    
    # 准备理论曲线数据
    x_vals = np.linspace(1, max_val, 500)
    y_vals = [f(x) for x in x_vals]
    
    # 绘制理论曲线与观测值对比
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, 'r-', label='Theoretical Prediction')
    plt.plot(d_vals, probs, 'bo', markersize=3, label='Observed Data')
    plt.xlabel('People')
    plt.ylabel('Probability')
    plt.title('Theoretical vs Observed Probability')
    plt.legend()
    plt.grid(True)
    plt.savefig("birthday2.png")
    
'''
    # 准备理论数据点
    theory_data = [(d, f(d)) for d in range(1, max_val + 1)]
    theory_d, theory_probs = zip(*theory_data)
    
    # 绘制理论与观测数据点对比
    plt.figure(figsize=(10, 6))
    plt.plot(d_vals, probs, 'bo', markersize=3, label='Observed Data')
    plt.plot(theory_d, theory_probs, 'r.', markersize=3, label='Theoretical Points')
    plt.xlabel('People')
    plt.ylabel('Probability')
    plt.title('Theoretical vs Observed Probability Points')
    plt.legend()
    plt.grid(True)
    plt.savefig("birthday2.png")
'''

# 示例使用（365天，模拟10000次）
birthdaycdf(10000, 365)