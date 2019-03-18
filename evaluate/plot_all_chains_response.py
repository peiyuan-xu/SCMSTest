#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/3/14 10:14
@desc:
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams['font.family'] = ['Times New Roman']

base_time = 1552485036959
t_chain1 = [
[1552531557932L, 123L, 224L, 111L, 458L],
[1552531558966L, 114L, 214L, 117L, 445L],
[1552531559998L, 148L, 223L, 110L, 481L],
[1552531561087L, 127L, 215L, 121L, 463L],
[1552531562131L, 128L, 227L, 126L, 481L],
[1552531563162L, 116L, 215L, 116L, 447L],
[1552531564193L, 119L, 220L, 120L, 459L],
[1552531565219L, 116L, 221L, 117L, 454L],
[1552531566249L, 128L, 211L, 121L, 460L],
[1552531567289L, 127L, 234L, 128L, 489L],
[1552531568334L, 135L, 230L, 170L, 535L],
[1552531569380L, 121L, 213L, 110L, 444L],
[1552531570403L, 108L, 211L, 111L, 430L],
[1552531571423L, 115L, 210L, 113L, 438L],
[1552531572449L, 114L, 209L, 110L, 433L],
[1552531573479L, 122L, 216L, 135L, 473L],
[1552531574510L, 115L, 217L, 134L, 466L],
[1552531575540L, 116L, 208L, 112L, 436L],
[1552531576572L, 112L, 210L, 114L, 436L],
[1552531577603L, 128L, 226L, 112L, 466L]
]
t_chain2 = [

]

# service response time
plt.figure(1)
plt.xlabel("Time(s)")
plt.ylabel("Response Time(ms)")
# plt.title('total service  response time')

plt.plot([(t[0] - base_time)/1000 for t in t_chain1], [t[1] for t in t_chain1], c='r', label='Books In Chain1')
plt.plot([(t[0] - base_time)/1000 for t in t_chain1], [t[2] for t in t_chain1], c='y', label='Reviews In Chain1')
plt.plot([(t[0] - base_time)/1000 for t in t_chain1], [t[3] for t in t_chain1], c='b', label='Score In Chain1')

plt.plot([(t[0] - base_time)/1000 for t in t_chain1], [t[1] for t in t_chain2], c='r', marker='o', label='Books In Chain1')
plt.plot([(t[0] - base_time)/1000 for t in t_chain1], [t[2] for t in t_chain2], c='y', marker='o', label='Reviews In Chain1')
plt.plot([(t[0] - base_time)/1000 for t in t_chain1], [t[3] for t in t_chain2], c='b', marker='o', label='Score In Chain1')

plt.legend()
plt.show()

plt.figure(2)
plt.xlabel("Time(s)")
plt.ylabel("Response Time(ms)")
plt.plot([(t[0] - base_time)/1000 for t in t_chain1], [t[4] for t in t_chain1], label='Chain1')
plt.plot([(t[0] - base_time)/1000 for t in t_chain1], [t[4] for t in t_chain2], c='r', marker='o', label='Chain2')

plt.legend()
plt.show()

