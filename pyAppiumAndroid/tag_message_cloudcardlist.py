# -*- coding: utf-8 -*-
import time
import logging
from screenshot import *


def messageCloudCardList(driver,picFlile):
        ###----------------（消息-云卫士刷卡-进入列表）-------------------
    try:
        driver.find_element_by_name('云卫士刷卡').click()
        path = picFlile+"weixueyuan_ywslist.png"
        screenshot(driver,path)
        logging.info(u"进入云卫士刷卡列表")
        time.sleep(1)
    except:
        logging.error(u"打开云卫士刷卡记录失败")
    ###----------------（消息-云卫士刷卡-查看照片）-------------------
    try:
        checkInList = driver.find_elements_by_id("com.tuxing.app.teacher:id/home_current_card_head")
        checkInListPic = driver.find_elements_by_class_name("android.widget.ImageView")
        checkInListPic[1].click()
        path = picFlile+"weixueyuan_ywslist_pic.png"
        screenshot(driver,path)
        logging.info(u"查看刷卡照片成功")
        time.sleep(2)
    except:
        logging.error(u"查看刷卡照片失败")
    ###----------------（消息-云卫士刷卡-查看照片-返回列表）-------------------
    try:
        driver.find_element_by_id("com.tuxing.app.teacher:id/wivPhoto").click()
        path = picFlile+"weixueyuan_ywslist_pic_back.png"
        screenshot(driver,path)
        logging.info(u"刷卡照片返回成功")
        time.sleep(2)
    except:
        logging.error(u"刷卡照片返回失败")
    ###----------------（消息-云卫士刷卡-列表返回消息）-------------------
    try:
        wxyDetailsBack = driver.find_element_by_name("返 回")
        wxyDetailsBack.click()
        time.sleep(1)
        path = picFlile+"weixueyuan_list_back.png"
        screenshot(driver,path)
        logging.info(u"云卫士刷卡列表返回成功")
        time.sleep(1)
    except:
        logging.error(u"云卫士刷卡列表返回失败")
