# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_chaxuntongji_yszk.py

"""
import pytest
from time import sleep
import allure
from base import base
import os



@allure.feature("供应商-查询统计-应收账款")
class test_yszk():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_XT', method.__name__)

    @allure.feature("供应商-应收账款有查询、下载操作")
    def test_yszk(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击查询统计tab
        get_driver.get_element('homepage', 'chaxuntongji_tab').click()
        # 点击借款记录
        get_driver.get_element('chaxuntongji-yszk', 'yszk').click()
        # 点击查询按钮
        get_driver.get_element('chaxuntongji-yszk', 'searchButton').click()
        # 点击下载查询结果按钮
        get_driver.download_query_results('chaxuntongji-yszk','exportButton')


if __name__ == "__main__":
        pytest.main()