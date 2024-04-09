# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_chaxuntongji_yszkqq.py

"""
import pytest
from time import sleep
import allure
from base import base
import os



@allure.feature("供应商-查询统计-应收账款确权")
class test_yszkqq():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_XT', method.__name__)

    @allure.feature("供应商-应收账款确权有可用、流转中、已融资、已支付、已到期tab页面")
    def test_keyong(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击查询统计tab
        get_driver.get_element('homepage', 'chaxuntongji_tab').click()
        # 点击应收账款确权
        get_driver.get_element('chaxuntongji-yszkqq', 'yszkqq').click()
        sleep(2)
        # 点击详情按钮
        get_driver.get_element('chaxuntongji-yszkqq', 'xqbutton').click()
        sleep(2)
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('chaxuntongji-yszkqq', 'closebutton').click()
        # 点击查看流转路径按钮
        get_driver.get_pre_handle()
        get_driver.get_element('chaxuntongji-yszkqq', 'lzljbutton').click()
        # 点击查询按钮
        get_driver.get_pre_handle()
        get_driver.get_element('chaxuntongji-yszkqq', 'searchButton').click()
        # 点击下载查询结果按钮
        get_driver.download_query_results('chaxuntongji-yszkqq','exportButton')
    def test_liuzhuanzhong(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击查询统计tab
        get_driver.get_element('homepage', 'chaxuntongji_tab').click()
        # 点击应收账款确权
        get_driver.get_element('chaxuntongji-yszkqq', 'yszkqq').click()
        sleep(2)
        # 点击流转中
        get_driver.get_element('chaxuntongji-yszkqq', 'liuzhuanzhong').click()
        sleep(2)
        # 点击详情按钮
        get_driver.get_element('chaxuntongji-yszkqq', 'xqbutton1').click()
        sleep(2)
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('chaxuntongji-yszkqq', 'closebutton').click()
        # 点击查看流转路径按钮
        get_driver.get_pre_handle()
        get_driver.get_element('chaxuntongji-yszkqq', 'lzljbutton1').click()
        # 点击查询按钮
        get_driver.get_pre_handle()
        get_driver.get_element('chaxuntongji-yszkqq', 'searchButton').click()
        # 点击下载查询结果按钮
        get_driver.download_query_results('chaxuntongji-yszkqq','exportButton')
    def test_yirongzi(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击查询统计tab
        get_driver.get_element('homepage', 'chaxuntongji_tab').click()
        # 点击应收账款确权
        get_driver.get_element('chaxuntongji-yszkqq', 'yszkqq').click()
        sleep(2)
        # 点击已融资
        get_driver.get_element('chaxuntongji-yszkqq', 'yirongzi').click()
        sleep(2)
        # 点击详情按钮
        get_driver.get_element('chaxuntongji-yszkqq', 'xqbutton1').click()
        sleep(2)
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('chaxuntongji-yszkqq', 'closebutton').click()
        # 点击查看流转路径按钮
        get_driver.get_pre_handle()
        get_driver.get_element('chaxuntongji-yszkqq', 'lzljbutton1').click()
        # 点击查询按钮
        get_driver.get_pre_handle()
        get_driver.get_element('chaxuntongji-yszkqq', 'searchButton').click()
        # 点击下载查询结果按钮
        get_driver.download_query_results('chaxuntongji-yszkqq','exportButton')
    def test_yizhifu(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击查询统计tab
        get_driver.get_element('homepage', 'chaxuntongji_tab').click()
        # 点击应收账款确权
        get_driver.get_element('chaxuntongji-yszkqq', 'yszkqq').click()
        sleep(2)
        # 点击已转让
        get_driver.get_element('chaxuntongji-yszkqq', 'yizhuanrang').click()
        sleep(2)
    def test_yidaoqi(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击查询统计tab
        get_driver.get_element('homepage', 'chaxuntongji_tab').click()
        # 点击应收账款确权
        get_driver.get_element('chaxuntongji-yszkqq', 'yszkqq').click()
        sleep(2)
        # 点击已到期
        get_driver.get_element('chaxuntongji-yszkqq', 'yidaoqi').click()
        sleep(2)
        # 点击详情按钮
        get_driver.get_element('chaxuntongji-yszkqq', 'xqbutton2').click()
        sleep(2)
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('chaxuntongji-yszkqq', 'closebutton').click()
        # 点击查看流转路径按钮
        get_driver.get_pre_handle()
        get_driver.get_element('chaxuntongji-yszkqq', 'lzljbutton2').click()
        # 点击查询按钮
        get_driver.get_pre_handle()
        get_driver.get_element('chaxuntongji-yszkqq', 'searchButton').click()
        # 点击下载查询结果按钮
        get_driver.download_query_results('chaxuntongji-yszkqq','exportButton')


if __name__ == "__main__":
        pytest.main()