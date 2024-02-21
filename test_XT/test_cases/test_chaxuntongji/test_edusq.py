# -*- coding: utf-8 -*-
"""
@Time ： 2023/4/27 16:34
@Auth ： 黄香杰
@File ：test_edusq.py

"""
import pytest
import allure
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base import base



@allure.feature("查询统计-默认进入额度申请记录列表")
class test_chaxuntongji_edsq():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)


    @allure.story("进入查询统计tab")
    def test_chaxuntongji_edsq_001(self,get_driver):
        #用户登录
        get_driver.start_houtai(1)
        #点击查询统计
        get_driver.get_element('querystatic', 'shouye_tab').click()
        time.sleep(3)
        #输入关键字
        get_driver.get_element('querystatic', 'key_word').send_keys('浙商')
        #点击查询
        get_driver.get_element('querystatic', 'query_button').click()




if __name__ == "__main__":
    pytest.main()