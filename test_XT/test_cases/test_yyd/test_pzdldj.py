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

@allure.feature("运营端凭证代理登记（转让成功）")
class test_pzdldj():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_XT', method.__name__)



    @allure.story("转让成功")
    def test_pzdldj(self,get_driver):
        #用户登录
        get_driver.start_houtai(1,'运营')
        # 点击融资管理
        get_driver.get_element('homepage', 'caiwuguanli_tab').click()
        # 点击凭证审核（代理登记）
        get_driver.get_element('pzdldj', 'pzdldj').click()
        #获取凭证编号
        vouchernum=get_driver.get_paras('vouchernum', 1)
        #输入凭证编号
        get_driver.get_element('pzdldj', 'crpayid').send_keys(vouchernum)
        # 点击查询按钮
        get_driver.get_element('pzdldj', 'searchButton').click()
        sleep(2)
        # 点击转让成功按钮
        get_driver.get_element('pzdldj', 'zrcgbtn').click()
        # 点击转让成功确认弹窗的确定按钮
        get_driver.get_element('pzdldj', 'qdbtn').click()
        sleep(2)
        with allure.step("验证该凭证已转让成功"):
            result = get_driver.get_element('pzdldj', 'cxresult')
            assert result is not None
        #打开模拟账户锁定地址
        sleep(3)
        get_driver.get_pzzhsdurl()
        #输入凭证编号
        get_driver.get_element('pzdldj', 'crpid').send_keys(vouchernum)
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





if __name__ == "__main__":
    pytest.main()