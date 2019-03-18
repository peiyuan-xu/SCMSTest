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
plt.rcParams['font.family'] = ['Times New Roman']


plt.figure(1)
plt.xlabel("Time(s)")
plt.ylabel("QPS")

x = [0, 10, 20, 30, 40, 50, 60, 70, 80]
y = [0, 5, 10, 40, 80, 80, 80,  80, 80]
y2 = [t/2 for t in y]
xnew = np.linspace(0, 80, 300)
power_smooth = spline(x, y, xnew)
power_smooth2 = spline(x, y2, xnew)
plt.plot(xnew, power_smooth,  label='Chain1')
plt.plot(xnew, power_smooth2, label='Chain2')

plt.yticks(range(0, 100, 10))
plt.legend()
plt.show()
