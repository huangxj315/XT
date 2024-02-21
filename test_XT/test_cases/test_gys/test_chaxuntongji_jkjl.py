# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_chaxuntongji_edsqjl.py

"""
import pytest
from time import sleep
import allure
from base import base
import os



@allure.feature("供应商-查询统计-借款记录")
class test_jkjl():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    @allure.feature("供应商-借款记录有查询、详情、下载操作")
    def test_jkjl(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击查询统计tab
        get_driver.get_element('homepage', 'chaxuntongji_tab').click()
        # 点击借款记录
        get_driver.get_element('jiekuanjilu', 'jkjl').click()
        # 定位div元素
        div_element = get_driver.get_element('jiekuanjilu', 'div_locator')
        # 定位table元素
        table_element = div_element.find_element_by_xpath("//table")
        # 定位tbody元素
        tbody_element = div_element.find_element_by_xpath("//tbody")
        # 定位第一行的元素
        first_row = tbody_element.find_elements_by_xpath(".//tr")[0]
        # 定位第一行第二列的元素
        sec_cell = first_row.find_elements_by_xpath(".//td")[1]
        # 点击第一行第二列的元素
        sec_cell.click()
        # 点击凭证信息
        get_driver.get_next_handle()
        get_driver.get_element('jiekuanjilu', 'pzxx').click()
        sleep(3)
        # 点击操作记录
        get_driver.get_element('jiekuanjilu', 'czjl').click()
        sleep(3)
        # 点击费用信息
        get_driver.get_element('jiekuanjilu', 'fyxx').click()
        sleep(3)
        # 点击关闭按钮
        get_driver.get_element('jiekuanjilu', 'closebutton').click()
        # 点击查询按钮
        get_driver.get_pre_handle()
        get_driver.get_element('jiekuanjilu', 'searchButton').click()
        # 点击下载查询结果按钮
        get_driver.download_query_results('jiekuanjilu','exportButton')


if __name__ == "__main__":
        pytest.main()