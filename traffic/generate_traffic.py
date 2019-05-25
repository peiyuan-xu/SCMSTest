#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/5/23 19:27
@desc:
"""


import urllib
import time
import multiprocessing


chain1_url = 'http://192.168.1.153:8081/servicegw/user_buy'
chain2_url = 'http://192.168.1.153:8081/servicegw/seller_statistics'


# qps 10 100 1000 100
def send(url, t_in, t_flag):
    # t_each = 40
    t_each = 40
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
        if temp_t < 10:
            time.sleep(2/t_flag)
        elif temp_t < 20:
            time.sleep(1/t_flag)
        elif temp_t < 30:
            time.sleep(0.5/t_flag)
        else:
            time.sleep(0.2/t_flag)
            pass

    chain_name = "Chain1" if t_flag == 2 else "Chain2"
    print(chain_name + " request num: " + str(num))


def main():
    # single process
    # send(chain1_url, 100)

    # multi process
    t = time.time()
    process_num = 4
    process = []
    for i in range(process_num):
        t_in = time.time()
        p = multiprocessing.Process(target=send, args=(chain1_url, t_in, 2))
        p.daemon = True
        p.start()
        process.append(p)

    for i in range(process_num):
        t_in = time.time()
        p = multiprocessing.Process(target=send, args=(chain2_url, t_in, 1))
        p.daemon = True
        p.start()
        process.append(p)

    for p in process:
        p.join()

    t_e = time.time()
    print("Generate Traffic Time: " + str(t_e - t) + " s")


if __name__ == "__main__":

    main()

