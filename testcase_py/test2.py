# -*- encoding: utf-8 -*-
"""
@时间:   2021/11/28 10:50
@作者:   王齐涛
@文件:   test2.py 
"""
import os

import allure


def test02(test):
    allure.dynamic.title(test)
    print("环境变量名称",os.environ["token"])
    print("测试用例2",test)