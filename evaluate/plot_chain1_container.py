#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/3/14 12:08
@desc:
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams['font.family'] = ['Times New Roman']


base_time = 1552652444145L

chain1_con = [

{'start_t': 1552652444145L, 'tag': 'add', 'service': u'books', 'chain': u'chain1', 'end_t': 1552652454230L},
{'start_t': 1552652456701L, 'tag': 'add', 'service': u'books', 'chain': u'chain1', 'end_t': 1552652466368L},
{'start_t': 1552652469409L, 'tag': 'add', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552652479559L},
{'start_t': 1552652479768L, 'tag': 'add', 'service': u'books', 'chain': u'chain1', 'end_t': 1552652490431L},
{'start_t': 1552652492761L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652502037L},
{'start_t': 1552652502206L, 'tag': 'add', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552652511900L},
{'start_t': 1552652514216L, 'tag': 'add', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552652524445L},
{'start_t': 1552652526701L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652537526L},
{'start_t': 1552652537642L, 'tag': 'add', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552652547890L},
{'start_t': 1552652550204L, 'tag': 'add', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552652561233L},
{'start_t': 1552652563524L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652573272L},
{'start_t': 1552652575561L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652585946L},
{'start_t': 1552652616956L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652626908L},
{'start_t': 1552652629260L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652639001L},
{'start_t': 1552652693339L, 'tag': 'delete', 'service': u'books', 'chain': u'chain1', 'end_t': 1552652696159L},
{'start_t': 1552652698489L, 'tag': 'delete', 'service': u'books', 'chain': u'chain1', 'end_t': 1552652701266L},
{'start_t': 1552652703486L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652707255L},
{'start_t': 1552652707382L, 'tag': 'delete', 'service': u'books', 'chain': u'chain1', 'end_t': 1552652711891L},
{'start_t': 1552652714196L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652721879L},
{'start_t': 1552652821696L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652824945L},
{'start_t': 1552652827255L, 'tag': 'add', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652838946L},
{'start_t': 1552652873743L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652876366L},
{'start_t': 1552652876477L, 'tag': 'delete', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552652879668L},
{'start_t': 1552652881991L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652884676L},
{'start_t': 1552652884788L, 'tag': 'delete', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552652887701L},
{'start_t': 1552652890027L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652893295L},
{'start_t': 1552652893410L, 'tag': 'delete', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552652895982L},
{'start_t': 1552652898266L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652901440L},
{'start_t': 1552652901542L, 'tag': 'delete', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552652904362L},
{'start_t': 1552652906626L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652909013L},
{'start_t': 1552652909108L, 'tag': 'delete', 'service': u'reviews', 'chain': u'chain1', 'end_t': 1552652911974L},
{'start_t': 1552652914241L, 'tag': 'delete', 'service': u'score', 'chain': u'chain1', 'end_t': 1552652916625L}

]

x_time = [[base_time], [base_time], [base_time]]
y_con_num = [[0], [0], [0]]
for d in chain1_con:
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


plt.figure(1)
plt.xlabel("Time(s)")
plt.ylabel("Container Number")
# plt.title('total service  response time')

print([(t - base_time)/1000 for t in x_time[0]])
print(y_con_num[0])
plt.bar([(t - base_time)/1000 for t in x_time[0]], y_con_num[0], width=4, label='Books')
plt.bar([(t - base_time)/1000 for t in x_time[1]], y_con_num[1], width=4, label='Reviews')
plt.bar([(t - base_time)/1000 for t in x_time[2]], y_con_num[2], width=4, label='Score')

# plt.plot([(t - base_time)/1000 for t in x_time[0]], y_con_num[0], label='Books')
# plt.plot([(t - base_time)/1000 for t in x_time[1]], y_con_num[1], label='Reviews')
# plt.plot([(t - base_time)/1000 for t in x_time[2]], y_con_num[2], label='Score')

plt.yticks([0,1,2,3,4,5,6])
# plt.legend(bbox_to_anchor=(1.02, 0), loc=3, borderaxespad=0)
# plt.subplots_adjust(right=0.8)

plt.legend(loc='upper left')
plt.show()
