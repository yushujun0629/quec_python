#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Time : 2021/11/4 15:27
    Author : Scott Yu
    Email : scott.yu@quectel.com
    File : quec_uart.py
"""


from machine import UART
import log, utime


log.basicConfig(level=log.INFO)     # 配置日志输出级别
topic_log = log.getLogger('UART')   # 获取日志主题


'''
UART类功能：串口收发类
用法：uart = UART(UART.UARTn, buadrate, databits, parity, stopbits, flowctl)
返回值：获取一个UART对象，该对象有，any(),read(),write(),close()等方法
参数：
UARTn	    int	    UARTn作用如下：UART0 - DEBUG PORT UART1 – BT PORT UART2 – MAIN PORT UART3 – USB CDC PORT
buadrate	int	    波特率，常用波特率都支持，如4800、9600、19200、38400、57600、115200、230400等
databits	int	    数据位（5~8），展锐平台当前仅支持8位
parity	    int	    奇偶校验（0 – NONE，1 – EVEN，2 - ODD）
stopbits	int	    停止位（1~2）
flowctl	    int	    硬件控制流（0 – FC_NONE， 1 – FC_HW）
'''


state = 10
def write_uart(data):
    # 对于EC600U模块，UART1（TX：pin124，RX：pin123），UART2（TX：pin32，RX：pin31）
    # 此实验基于UART1 来测试。
    # 通过EVB原理图可以知道，pin123，pin124直接连接到开发板的J6连接器，对应关系是：pin123 <==>J6(12脚), pin124 <==>J6(13脚)
    uart = UART(UART.UART1, 115200, 8, 0, 1, 0)
    topic_log.debug("UART is ready")
    uart.write("UART is ready\n")
    utime.sleep_ms(500)
    uart.write(data)
    uart.close()


def read_uart():
    global state
    uart = UART(UART.UART1, 115200, 8, 0, 1, 0)
    while True:
        utime.sleep_us(10)
        data_length = uart.any()
        if data_length:
            data = uart.read(data_length)
            # data_transfer = data.decode(encoding="utf-8")
            # print(data.decode())
            # print(type(data))
            # decode()函数不能带encoding关键字。带了会报错，这个是EC600U解释器不支持
            topic_log.info("Received Message: %s", data.decode())
            state -= 1
            if state == 0:
                uart.close()
                break
        else:
            continue


if __name__ == '__main__':
    for i in range(5):
        write_uart('hello, scott\n')
    utime.sleep(1)
    read_uart()






