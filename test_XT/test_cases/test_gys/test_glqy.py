# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_smrz.py

"""
import datetime
import random
from time import sleep
import pytest
import allure
from base import base
from selenium.webdriver.support.ui import Select



@allure.feature("供应商-关联企业")
class test_glqy():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_XT', method.__name__)

    def test_glqy(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1,'供应商')
        # 点击账户设置
        get_driver.get_element('glqy', 'zhsz').click()
        # 点击我的信息
        get_driver.get_next_handle()
        get_driver.get_element('glqy', 'wdxx').click()
        # 点击关联企业
        get_driver.get_element('glqy', 'glqy').click()
        #生成企业名称
        companyname=get_driver.generate_company_name()
        #输入企业名称
        get_driver.get_element('glqy','firmname').send_keys(companyname)
        # get_driver.get_element('smrz', 'firmname').send_keys('山西三建集团有限公司')
        # 生成统一社会信用代码河北君安电力工程
        credit_code = get_driver.generate_uscc()
        #输入企业统一社会信用代码
        get_driver.get_element('glqy','yingyezz').send_keys(credit_code)
        # get_driver.get_element('glqy', 'yingyezz').send_keys('911404001107629706')
        #输入法人姓名
        frname=get_driver.generate_name()
        get_driver.get_element('smrz','farnname').send_keys(frname)
        #get_driver.get_element('smrz','farnname').send_keys('')
        #输入法人身份证号
        fridnum=get_driver.generate_id()
        #fridnum = get_driver.generate_id()
        get_driver.get_element('smrz','farnzjno').send_keys(fridnum)
        #get_driver.get_element('smrz','farnzjno').send_keys('')
        #输入身份证开始时间
        get_driver.get_element('smrz','credstarttime').send_keys('2023-07-18')
        #输入身份证结束时间
        get_driver.get_element('smrz','credendtime').send_keys('2043-07-18')
        #输入法人手机号
        frtel=get_driver.generate_phone_number()
        get_driver.get_element('smrz','farnshji').send_keys(frtel)
        #点击企业规模
        qygm=Select(get_driver.get_element('glqy', 'qiygm'))
        qygm.select_by_visible_text("大型企业")
        #点击大区
        qygm=Select(get_driver.get_element('glqy', 'areaSelect'))
        qygm.select_by_visible_text("华中")
        sleep(3)
        #点击省
        qygm=Select(get_driver.get_element('glqy', 'provinceSelect'))
        qygm.select_by_visible_text("河南省")
        #点击市
        qygm=Select(get_driver.get_element('glqy', 'citySelect'))
        qygm.select_by_visible_text("郑州市")
        #点击县
        qygm=Select(get_driver.get_element('glqy', 'regionSelect'))
        qygm.select_by_visible_text("管城回族区")
        #输入详细地址
        get_driver.get_element('glqy','streetname').send_keys('中兴南路309号河南商会大厦26层')
        # 点击获取验证码
        get_driver.get_element('glqy', 'sendSms').click()
        # 输入验证码
        get_driver.get_element('glqy', 'code').send_keys('999999')
        # 点击下一步
        get_driver.get_element('glqy', 'nextBtn').click()
        # with allure.step("验证关联企业成功"):
        #     result = get_driver.get_element('glqy', 'khcg')
        #     assert result.text == "开户信息审核中，请耐心等待！"














if __name__ == "__main__":
        pytest.main()