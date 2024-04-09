# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_qspz.py

"""

from time import sleep

import pytest
import allure
import locale
from base import base

@allure.feature("供应商-签收凭证")
class test_qsdfpz():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_XT', method.__name__)



    @allure.story("签收平台内签发电费类债权凭证")
    def test_qsdfpz(self,get_driver):
        #用户登录
        get_driver.start_houtai(1,'供应商')
        # 设置当前的locale为你所使用的地区的格式
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        amount=get_driver.get_paras('voucheramount', 1)
        if isinstance(amount, float):  # Check if amount is a float
            amount_str = str(amount)  # Convert float to string
            if amount.is_integer():
                # If the amount is an integer, convert it to string and remove the '.0'
                amount_str = amount_str[:-2]
            else:
                # If the amount has decimals, remove the decimal point
                amount_str = amount_str.replace('.', '')

            vchamount = int(amount_str)
        else:
            # If amount is not a float, assume it's already a string
            vchamount = int(amount.replace(',', '').replace('.', '').replace('元', ''))
        #点击签收凭证
        divs = get_driver.get_elements('mytodo', 'div_locator')
        # 定义一个标志变量
        should_break = False
        for div in divs:
            table = div.find_element_by_tag_name('table')
            # 迭代每个 <table> 元素,内层循环
            for tr in table.find_elements_by_tag_name('tr'):
                # 获取此行中的每个单元格 <td>，并获取该单元格的文本
                tds = tr.find_elements_by_tag_name('td')
                if len(tds) < 2:
                    continue
                col1_element = tds[1]  # 获取第二列元素
                last_cell = tds[-1]  # 获取最后一列元素
                lasttxt=last_cell.text
                if lasttxt=='签收凭证':
                    p_element1 = col1_element.find_element_by_xpath('.//p[1]')  # 在第一列的元素上查找 'p' 标签
                    voucheramount = p_element1.text  # 获取第二列的 'p' 标签文本
                    amt = int(voucheramount.replace(',', '').replace('.', '').replace('元', ''))
                    yfamt = float(voucheramount.replace(',', '').replace('元', ''))
                    pzamt=str(yfamt)
                    # 检查第一列和第二列是否等于指定的值，如果是，则单击该行元素中的“签收凭证”按钮
                    if vchamount == amt:
                        last_cell.click()
                        # 设置标志变量为 True，表示应该跳出外层循环
                        should_break = True
                        break
            # 检查标志变量是否为 True，如果是，则跳出外层循环
            if should_break:
                break
        # # 点击签署按钮
        # table = get_driver.get_element('mytodo', 'qianshu')
        # tbody = table.find_element_by_tag_name('tbody')
        # for tr in tbody.find_elements_by_tag_name('tr'):
        #     for a in tr.find_elements_by_tag_name('a'):
        #         if a.text == '签署':
        #             a.click()
        #             sleep(11)
        #             # 点击签署页面确定按钮按钮
        #             get_driver.get_element('mytodo', 'okBtn').click()
        #             sleep(5)
        #             break
        # 点击签署按钮
        qsbtns = get_driver.get_elements('mytodo', 'qianshu')
        for qsbtn in qsbtns:
            qsbtn.click()
            sleep(11)
            # 点击签署页面确定按钮
            get_driver.get_element('mytodo', 'okBtn').click()
            # 等待弹窗出现，设置一个合理的等待时间
            try:
                # 如果弹窗出现，则执行获取验证码按钮点击操作
                getcode = get_driver.get_element('mytodo', 'getcode')
                getcode.click()
                # 输入验证码
                get_driver.get_element('mytodo', 'smscode').send_keys('999999')
                # 点击验证码页面确定按钮
                get_driver.get_element('mytodo', 'qdbtn').click()
            except:
                # 如果没有弹窗出现，则什么都不做，继续后面的脚本执行
                pass
            sleep(2)
        # 输入审核意见
        get_driver.get_element('mytodo', 'commentinput').send_keys('脚本自动签收凭证')
        # 点击提交申请按钮
        get_driver.get_element('mytodo', 'subBtn').click()
        sleep(10)
        with allure.step("验证该凭证已签收成功"):
            # 点击融资管理tab
            get_driver.get_element('homepage', 'rongziguanli_tab').click()
            # 点击电子债权凭证
            get_driver.get_element('rongziguanli-dzzqpz', 'dzzqpz').click()
            # 点击已签收
            get_driver.get_element('rongziguanli-dzzqpz', 'yiqianshou').click()
            # 输入凭证金额
            get_driver.get_element('rongziguanli-dzzqpz', 'vouchmoney').send_keys(pzamt)
            # 点击查询
            get_driver.get_element('rongziguanli-dzzqpz', 'searchButton').click()
            sleep(2)
            #获取凭证编号，存到参数表中
            vouchernum = get_driver.get_element('rongziguanli-dzzqpz', 'qqbh').text  # 获取第一列元素
            with allure.step("将凭证编号存到参数表中"):
                get_driver.parameter('test_XT', 'case', 'vouchernum', vouchernum, 1)
            result = get_driver.get_element('rongziguanli-dzzqpz', 'yqscxresult')
            assert result.text == "共有1条，每页显示：20条"

if __name__ == "__main__":
        pytest.main()
