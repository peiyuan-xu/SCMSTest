#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/3/14 21:52
@desc:
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams['font.family'] = ['Times New Roman']

x = [0, 25, 50, 100, 150, 200, 220, 240, 250, 350, 370, 400, 410]

fig, ax = plt.subplots()
plt.xlabel("Time(s)")
plt.ylabel("Container Number")

chain1 = [
    #0  25 50 100 150 200 220 240 250 350 370 400 410
    [1, 1, 2, 2,  2,  2,  2,  2,  2,  1,  0,  0,  0],
    [0, 0, 1, 2,  4,  4,  4,  4,  4,  4,  3,  1,  0],
    [0, 0, 0, 2,  2,  3,  4,  5,  6,  5,  5,  2,  1]
]
chain2 = [
    #0  25 50 100 150 200 220 240 250 350 370 400 410
    [1, 2, 3, 3,  3,  1,  0,  0,  0,  0,  0,  0,  0],
    [0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0, 0, 1, 2,  2,  3,  2,  1,  0,  0,  0,  0,  0]
]
plt.bar(left=x, height=[b1 for b1 in chain1[0]], width=5, label='Chain1 Books')
plt.bar(left=x, height=[b2 for b2 in chain2[0]], bottom=[b1 for b1 in chain1[0]], width=5, label='Chain2 Books')
plt.bar(left=[xt + 5 for xt in x], height=[r1 for r1 in chain1[1]], width=5, label='Chain1 Reviews')
# plt.bar(left=[xt + 5 for xt in x], height=[r2 for r2 in chain2[1]], bottom=[r1 for r1 in chain1[1]], width=5, label='Chain2 Reviews')
plt.bar(left=[xt + 10 for xt in x], height=[s1 for s1 in chain1[2]], width=5, label='Chain1 Score')
plt.bar(left=[xt + 10 for xt in x], height=[s2 for s2 in chain2[2]], bottom=[s1 for s1 in chain1[2]], width=5, label='Chain2 Score')

# plt.legend(bbox_to_anchor=(1.02, 0), loc=3, borderaxespad=0)
plt.legend(loc='upper left')
plt.xticks(range(0, 450, 50))
plt.yticks([0, 1, 2, 3, 4, 5, 6])
# fig.subplots_adjust(right=0.7)
plt.show()