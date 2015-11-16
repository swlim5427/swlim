# -*- coding: utf-8 -*-
import time
import logging
from screenshot import *

def tagHomeAnnouncement(driver,picFlile):
    ###----------------（微家园-家园）-------------------
    try:
        wxy_jiayuan = driver.find_element_by_name("家园")
        wxy_jiayuan.click()
        time.sleep(2)
        screenshot(driver,picFlile+"jiayuan_main.png")
        time.sleep(2)
        logging.info(u"进入家园选项卡成功")
    except:
        logging.error(u"进入家园选项卡111失败")
    ###----------------（微家园-家园-进入公告列表）-------------------
    try:
        driver.find_element_by_name("公告").click()
        time.sleep(2)
        screenshot(driver,picFlile+"jiayuan_announcement_list.png")
        logging.info(u"进入公告成功")
        time.sleep(2)
    except:
        logging.error(u"进入公告失败")
    ###----------------（微家园-家园-查看公告详情）-------------------
    try:
        announcemenList = driver.find_elements_by_class_name("android.widget.LinearLayout")
        print announcemenList
        announcemenList[5].click()
        screenshot(driver,picFlile+"jiayuan_announcement_details.png")
        time.sleep(2)
        logging.info(u"查看公告详情")
        time.sleep(2)
    except:
        logging.error(u"查看公告详情失败")
    ###----------------（微家园-家园-查看公告详情-返回）-------------------
    try:
        wxyDetailsBack = driver.find_element_by_name("返 回")
        wxyDetailsBack.click()
        time.sleep(2)
        path = picFlile+"wjiayuan_announcement_details_back.png"
        screenshot(driver,path)
        logging.info(u"公告详情返回成功")
        time.sleep(2)
    except:
        logging.error(u"公告详情返回失败")
    ###----------------（微家园-家园-查看公告详情-返回）-------------------
    try:
        wxyDetailsBack = driver.find_element_by_name("返 回")
        wxyDetailsBack.click()
        time.sleep(2)
        path = picFlile+"wjiayuan_announcement_list_back.png"
        screenshot(driver,path)
        logging.info(u"公告列表返回成功")
        time.sleep(2)
    except:
        logging.error(u"公告列表返回失败")