#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/3/13 15:47
@desc:
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams['font.family'] = ['Times New Roman']


base_time = 1552485036959L
t_all = [
[1552485036959L, 125L, 216L, 122L, 463L],
[1552485037997L, 109L, 213L, 118L, 440L],
[1552485039024L, 117L, 216L, 119L, 452L],
[1552485040051L, 128L, 225L, 117L, 470L],
[1552485041084L, 120L, 236L, 151L, 507L],
[1552485042113L, 119L, 212L, 120L, 451L],
[1552485043134L, 117L, 212L, 125L, 454L],
[1552485044164L, 111L, 217L, 114L, 442L],
[1552485045185L, 121L, 211L, 122L, 454L],
[1552485046215L, 120L, 218L, 124L, 462L],
[1552485047240L, 132L, 227L, 109L, 468L],
[1552485048264L, 119L, 216L, 126L, 461L],
[1552485049296L, 112L, 215L, 117L, 444L],
[1552485050320L, 114L, 226L, 151L, 491L],
[1552485051349L, 123L, 218L, 127L, 468L],
[1552485052374L, 132L, 227L, 117L, 476L],
[1552485053398L, 117L, 215L, 120L, 452L],
[1552485054418L, 116L, 235L, 114L, 465L],
[1552485055439L, 121L, 214L, 121L, 456L],
[1552485056474L, 132L, 221L, 183L, 536L]

]

# service response time
plt.figure(1)
plt.xlabel("Time(s)")
plt.ylabel("Response Time(ms)")
# plt.title('total service  response time')

#ms
plt.plot([(t[0] - base_time)/1000 for t in t_all], [t[1] for t in t_all], label='Books')
plt.plot([(t[0] - base_time)/1000 for t in t_all], [t[2] for t in t_all], label='Reviews')
plt.plot([(t[0] - base_time)/1000 for t in t_all], [t[3] for t in t_all], label='Score')
plt.plot([(t[0] - base_time)/1000 for t in t_all], [t[4] for t in t_all], label='Chain1')

plt.legend()
plt.show()

def to_percent(temp, position):
    return '%1.0f'%(100*temp) + '%'
# time consumption caused by communication management
plt.figure(2)
plt.xlabel("Time(s)")
plt.ylabel("Consumption")
plt.plot([(t[0] - base_time)/1000 for t in t_all], [float(t[1] - 100)/t[1] for t in t_all], label='Books')
plt.plot([(t[0] - base_time)/1000 for t in t_all], [float(t[2] - 200)/t[2] for t in t_all], label='Reviews')
plt.plot([(t[0] - base_time)/1000 for t in t_all], [float(t[3] - 100)/t[3] for t in t_all], label='Score')
plt.plot([(t[0] - base_time)/1000 for t in t_all], [float(t[4] - 400)/t[4] for t in t_all], label='Chain1')
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.legend()
plt.show()

