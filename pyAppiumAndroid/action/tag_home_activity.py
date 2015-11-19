# -*- coding: utf-8 -*-
import time
import logging
from screenshot import *


def tagHomeActivity(driver,picFlile):
    try:
        driver.find_element_by_name('活动').click()
        time.sleep(2)
        path = picFlile+"wjiayuan_activity_list.png"
        screenshot(driver,path)
        logging.info(u"进入家园-活动成功")
        time.sleep(1)
    except:
        logging.info(u"进入家园-活动失败")
    try:
        homeActivityList = driver.find_elements_by_class_name("android.widget.LinearLayout")
        homeActivityList[5].click()
        time.sleep(2)
        path = picFlile+"wjiayuan_activity_details.png"
        screenshot(driver,path)
        time.sleep(1)
        logging.info(u"进入家园-活动详情成功")
    except:
        logging.info(u"进入家园-活动详情失败")
    try:
        wxyDetailsBack = driver.find_element_by_name("返 回")
        wxyDetailsBack.click()
        time.sleep(2)
        path = picFlile+"wjiayuan_activity_details_back.png"
        screenshot(driver,path)
        logging.info(u"家园-活动详情返回成功")
        time.sleep(2)
    except:
        logging.error(u"家园-活动详情返回失败")
    try:
        wxyDetailsBack = driver.find_element_by_name("返 回")
        wxyDetailsBack.click()
        time.sleep(2)
        path = picFlile+"wjiayuan_activity_list_back.png"
        screenshot(driver,path)
        logging.info(u"家园-活动详情返回成功")
        time.sleep(2)
    except:
        logging.error(u"家园-活动详情返回失败")