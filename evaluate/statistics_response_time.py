#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/3/13 11:32
@desc:
"""
import ast


import pika
import pika.exceptions as p_ex


def receive_message(queue, callback):
    RABBITMQ_VHOST = "scms"
    RABBITMQ_USER = "scms"
    RABBITMQ_PWD = "scms"
    server_ip = '192.168.1.220'

    try:
        credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PWD)
        PIKA_CONN = pika.BlockingConnection(pika.ConnectionParameters(
            host=server_ip, virtual_host=RABBITMQ_VHOST, credentials=credentials))
        channel = PIKA_CONN.channel()
    except p_ex.AMQPConnectionError as e:
        print(e.args)

    channel.queue_declare(queue=queue)
    channel.basic_consume(callback,
                          queue=queue)

    print(' [*] Waiting for messages. From the queue: ' + queue)
    channel.start_consuming()


chain1_resp_list = []
chain1_x = []


def statistics(ch, method, properties, body):
    global chain1_x
    global chain1_resp_dict

    # RABBITMQ_CLIENT = Client('192.168.1.220:15672', 'scms', 'scms')
    #
    # chain1_gw_messages = RABBITMQ_CLIENT.get_messages(vhost=RABBITMQ_VHOST, qname=Chain1_QUEUE_NAME)

    m_dict = ast.literal_eval(body)
    gw_t = m_dict.get('gw_time')
    books_t = m_dict.get('books_time')
    review_t = m_dict.get('review_time')
    score_t = m_dict.get('score_time')
    print(str([gw_t, books_t - gw_t, review_t - books_t, score_t - review_t, score_t - gw_t]) + ',')
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # chain1_x.append(gw_t)
    # chain1_resp_dict[gw_t] = [books_t - gw_t, review_t - books_t, score_t - review_t, score_t - gw_t]


receive_message('chain1_gw', statistics)




