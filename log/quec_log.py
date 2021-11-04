#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Time : 2021/11/2 19:43
    Author : Scott Yu
    Email : scott.yu@quectel.com
    File : quec_log.py
"""

'''
说明：Quectel的log模块是系统日志记录工具，主要用于代码调试，根据官方文档，有不同的log级别，根据log级别的不同，输出不同的log信息。
以下是不同级别的log。
+++++++++++++++++++++++++++++++++++++++++++++++++++++
*  参数	         参数类型	         说明           *
*  CRITICAL        常量	      日志记录级别的数值 50  * 
*  ERROR		   常量        日志记录级别的数值 40  *
*  WARNING		   常量        日志记录级别的数值 30  *
*  INFO		       常量        日志记录级别的数值 20  *
*  DEBUG		   常量        日志记录级别的数值 10  *
*  NOTSET		   常量        日志记录级别的数值 0   *
+++++++++++++++++++++++++++++++++++++++++++++++++++++
系统只会输出 level 数值大于或等于该 level 的日志结果,
举例来说：如果配置log级别是 INFO，则代码中所有DEBUG和NOTSET的Log将不会被输出。
'''


import log

# basicConfig(level)
# 设置日志输出级别, 设置日志输出级别, 默认为log.INFO，系统只会输出 level 数值大于或等于该 level 的的日志结果。
# 由于配置的是NOTSET级别的log，所以，以下所有log将会输出。如果配置默认的INFO级别的log，debug log将不会输出。
log.basicConfig(level=log.NOTSET)   # level 可以省略

'''
原型：log.getLogger(name)
功能：获取logger对象，如果不指定name则返回root对象，多次使用相同的name调用getLogger方法返回同一个logger对象。
参数：name，日志主题
返回值：主题是name的Log对象
'''
log_subject = log.getLogger('scott Yu')

'''
原型：obj.debug(tag)
功能：输出debug级别的日志。
参数：tag，字符串类型
返回值：无
'''
log_subject.debug('this is debug level log ==> %s', 'from "debug" method!')

'''
原型：obj.info(tag)
功能：输出info级别的日志。
参数：tag，字符串类型
返回值：无
'''
log_subject.info('this is info level log ==> %s', 'from "info" method!')

'''
原型：obj.warning(tag)
功能：输出warning级别的日志。
参数：tag，字符串类型
返回值：无
'''
log_subject.warning('this is warning level log ==> %s', 'from "warning" method!')

'''
原型：obj.error(tag)
功能：输出error级别的日志。
参数：tag，字符串类型
返回值：无
'''
log_subject.error('this is error level log ==> %s', 'from "error" method!')

'''
原型：obj.critical(tag)
功能：输出critical级别的日志。
参数：tag，字符串类型
返回值：无
'''
log_subject.critical('this is critical level log ==> %s', 'from "critical" method!')
