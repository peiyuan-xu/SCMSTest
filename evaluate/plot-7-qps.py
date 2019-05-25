#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/5/8 14:42
@desc:
"""

#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/3/15 22:06
@desc:
"""

import numpy as np
from scipy.interpolate import spline
import matplotlib.pyplot as plt

plt.figure(1)

x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y = [0, 5, 10, 40, 80, 80, 80,  80, 70, 20, 0]
y2 = [t/2 for t in y]
xnew = np.linspace(0, 100, 50)
power_smooth = spline(x, y, xnew)
power_smooth2 = spline(x, y2, xnew)
plt.plot(xnew, power_smooth, linestyle='--', marker='o', label='Chain1')
plt.plot(xnew, power_smooth2, linestyle='--', marker='>', label='Chain2')

# 设置横纵坐标的名称以及对应字体格式
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 14,
         }
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 13,
         }

plt.xlabel("Time(s)", font1)
plt.ylabel("QPS", font1)

plt.tick_params(labelsize=14)
plt.xticks(range(0, 111, 20))
plt.yticks(range(0, 95, 20))
plt.legend(loc='upper left', prop=font2)
plt.tight_layout()
plt.savefig("../fig/fig_7_qps")
