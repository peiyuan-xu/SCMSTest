#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/5/7 16:03
@desc:
"""

# figure 1 qps曲线为测试

import numpy as np
from scipy.interpolate import spline

import matplotlib.pyplot as plt


#设置输出的图片大小
figure, ax = plt.subplots()

x = [0, 10, 20, 30, 40]
y = [0, 5, 10, 20, 5]
xnew = np.linspace(0, 40, 300)
power_smooth = spline(x, y, xnew)
plt.plot(xnew, power_smooth)

# 设置横纵坐标的名称以及对应字体格式
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 21,
         }

plt.xlabel("Time(s)", font2)
plt.ylabel("QPS", font2)
plt.tick_params(labelsize=18)
plt.xticks(range(0, 41, 10))
plt.yticks(range(0, 21, 5))
plt.tight_layout()
plt.savefig("../fig/fig_1_qps")
