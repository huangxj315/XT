# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_register.py

"""
import io
import re
from copy import copy
from xlutils.copy import copy
import random
from selenium import webdriver
from time import sleep
import datetime
import requests
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from pytesseract import image_to_string
import pytest
import allure
from base import base
import xlrd
import os
from openpyxl import load_workbook



@allure.feature("山西电费类录入凭证")
class test_sxdflr():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_XT', method.__name__)

    def test_sxdflr(self, get_driver):
        #打开模拟推山西电费类凭证数据地址
        get_driver.get_lrsxdfurl()
        amount = random.randint(1000000, 999990000)
        skf='北京鲜花自由文化传播有限公司'
        sckswno='91110105MA01YTT4X7'
        #输入凭证编号
        billno = get_driver.get_bianhao()
        billid=get_driver.get_element('sxdflr', 'billid')
        billid.clear()
        billid.send_keys(billno)
        #输入凭证日期
        sgndt = get_driver.get_currentdate()
        sgndate=get_driver.get_element('sxdflr', 'sgndt')
        sgndate.clear()
        sgndate.send_keys(sgndt)
        #输入凭证到期日
        enddate=get_driver.get_element('sxdflr', 'enddt')
        enddate.clear()
        enddate.send_keys('20240630')
        #输入凭证金额
        vouamt=get_driver.get_element('sxdflr', 'vouamt')
        vouamt.clear()
        vouamt.send_keys(amount)
        #输入应付款金额
        payamt=get_driver.get_element('sxdflr', 'payamt')
        payamt.clear()
        payamt.send_keys(amount)
        #输入收款方名称
        rcunm=get_driver.get_element('sxdflr', 'rcunm')
        rcunm.clear()
        rcunm.send_keys(skf)
        #输入收款方税务号
        rtaxno=get_driver.get_element('sxdflr', 'rtaxno')
        rtaxno.clear()
        rtaxno.send_keys(sckswno)
        #输入凭证摘要
        mo=get_driver.get_currentdate()
        memo=get_driver.get_element('sxdflr', 'memo')
        memo.clear()
        memo.send_keys(mo +'脚本自动录入的山西电费类凭证')
        #输入合同编号
        con=get_driver.get_randomtime()
        conno=get_driver.get_element('sxdflr', 'conno')
        conno.clear()
        conno.send_keys(con)
        #输入合同名称
        connm=get_driver.get_element('sxdflr', 'connm')
        connm.clear()
        connm.send_keys(con +'脚本自动生成的合同')
        #输入应付款金额
        conamt=get_driver.get_element('sxdflr', 'conamt')
        conamt.clear()
        conamt.send_keys(amount)
        #输入合同签订日期
        conqdate=get_driver.get_currentdate()
        conqddt=get_driver.get_element('sxdflr', 'conqddt')
        conqddt.clear()
        conqddt.send_keys(conqdate)
        with allure.step("将凭证金额存到参数表中"):
            get_driver.parameter('test_XT', 'case', 'voucheramount', amount, 1)
        # 点击提交
        get_driver.get_element('sxdflr', 'subBtn').click()
        sleep(60)







if __name__ == "__main__":
        pytest.main()
