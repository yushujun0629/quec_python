#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Time : 2021/11/27 13:48
    Author : Scott Yu
    Email : scott.yu@quectel.com
    File : watchdog.py
"""


from machine import WDT      # 导入看门狗类
from machine import Timer    # 导入定时器类
import log

log.basicConfig(level=log.NOTSET)   # 设置log级别
log_subject = log.getLogger('WatchDog')
# log_subject.info('this is debug level log ==> %s', 'from "debug" method!')

number = 0


def feed_dog(obj_time):
    """ 定义一个喂狗函数 """
    global number
    if number < 10:
        print("第{}次喂狗".format(number+1))
        wdt.feed()
        number += 1
    else:
        obj_time.stop()
        log_subject.info('喂狗成功，关闭周期性定时器')
        status = wdt.stop()  # 关闭看门狗
        if status == 0:
            log_subject.info('看门狗关闭成功！')


if __name__ == '__main__':
    wdt = WDT(20)   # 启动一个20s的看门狗
    timer1 = Timer(Timer.Timer1)  # 生成第一个定时器对象
    # 每隔15s 周期性的启动喂狗信号
    timer1.start(period=15000, mode=timer1.PERIODIC, callback=feed_dog)




