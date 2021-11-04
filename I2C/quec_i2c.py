#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Time : 2021/10/26 14:57
    Author : Scott Yu
    Email : scott.yu@quectel.com
    File : quec_i2c.py
"""


import log
import utime as time
from machine import I2C


class AHT10:
    # i2c_device = None
    # i2c_log = None

    AHT10_INIT_CMD = 0xE1             # I2C设备（奥松的AHT10）初始化命令
    AHT10_MEASURE_CMD = 0xAC          # 触发测量的命令
    AHT10_RESET_CMD = 0xBA            # 复位命令
    AHT10_ADDR_DEVICE = 0x38          # AHT10 设备地址
    # AHT10_STATUS_CMD = 0x71           # 获取设备状态字节命令

    def __init__(self, addr=AHT10_ADDR_DEVICE, log_subject='AHT10'):
        # 获取一个日志主题是 "AHT10"的对象
        self.i2c_logger = log.getLogger(log_subject)
        # EC600U含有2路I2C，根据EVB硬件原理图，其中一路I2C1（PIN56 <==> SDA，PIN57 <==> SCL）通过电平转换芯片连接到了AHT10，
        # 另一路I2C2设备（PIN11，PIN12）连到了camera
        self.i2c_dev = I2C(I2C.I2C1, I2C.STANDARD_MODE)
        self.i2c_addr = addr

    def init_ath10(self):
        self.__write_ath10([AHT10.AHT10_INIT_CMD, 0x08, 0x00])
        time.sleep_ms(40)  # at last 300ms
        # r_data = self.write_ath10(AHT10.AHT10_STATUS_CMD)

    def __write_ath10(self, data):
        success_flag = self.i2c_dev.write(self.i2c_addr, bytearray(0x00), 0, bytearray(data), len(data))
        if success_flag == 0:
            self.i2c_logger.info('I2C设备：%s', '写入成功')
        else:
            self.i2c_logger.error('I2C设备：%s', '写入失败')

    def __read_ath10(self, length):
        r_data = [0x00 for i in range(length)]    # 列表序里化
        r_data = bytearray(r_data)
        success_flag = self.i2c_dev.read(self.i2c_addr, bytearray(0x00), 0, r_data, length, 0)
        if success_flag == 0:
            self.i2c_logger.info('I2C设备：%s', '读取成功')
            return list(r_data)
        else:
            self.i2c_logger.error('I2C设备：%s', '读取失败')

    def reset_ath10(self):
        self.__write_ath10([AHT10.AHT10_RESET_CMD])
        time.sleep_ms(20)

    def trigger_data_measure(self):
        # 根据手册，AHT10触发测量命令是0xAC，次命令含有2个字节参数，一个是0x33，另一个是0x00
        self.__write_ath10([AHT10.AHT10_MEASURE_CMD, 0x33, 0x00])
        time.sleep_ms(100)  # 根据手册，至少延迟80ms等待测量完成，此处设置100ms
        # 根据手册，测量完成以后，读取转换后的数据，通过读取Bit[7]的状态位，判读数据是否正常
        r_data = self.__read_ath10(6)
        # 检查bit[7]， 0代表数据正常，1代表设备忙，需要等待设备数据处理完成
        if (r_data[0] >> 7) != 0x0:
            self.i2c_logger.error('I2C设备：%s', '设备忙')
        else:
            self.__signal_transfer(r_data[1:6])

    def __signal_transfer(self, data):
        r_data = data
        # 　根据数据手册的描述来转化湿度
        humidity = (r_data[0] << 12) | (r_data[1] << 4) | ((r_data[2] & 0xF0) >> 4)
        humidity = (humidity / (1 << 20)) * 100.0
        # self.humidity = humidity
        print("当前环境湿度是： {0}%".format(humidity))

        # 　根据数据手册的描述来转化温度
        temperature = ((r_data[2] & 0xf) << 16) | (r_data[3] << 8) | r_data[4]
        temperature = (temperature * 200.0 / (1 << 20)) - 50
        self.temperature = temperature
        print("当前环境温度是： {0}°C".format(temperature))


if __name__ == "__main__":
    from machine import Pin

    def i2c_aht10_test():
        aht10_dev = AHT10()
        aht10_dev.init_ath10()
        # 测试50次
        for i in range(50):
            aht10_dev.trigger_data_measure()
            if aht10_dev.temperature > 29:
                led = Pin(Pin.GPIO14, Pin.OUT, Pin.PULL_DISABLE, 0)
                led.write(1)
            else:
                led = Pin(Pin.GPIO14, Pin.OUT, Pin.PULL_DISABLE, 0)
                led.write(0)
            time.sleep(1)

    i2c_aht10_test()

