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
class test_qspz():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_XT', method.__name__)



    @allure.story("签收模拟山西推送的债权凭证")
    def test_qspz(self,get_driver):
        #用户登录
        get_driver.start_houtai(1,'山西电费供应商')
        # 设置当前的locale为你所使用的地区的格式
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        amount=get_driver.get_paras('voucheramount', 1)
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
                    if amount == amt:
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
            # 点击签署页面确定按钮按钮
            get_driver.get_element('mytodo', 'okBtn').click()
            sleep(5)
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
            result = get_driver.get_element('rongziguanli-dzzqpz', 'yqscxresult')
            assert result.text == "共有1条，每页显示：20条"

if __name__ == "__main__":
        pytest.main()
