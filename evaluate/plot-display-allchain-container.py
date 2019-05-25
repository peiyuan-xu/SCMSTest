#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/5/8 15:03
@desc:
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


base_time =
all_con = [


]


g_x_time = [[base_time], [base_time], [base_time]]
g_y_con_num = [[0], [0], [0]]
g_x2_time = [[base_time], [base_time], [base_time]]
g_x2_con_num = [[0], [0], [0]]


def statistics_number(chain_name, all_con, x_time, y_con_num):
    for d in all_con:
        if d.get('chain') != chain_name:
            continue
        x_t = (d.get('start_t'))
        if d.get('service') == 'books':
            tmp = y_con_num[0][-1]
            if d.get('tag') == 'add':
                tmp += 1
            else:
                tmp -= 1
            y_con_num[0].append(tmp)
            x_time[0].append(x_t)
        elif d.get('service') == 'reviews':
            tmp = y_con_num[1][-1]
            if d.get('tag') == 'add':
                tmp += 1
            else:
                tmp -= 1
            y_con_num[1].append(tmp)
            x_time[1].append(x_t)
        elif d.get('service') == 'score':
            tmp = y_con_num[2][-1]
            if d.get('tag') == 'add':
                tmp += 1
            else:
                tmp -= 1
            y_con_num[2].append(tmp)
            x_time[2].append(x_t)
    return x_time, y_con_num


g_x_time, g_y_con_num = statistics_number('chain1', all_con, g_x_time, g_y_con_num)
g_x2_time, g_x2_con_num = statistics_number('chain2', all_con, g_x2_time, g_x2_con_num)

plt.figure(1)

plt.plot([(t - base_time)/1000 for t in g_x_time[0]], g_y_con_num[0], linestyle='--', marker='o', label='Books in chain1')
plt.plot([(t - base_time)/1000 for t in g_x_time[1]], g_y_con_num[1], linestyle='--', marker='>', label='Reviews in chain1')
plt.plot([(t - base_time)/1000 for t in g_x_time[2]], g_y_con_num[2], linestyle='--', marker='*', label='Score in chain1')

plt.plot([(t - base_time)/1000 for t in g_x2_time[0]], g_x2_con_num[0], linestyle=':', marker='o', label='Books in chain2')
# plt.plot([(t - base_time)/1000 for t in g_x2_time[1]], g_x2_con_num[1], linestyle=':', marker='>', label='Chain2 Reviews')
plt.plot([(t - base_time)/1000 for t in g_x2_time[2]], g_x2_con_num[2], linestyle=':', marker='*', label='Score in chain2')

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
plt.ylabel("Container Number", font1)

plt.tick_params(labelsize=14)
plt.xticks(range(0, 500, 100))
plt.yticks(range(0, 11, 2))
plt.legend(loc='upper center', ncol=2, prop=font2)
plt.tight_layout()
plt.show()
plt.savefig("../fig/fig_8_allchain_container")

