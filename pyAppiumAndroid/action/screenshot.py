# -*- coding: utf-8 -*-
import time
import logging

def screenshot(driver,path):
    driver.get_screenshot_as_file(path)

def backButton(driver,picFlile,picName,funcName):
    try:
        wxyDetailsBack = driver.find_element_by_name("返 回")
        wxyDetailsBack.click()
        time.sleep(1)
        path = picFlile+picName
        screenshot(driver,path)
        logging.info(funcName+u"返回成功")
        time.sleep(1)
    except:
        logging.error(funcName+u"返回失败")

def inTagHome(driver,picFlile,picName):
    try:
        wxy_jiayuan = driver.find_element_by_name("家园")
        wxy_jiayuan.click()
        time.sleep(2)
        screenshot(driver,picFlile+picName)
        time.sleep(2)
        logging.info(u"进入家园选项卡成功")
    except:
        logging.error(u"进入家园选项卡失败")