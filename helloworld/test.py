#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Time : 2021/10/26 13:46
    Author : Scott Yu
    Email : scott.yu@quectel.com
    File : quec_led.py
"""

import utime
import uos   
while True:
    print(uos.listdir('usr/'))  # list file of current directory
    print(uos.uname())  # print Quectel module system information
    
    print("Hello Scott, This script is running!")
    utime.sleep(1)   # delay 1 second
    