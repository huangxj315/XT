# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰

"""
import pytest
from time import sleep
import allure
from base import base
from selenium.webdriver.support.ui import Select
import os



@allure.feature("供应商-融资管理-我的发票")
class test_wdfp():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_XT', method.__name__)

    @allure.feature("供应商-我的发票有查询、申请发票、查看发票操作")
    def test_wdfp(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击我的发票
        get_driver.get_element('rongziguanli-wdfp', 'wdfp').click()
        # 选择未申请状态
        get_driver.get_element('rongziguanli-wdfp', 'wsq').click()
        # 点击申请发票
        get_driver.get_element('rongziguanli-wdfp', 'drawinv').click()
        #输入地址
        get_driver.get_element('rongziguanli-wdfp','payaddr').send_keys('收货地址中兴南路309号河南商会大厦26层')
        #输入电话
        phone=get_driver.generate_phone_number()
        get_driver.get_element('rongziguanli-wdfp','payaddr').send_keys(phone)
        # 点击选择开户行
        get_driver.get_element('rongziguanli-wdfp', 'khh').click()
        # 选择某个开户行
        get_driver.get_element('rongziguanli-wdfp', 'choosekhh').click()
        #输入账号
        accno=get_driver.get_bianhao()
        get_driver.get_element('rongziguanli-wdfp','payaddr').send_keys(accno)
        #输入备注
        get_driver.get_element('rongziguanli-wdfp','memo').send_keys('脚本自动申请的发票')
        #输入收件人姓名
        accno=get_driver.get_bianhao()
        get_driver.get_element('rongziguanli-wdfp','payaddr').send_keys(accno)
        #输入收件人手机号
        get_driver.get_element('rongziguanli-wdfp','payaddr').send_keys(phone)
        #点击省
        qygm=Select(get_driver.get_element('rongziguanli-wdfp', 'provinceSelect'))
        qygm.select_by_visible_text("河南省")
        #点击市
        qygm=Select(get_driver.get_element('rongziguanli-wdfp', 'citySelect'))
        qygm.select_by_visible_text("郑州市")
        #点击县
        qygm=Select(get_driver.get_element('rongziguanli-wdfp', 'regionSelect'))
        qygm.select_by_visible_text("管城回族区")
        #输入详细地址
        get_driver.get_element('rongziguanli-wdfp','streetname').send_keys('中兴南路309号河南商会大厦26层')
        # 选择已申请状态
        get_driver.get_element('rongziguanli-wdfp', 'ysq').click()
        # 点击发票详情
        get_driver.get_element('rongziguanli-wdfp', 'fpxq').click()
        # 点击发票详情
        get_driver.get_element('rongziguanli-wdfp', 'fpxq').click()




if __name__ == "__main__":
        pytest.main()