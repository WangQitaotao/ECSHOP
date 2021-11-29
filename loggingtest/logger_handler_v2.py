# -*- encoding: utf-8 -*-
"""
@时间:   2021/11/7 19:39
@作者:   王齐涛
@文件:   logger_handler_v2.py
"""
import logging
from common.all_paths import log_path
from common.read_yaml import ReadYaml

#os.chdir(os.path.dirname(os.path.abspath(__file__)))     os.getcwd()+r"\\log_data"

log_info = ReadYaml().read_yaml("./config/log_data")["log"]

def get_logger(filepath=log_path,
               filename=log_info["name"],
               fmtt=log_info["fmt"],
               fmtt2=log_info["fmt2"],
               datefmt=log_info["datefmt"],
               logger_level=log_info["logger_level"],
               console_level=log_info["console_level"],
               file_level=log_info["file_level"]):

    logger = logging.getLogger(filename)  #初始化，创建日志器
    if not logger.handlers:
        logger.setLevel(logger_level)   #设置日志的等级
        console_handler = logging.StreamHandler()   #创建处理器
        console_handler.setLevel(console_level)     #设置处理器日志等级
        logger.addHandler(console_handler)          #处理器添加到日志器中
        fmt = logging.Formatter(fmt=fmtt,datefmt=datefmt)       #设置控制台输出格式
        fmt2 = logging.Formatter(fmt=fmtt2, datefmt=datefmt)    #设置日志文件的格式
        console_handler.setFormatter(fmt)   #添加到处理器
        # logging.basicConfig(filename="111111")

        if filepath:    #日志存放的文件
            file_handler = logging.FileHandler(filepath, mode="a", encoding="utf-8")   #文件控制台处理器
            file_handler.setLevel(file_level)    #设置处理器日志等级
            file_handler.setFormatter(fmt2)  #设置日志格式
            logger.addHandler(file_handler)     #处理器添加到日志器中

    return logger


if __name__ == '__main__':
    get_logger().debug("111111")


