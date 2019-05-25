#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/3/14 20:14
@desc:
"""
import threading

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_LOCK = threading.Lock()


def get_engine():
    global _LOCK
    with _LOCK:
        global _SQL_ENGINE

        if not _SQL_ENGINE:
            _SQL_ENGINE = create_engine("mysql+pymysql://root:@localhost:3306/cocs", encoding="utf-8", echo=False)
        return _SQL_ENGINE

def get_session():
    global SESSION
    if not SESSION:
        SESSION = sessionmaker(bind=get_engine())()
    return SESSION


class BaseDAO:

    def __init__(self):
        pass

    def list_resources_by_attr(self, model, filter_dict, time):
        try:
            session = get_session()
            resources = session.query(model).filter_by(**filter_dict).all()
            session.commit()
            return resources
        except:
            session.rollback()
            raise