# -*- coding: utf-8 -*-
import time
import logging
from screenshot import *

def weixueyuan(driver,picFlile):
    try:
        wxy = driver.find_element_by_name('微学园')
        wxy.click()
        time.sleep(2)
        screenshot(driver,picFlile+"weixueyuan_list.png")
        logging.info(u"进入微学园列表")
        time.sleep(2)
    except:
        logging.error(u"微学园列表进入失败")
    ###----------------（消息-微学园-列表翻页）-------------------
    try:
        for i in range(1):
            driver.swipe(start_x=313,start_y=209,end_x=313,end_y=1163,duration=600)
            time.sleep(1)
            path = picFlile+"weixueyuan_list_up_"+str(i+1)+".png"
            screenshot(driver,path)
            logging.info(u"微学园列表上翻:"+str(i+1))
            time.sleep(1)
        for j in range(1):
            driver.swipe(start_x=313,start_y=1163,end_x=313,end_y=209,duration=600)
            time.sleep(1)
            path = picFlile+"weixueyuan_list_down_"+str(j+1)+".png"
            screenshot(driver,path)
            logging.info(u"微学园列表下翻:"+str(j+1))
            time.sleep(1)
    except:
        logging.error(u"微学园列表翻页失败")
    ###----------------（消息-微学园-内容详情）-------------------
    try:
        time.sleep(1)
        wxyList = driver.find_element_by_id("com.tuxing.app.teacher:id/lyceum_top_pic")
        wxyList.click()
        #       positions = []
        #       positions.append((361,806))
        #       driver.tap(positions)
        time.sleep(1)
        path = picFlile+"weixueyuan_list_details.png"
        screenshot(driver,path)
        logging.info(u"进入微学园内容详情")
        time.sleep(1)
    except:
        logging.error(u"微学园内容详情进入失败")
    ###----------------（消息-微学园-内容上下拖动）-------------------
    try:
        for j in range(2):
            driver.swipe(start_x=313,start_y=1163,end_x=313,end_y=209,duration=600)
            time.sleep(1)
            path = picFlile+"weixueyuan_list_down_details"+str(j+1)+".png"
            screenshot(driver,path)
            logging.info(u"详情下拉成功"+str(j+1))
            time.sleep(1)
        for i in range(2):
            driver.swipe(start_x=313,start_y=209,end_x=313,end_y=1163,duration=600)
            time.sleep(1)
            path = picFlile+"weixueyuan_list_up_details"+str(i+1)+".png"
            screenshot(driver,path)
            logging.info(u"详情上拉成功"+str(i+1))
            time.sleep(1)
    except:
        logging.error(u"详情拖动失败")
    ###----------------（消息-微学园-内容返回列表）-------------------
    try:
        wxyDetailsBack = driver.find_element_by_name("返 回")
        wxyDetailsBack.click()
        time.sleep(1)
        path = picFlile+"weixueyuan_details_back.png"
        screenshot(driver,path)
        logging.info(u"详情返回成功")
        time.sleep(1)
    except Exception,e:
        logging.error(e)
        logging.error(u"详情返回失败")
    ###----------------（消息-微学园-列表返回消息）-------------------
    try:
        wxyDetailsBack = driver.find_element_by_name("返 回")
        wxyDetailsBack.click()
        time.sleep(1)
        path = picFlile+"weixueyuan_list_back.png"
        screenshot(driver,path)
        logging.info(u"详情列表返回成功")
        time.sleep(1)
    except:
        logging.error(u"详情返回失败")
