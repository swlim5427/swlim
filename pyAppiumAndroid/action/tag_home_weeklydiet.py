# -*- coding: utf-8 -*-
import time
import logging
from screenshot import *


def tagHomeWeeklydiet(driver,picFlile):
    picName_in ="jiayuan_main_byweeklydiet.png"
    funcName = "食谱_"
    inTagHome(driver,picFlile,picName_in,funcName)
    try:
        driver.find_element_by_name('食谱').click()
        time.sleep(2)
        path = picFlile+"wjiayuan_weeklydiet_list.png"
        screenshot(driver,path)
        logging.info(u"进入家园-食谱成功")
        time.sleep(1)

        try:
            for i in range(1):
                driver.swipe(start_x=313,start_y=1163,end_x=313,end_y=300,duration=600)
                time.sleep(1)
                path = picFlile+"weeklydiet_list_up_"+str(i+1)+".png"
                screenshot(driver,path)
                logging.info(u"食谱上翻:"+str(i+1))
                time.sleep(1)
            for j in range(1):
                driver.swipe(start_x=313,start_y=1163,end_x=313,end_y=209,duration=600)
                time.sleep(1)
                path = picFlile+"weeklydiet_list_down_"+str(j+1)+".png"
                screenshot(driver,path)
                logging.info(u"食谱下翻:"+str(j+1))
                time.sleep(1)
        except:
            logging.error(u"食谱上下翻页失败")

        try:
            for i in range(1):
                driver.swipe(start_x=698,start_y=703,end_x=34,end_y=703,duration=500)
                time.sleep(1)
                path = picFlile+"weeklydiet_list_right_"+str(i+1)+".png"
                screenshot(driver,path)
                logging.info(u"食谱右翻:"+str(i+1))
                time.sleep(1)
            for j in range(1):
                driver.swipe(start_x=34,start_y=703,end_x=698,end_y=703,duration=500)
                time.sleep(1)
                path = picFlile+"weeklydiet_list_left_"+str(j+1)+".png"
                screenshot(driver,path)
                logging.info(u"食谱左翻:"+str(j+1))
                time.sleep(1)
        except:
            logging.error(u"微学园列表左右翻页失败")

        try:
            for i in range(1):
                rightButton = driver.find_element_by_id("com.tuxing.app.teacher:id/right")
                rightButton.click()
                time.sleep(2)
                path = picFlile+"weeklydiet_list_rightButton_"+str(i+1)+".png"
                screenshot(driver,path)
                logging.info(u"食谱右箭头翻页:"+str(i+1))
                time.sleep(1)
        except:
            logging.error(u"食谱右箭头翻页失败")
        try:
            for i in range(1):
                leftButon = driver.find_element_by_id("com.tuxing.app.teacher:id/left")
                leftButon.click()
                time.sleep(2)
                path = picFlile+"weeklydiet_list_leftButton_"+str(i+1)+".png"
                screenshot(driver,path)
                logging.info(u"食谱左箭头翻页:"+str(i+1))
                time.sleep(1)
        except:
            logging.error(u"食谱左箭头翻页失败")

        picName_out = "jiayuan_main_byweeklydiet_back.png"
        backButton(driver,picFlile,picName_out,funcName)
        '''
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
        '''
    except:
        logging.info(u"进入家园-食谱失败")