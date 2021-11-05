#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Time : 2021/11/5 16:05
    Author : Scott Yu
    Email : scott.yu@quectel.com
    File : quec_adc.py
"""


from misc import ADC
from machine import Pin
import utime, log


def led_on():
    led = Pin(Pin.GPIO14, Pin.OUT, Pin.PULL_DISABLE, 0)
    led.write(1)


def led_off():
    led = Pin(Pin.GPIO14, Pin.OUT, Pin.PULL_DISABLE, 0)
    led.write(0)


log.basicConfig(level=log.INFO)
topic_log = log.getLogger("ADC")


def check_light_level():
    # 创建一个ADC对象
    adc = ADC()
    if adc.open() == 0:
        while True:
            utime.sleep_ms(500)
            # 方法obj.read(ADCn),读取成功，返回实际的ADC值，读取失败，返回-1。对于EC600U模块，ADC引脚对应如下：
            # EC600U平台对应引脚如下 ADC0 – 引脚号19 ADC1 – 引脚号20 ADC2 – 引脚号113 ADC3 – 引脚号114
            # 根据开发板原理图可知，ADC0连接到了一个光敏传感器
            data = adc.read(ADC.ADC0)
            # 如果采集的数据大于300mV，表明灯光太暗，需要开灯(此处模拟一个灯光检测器）
            # 光敏电阻，光线越暗，阻值越大，根据原理图，分的电压就越大
            if data != -1 and data >= 300:
                led_on()
            elif data != -1:
                led_off()
            else:
                topic_log.error("ADC读取数据错误")

    else:
        topic_log.error("ADC初始化失败!")


if __name__ == '__main__':
    check_light_level()
