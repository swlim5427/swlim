# -*- coding: utf-8 -*-
import os
import logging
import traceback
from appium import webdriver
import time
from screenshot import *
import tag_message_wxy
import tag_home_announcement
import tag_message_cloudcardlist
import tag_home_activity
import sys
import threading
#def screenshot(path):
#    driver.get_screenshot_as_file(path)


actionTypeList = [1,1001,2001,2002,2003,2004,2005,2006,2007,8,9,10,11,12,13,14,15,16,17,18,19,20]

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'

desired_caps['deviceName'] = 'Xiaomi 2014501'
desired_caps['appPackage'] = 'com.tuxing.app.teacher'
desired_caps['appActivity'] = 'com.tuxing.app.SplashActivity'
#desired_caps['automationName']='Selendroid'

resultPath = r"D:/android_result_pic/"

for times in range(1,2):
    checkLogPath = os.path.isdir(resultPath)
    if not checkLogPath:
        os.makedirs(resultPath)
        logPath = resultPath
    else:
        logPath = resultPath
    checkPicPath = os.path.isdir(resultPath+str(times)+"/")
    if not checkPicPath:
        os.makedirs(resultPath+str(times)+"/")
        picFlile = (resultPath+str(times)+"/")
    else:
        picFlile = (resultPath+str(times)+"/")

    LOG_FILENAME = logPath+"testLog.log"
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=LOG_FILENAME,
                    filemode='w')
    try:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        time.sleep(8)
        screenshot(driver,picFlile+"login_main_message.png")
        logging.info(u"打开教师版app")
        time.sleep(2)

        ###----------------（微家园-教师-登录）-------------------
        try:
            wxyLoin = driver.find_element_by_name("登 录")
            screenshot(driver,picFlile+"weixueyuan_login.png")
            wxyLoin_userName = driver.find_element_by_id("com.tuxing.app.teacher:id/et_username")
            wxyLoin_userName.send_keys("14100000001")
            screenshot(driver,picFlile+"weixueyuan_login_username.png")
            time.sleep(1)
            driver.find_element_by_id("com.tuxing.app.teacher:id/et_password").send_keys("111111")
            wxyLoin.click()
            logging.info(u"登录成功")
            time.sleep(1)
        except:
            try:
                driver.find_element_by_name('微学园')
                logging.info(u"当前为免登陆状态")
            except:
                print traceback.print_exc()
                logging.error(u"登录失败")

        ###----------------（消息-微学园-列表）-------------------
        for actionTye in actionTypeList:
            if actionTye == 1:
                tag_message_wxy.weixueyuan(driver,picFlile)
            elif actionTye == 1001:
                tag_message_cloudcardlist.messageCloudCardList(driver,picFlile)
            elif actionTye == 2001:
                tag_home_announcement.tagHomeAnnouncement(driver,picFlile)
            elif actionTye == 2002:
                tag_home_activity.tagHomeActivity(driver,picFlile)

    except :
        print traceback.print_exc()
        logging.error(u"打开教师版失败")

    driver.quit()
    time.sleep(40)

