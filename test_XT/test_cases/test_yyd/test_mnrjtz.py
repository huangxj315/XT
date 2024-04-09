# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_pzdldj.py

"""

from time import sleep
import allure
import pytest
import locale

from appium.webdriver import webdriver

from base import base

@allure.feature("运营端模拟入金通知）")
class test_pzdldj():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_XT', method.__name__)



    @allure.story("转让成功")
    def test_pzdldj(self,get_driver):
        #用户登录
        get_driver.start_houtai(1,'运营')
        #获取凭证编号
        vouchernum=get_driver.get_paras('vouchernum', 1)
        #打开模拟账户锁定地址
        get_driver.get_pzzhsdurl()
        #输入凭证编号
        get_driver.get_element('pzdldj', 'crpayid').send_keys(vouchernum)
        # 点击提交锁定按钮
        get_driver.get_element('pzdldj', 'tjsd').click()
        try:
            okbutton = get_driver.get_element('pzdldj', 'ffqd')
            # 判断按钮是否存在
            if okbutton:
                # 如果存在，点击按钮
                okbutton.click()
                # 再次点击提交锁定按钮
                get_driver.get_element('pzdldj', 'tjsd').click()
            else:
                print('元素未找到')
        except Exception as e:
            print("发生异常：", e)

        sleep(20)




if __name__ == "__main__":
    pytest.main()