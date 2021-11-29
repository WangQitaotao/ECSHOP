# -*- encoding: utf-8 -*-
"""
@时间:   2021/11/27 17:34
@作者:   王齐涛
@文件:   123.py 
"""
import os

import pytest

@pytest.mark.skip("练习")
@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):
    out = yield
    report = out.get_result()
    print(out)
    print(report)
    print(report.when)
    print(report.nodeid)
    print(report.outcome)





