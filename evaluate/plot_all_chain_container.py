#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/3/14 21:20
@desc:
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams['font.family'] = ['Times New Roman']


base_time = 1552810331510L
all_con = [

{'start_t': 1552810331510L, 'tag': 'add', 'service': u'books', 'chain': u'chain2', 'end_t': 1552810344200L},
{'start_t': 1552810344639L, 'tag': 'add', 'service': u'books', 'chain': u'chain1', 'end_t': 1552810355263L},
{'start_t': 1552810356478L, 'tag': 'add', 'service': u'books', 'chain': u'chain2', 'end_t': 1552810368816L},
{'start_t': 1552810368965L, 'tag': 'add', 'service': u'score', 'chain': u'chain2', 'end_t': 1552810381462L},
{'start_t': 1552810381674L, 'tag': 'add', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552810393214L},
{'start_t': 1552810393359L, 'tag': 'add', 'service': u'books', 'chain': u'chain1', 'end_t': 1552810405240L},
{'start_t': 1552810406419L, 'tag': 'add', 'service': u'books', 'chain': u'chain2', 'end_t': 1552810418560L},
{'start_t': 1552810418683L, 'tag': 'add', 'service': u'score', 'chain': u'chain2', 'end_t': 1552810429779L},
{'start_t': 1552810429905L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810441475L},
{'start_t': 1552810441605L, 'tag': 'add', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552810445905L},
{'start_t': 1552810447187L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810460267L},
{'start_t': 1552810460391L, 'tag': 'add', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552810472411L},
{'start_t': 1552810473772L, 'tag': 'add', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552810484605L},
{'start_t': 1552810485838L, 'tag': 'delete', 'service': u'books', 'chain': u'chain2', 'end_t': 1552810489534L},
{'start_t': 1552810490822L, 'tag': 'delete', 'service': u'books', 'chain': u'chain2', 'end_t': 1552810494336L},
{'start_t': 1552810495605L, 'tag': 'delete', 'service': u'books', 'chain': u'chain2', 'end_t': 1552810498826L},
{'start_t': 1552810521942L, 'tag': 'add', 'service': u'score', 'chain': u'chain2', 'end_t': 1552810533480L},
{'start_t': 1552810533624L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810545610L},
{'start_t': 1552810549477L, 'tag': 'delete', 'service': u'score', 'chain': u'chain2', 'end_t': 1552810552423L},
{'start_t': 1552810552539L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810565599L},
{'start_t': 1552810566927L, 'tag': 'delete', 'service': u'score', 'chain': u'chain2', 'end_t': 1552810569727L},
{'start_t': 1552810569845L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810582246L},
{'start_t': 1552810583619L, 'tag': 'delete', 'service': u'score', 'chain': u'chain2', 'end_t': 1552810586588L},
{'start_t': 1552810589319L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810600317L},
{'start_t': 1552810673359L, 'tag': 'delete', 'service': u'books', 'chain': u'chain1', 'end_t': 1552810676510L},
{'start_t': 1552810677850L, 'tag': 'delete', 'service': u'books', 'chain': u'chain1', 'end_t': 1552810681296L},
{'start_t': 1552810683997L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810686459L},
{'start_t': 1552810687830L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810699135L},
{'start_t': 1552810708919L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810711697L},
{'start_t': 1552810711810L, 'tag': 'delete', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552810714941L},
{'start_t': 1552810716329L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810719076L},
{'start_t': 1552810719172L, 'tag': 'delete', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552810722433L},
{'start_t': 1552810723800L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810726755L},
{'start_t': 1552810726854L, 'tag': 'delete', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552810729941L},
{'start_t': 1552810731326L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810733890L},
{'start_t': 1552810733984L, 'tag': 'delete', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552810738216L},
{'start_t': 1552810739576L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810742395L},
{'start_t': 1552810743792L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552810746273L}

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
plt.xlabel("Time")
plt.ylabel("Container Number")
# plt.title('total service  response time')


plt.bar([(t - base_time)/1000 for t in g_x_time[0]], g_y_con_num[0], label='Chain1 Books')
# plt.bar([(t - base_time)/1000 for t in g_x_time[1]], g_y_con_num[1], label='Chain1 Reviews')
# plt.bar([(t - base_time)/1000 for t in g_x_time[2]], g_y_con_num[2], label='Chain1 Score')

plt.bar([(t - base_time)/1000 for t in g_x2_time[0]], g_x2_con_num[0], label='Chain2 Books')
# plt.bar([(t - base_time)/1000 for t in g_x2_time[1]], g_x2_con_num[1], label='Chain2 Reviews')
# plt.bar([(t - base_time)/1000 for t in g_x2_time[2]], g_x2_con_num[2], label='Chain2 Score')

plt.yticks([0,1,2,3,4,5,6])
plt.legend()
plt.show()