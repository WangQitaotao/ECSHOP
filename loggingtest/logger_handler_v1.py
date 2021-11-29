# -*- encoding: utf-8 -*-
"""
@时间:   2021/10/4 11:54
@作者:   王齐涛
@文件:   logger_handler_v1.py
"""
import logging
#1.创建日志器
logger = logging.getLogger("Ecshop服务器")


#2、定义处理器，控制台和文本输出两种方式
console_handler = logging.StreamHandler()   #控制台
file_handler = logging.FileHandler("./new.text",mode="a",encoding="utf-8")    #文本

# console_handler.setLevel(level="INFO")
# file_handler.setLevel(level="INFO")

#3、设置不同的输出格式
console_fmt = "%(name)s --->%(levelname)s --->%(asctime)s"
file_fmt = "%(lineno)d --->%(asctime)s --->%(levelname)s"

fmt1 = logging.Formatter(fmt=console_fmt,datefmt="%Y/%m/%d/%X")
fmt2 = logging.Formatter(fmt=file_fmt,datefmt="%Y/%m/%d/%X")

console_handler.setFormatter(fmt1)
file_handler.setFormatter(fmt2)
#4、将日志器添加到控制台处理器
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("这是debug信息")
logger.info("这是info信息")
logger.warning("这是warning信息")
logger.error("这是error信息")
logger.critical("这是cri信息")

class LogTest:
    def __init__(self,name,level="DEBUG"):
        self.log = logging.getLogger(name)
        self.log.setLevel(level)

    def console_handler(self,level = "DEBUG"):
        """
        控制台处理器
        :param level:
        :return:
        """
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(self.get_formatter()[0])
        return console_handler

    def file_handler(self,level = "DEBUG"):
        """
        文件处理器
        :param level:
        :return:
        """
        file_handler = logging.FileHandler("./new.text", mode="a", encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(self.get_formatter()[1])
        return file_handler

    def get_formatter(self):
        """
        格式器，定义输出格式
        :return:
        """
        console_fmt =logging.Formatter(fmt="%(name)s --->%(levelname)s --->%(asctime)s")
        file_fmt = logging.Formatter(fmt="%(lineno)d --->%(asctime)s --->%(levelname)s")
        return console_fmt,file_fmt

    def get_log(self):
        """
        将日志和文件添加到日志器
        :return:
        """
        self.log.addHandler(self.console_handler())
        self.log.addHandler(self.file_handler())
        return self.log



