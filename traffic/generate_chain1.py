#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/3/13 11:28
@desc:
"""

import urllib
import time
import multiprocessing


chain1_url = 'http://192.168.1.154:8081/servicegw/user_buy'
chain2_url = 'http://192.168.1.154:8081/servicegw/seller_statistics'


# qps 10 100 1000 100
def send(url, t_in):
    # t_each = 40
    t_each = 20
    num = 0
    # print("qps: " + str(qps))
    t_auto_start = time.localtime()
    t_gather_start = time.strftime("%Y-%m-%d %H:%M:%S", t_auto_start)
    print("Send request, time : ", t_gather_start)

    t_s = time.time()
    while time.time() < t_s + t_each:
        # temp_t1 = time.time()
        urllib.urlopen(url)
        # print(time.time() - temp_t1)
        num += 1
        temp_t = time.time() - t_in
        time.sleep(0.2)
        # if temp_t < 10:
        #     time.sleep(1)
        # elif temp_t < 20:
        #     time.sleep(0.5)
        # elif temp_t < 30:
        #     # time.sleep(0.2)
        #     time.sleep(0.1)
        # else:
        #     # time.sleep(1)
        #     time.sleep(0.05)
        #     pass

    print("request num: " + str(num))


def main():
    # single process
    # send(chain1_url, 100)

    # multi process
    t = time.time()
    process_num = 4
    process = []
    # for i in range(process_num):
    #     t_in = time.time()
    #     p = multiprocessing.Process(target=send, args=(chain1_url, t_in))
    #     p.daemon = True
    #     p.start()
    #     process.append(p)
    # for p in process:
    #     p.join()
    send(chain1_url, t)
    t_e = time.time()
    print(t_e - t)


if __name__ == "__main__":

    main()

