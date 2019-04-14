#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 创建浏览器对象
print("Chrome is starting...")
opt = webdriver.ChromeOptions()
opt.set_headless()
driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver.exe', options=opt)

driver.get("https://tco.aliyun.com/tco/ecs/calculator?spm=5176.8030368.1058474.1.22c43aa4TZEd79")

# 打印页面标题
print(driver.title)

# 生成当前页面快照
# driver.save_screenshot("baidu.png")

# 获取选择框的元素集合
element_select = driver.find_elements("css selector", ".bk-select-group-arrow")
# 获取地域下拉框
element_region = element_select[0]
# 模拟点击地域下拉框
element_region.click()
# 获取下拉框的值
element_region_detail = driver.find_elements("css selector", ".bk-select-option")
#

# 遍历地域下拉框值元素
# for each in element_region_detail:
#     # 模拟下拉框值选中
#     each.click()
#     driver.save_screenshot("u" + each.text + ".png")

# 关闭浏览器
driver.quit()
