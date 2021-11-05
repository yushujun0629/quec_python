#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Time : 2021/10/26 13:46
    Author : Scott Yu
    Email : scott.yu@quectel.com
    File : quec_led.py
"""

'''
EC600UCN平台引脚对应关系如下（引脚号为模块外部引脚编号）
GPIO1 – 引脚号61
GPIO2 – 引脚号58
GPIO3 – 引脚号34
GPIO4 – 引脚号60
GPIO5 – 引脚号69
GPIO6 – 引脚号70
GPIO7 – 引脚号123
GPIO8 – 引脚号118
GPIO9 – 引脚号9
GPIO10 – 引脚号1
GPIO11 – 引脚号4
GPIO12 – 引脚号3
GPIO13 – 引脚号2
GPIO14 – 引脚号54
GPIO15 – 引脚号57
GPIO16 – 引脚号56
'''

from machine import Pin
import utime

# 根据开发板原理图，开发板的一个LED灯连接到了Pin54，通过控制Pin54引脚，实现点灯效果


def led_on():
    LED = Pin(Pin.GPIO14, Pin.OUT, Pin.PULL_DISABLE, 0)
    LED.write(1)


def led_off():
    LED = Pin(Pin.GPIO14, Pin.OUT, Pin.PULL_DISABLE, 0)
    LED.write(0)


if __name__ == '__main__':
    for i in range(10):
        led_on()
        utime.sleep(1)
        led_off()
        utime.sleep(1)

