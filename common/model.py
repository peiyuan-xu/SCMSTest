#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/3/14 20:18
@desc:
"""
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.ext import declarative
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text

ModelBase = declarative.declarative_base()

# QueueMessage Model
# refer http://docs.sqlalchemy.org/en/latest/orm/tutorial.html


class DictBase(object):
    attributes = []

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        d = {}
        for attr in self.__class__.attributes:
            d[attr] = getattr(self, attr)
        return d

    def __getitem__(self, key):
        return getattr(self, key)


class QueueMessage(ModelBase, DictBase):
    __tablename__ = 'queuemessage'
    attributes = ['id', 'chain_id', 'service_id', 'message_number',
                  'timestamp']

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    chain_id = Column('chain_id', String(length=36), ForeignKey('chain.id'))
    service_id = Column('service_id', String(length=36), ForeignKey('service.id'))
    message_number = Column('message_number', Integer)
    timestamp = Column('timestamp',   TIMESTAMP,
                       server_default=text('CURRENT_TIMESTAMP'), index=True)