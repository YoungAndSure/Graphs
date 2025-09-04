#! python3

import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.rand(20) * 10  # 第一组数据 (0~10范围)
data2 = np.random.rand(20) * 5 + 2  # 第二组数据 (2~7范围)

plt.figure(figsize=(10, 6))
plt.grid(True, linestyle='--', alpha=0.7)

plt.plot(data1, 
         color='red', 
         marker='o', 
         linewidth=2, 
         label='')

plt.plot(data2, 
         color='blue', 
         linestyle='--', 
         marker='s', 
         linewidth=2, 
         label='')

plt.title('', fontsize=14, pad=20)
plt.xlabel('', fontsize=12)
plt.ylabel('', fontsize=12)
plt.legend(loc='best', fontsize=10)

plt.xticks(range(0, len(data1), 2))
plt.ylim(0, 12)

plt.tight_layout()
plt.savefig('double_curve.png', dpi=300)