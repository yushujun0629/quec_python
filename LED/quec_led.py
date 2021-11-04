#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Time : 2021/10/26 13:46
    Author : Scott Yu
    Email : scott.yu@quectel.com
    File : quec_led.py
"""

from machine import Pin
import utime

LED = Pin(Pin.GPIO14, Pin.OUT, Pin.PULL_DISABLE, 0)

while True:
    LED.write(1)
    utime.sleep(1)
    LED.write(0)
    utime.sleep(1)

