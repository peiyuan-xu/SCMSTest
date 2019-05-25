#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/5/8 13:28
@desc:
"""

import numpy as np
from scipy.interpolate import spline

import matplotlib.pyplot as plt


plt.figure(1)


x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
y = [0, 5, 10, 20, 40, 70, 90, 40, 0, 0]
xnew = np.linspace(0, 80, 100)
power_smooth = spline(x, y, xnew)
plt.plot(xnew, power_smooth)

# 设置横纵坐标的名称以及对应字体格式
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 14,
         }
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 18,
         }

plt.xlabel("Time(s)", font1)
plt.ylabel("QPS", font1)

plt.tick_params(labelsize=14)
plt.xticks(range(0, 91, 20))
plt.yticks(range(0, 85, 20))
plt.tight_layout()
plt.savefig("../fig/fig_5_qps")
