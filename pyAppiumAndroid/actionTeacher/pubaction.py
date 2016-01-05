# -*- coding: utf-8 -*-
import time
import logging
import datetime
import re

import traceback

def timeAction():

    inputYear = datetime.datetime.now().year
    inputMonth = datetime.datetime.now().month
    inputDay = datetime.datetime.now().day
    inputHour = datetime.datetime.now().hour
    inputMinute = datetime.datetime.now().minute
    inputSecond = datetime.datetime.now().second

    mTime = datetime.datetime.now().microsecond
    imputDateTime = datetime.datetime(year=int(inputYear),month=int(inputMonth),day=int(inputDay),
                                      hour=int(inputHour),minute=int(inputMinute),second=int(inputSecond))
    formatTime = long(round(time.mktime(imputDateTime.timetuple())))
    nowTime =  long(str(formatTime)+str(mTime/1000))
    return nowTime

def screenshot(driver,path):
    driver.get_screenshot_as_file(path)

def backButton(driver,picFlile,picName,funcName):
    try:
        wxyDetailsBack = driver.find_element_by_name("返 回")
        wxyDetailsBack.click()
        time.sleep(1)
        path = picFlile+picName
        screenshot(driver,path)
        logging.info(funcName+"返回成功")
        time.sleep(1)
    except:
        logging.error(funcName+"返回失败")

def checkTag(driver):
    try:
        driver.find_element_by_name('云卫士刷卡')
        return "message"
    except:
        try:
            driver.find_element_by_id("com.tuxing.app.teacher:id/iv_home_banner")
            return "home"
        except:
            try:
                driver.find_element_by_id("com.tuxing.app.teacher:id/fx_tv_qzq")
                return "discovery"
            except:
                try:
                   driver.find_element_by_id("com.tuxing.app.teacher:id/my_help_icon")
                   return "my"
                except:
                    return "other"

def inTagMessage(driver,picFlile,picName,funcName):
    try:
        wxy_jiayuan = driver.find_element_by_name("消息")
        wxy_jiayuan.click()
        time.sleep(2)
        screenshot(driver,picFlile+picName)
        time.sleep(2)
        logging.info(funcName+"进入消息选项卡成功")
        return 1
    except:
        logging.error(funcName+"进入消息选项卡失败")
        return 0

def inTagHome(driver,picFlile,picName,funcName):
    try:
        wxy_jiayuan = driver.find_element_by_name("家园")
        wxy_jiayuan.click()
        time.sleep(2)
        screenshot(driver,picFlile+picName)
        time.sleep(2)
        logging.info(funcName+"进入家园选项卡成功")
        return 1
    except:
        logging.error(funcName+"进入家园选项卡失败")
        return 0
def inTagDiscovery(driver,picFlile,picName,funcName):
    try:
        wxy_jiayuan = driver.find_element_by_name("发现")
        wxy_jiayuan.click()
        time.sleep(2)
        screenshot(driver,picFlile+picName)
        time.sleep(2)
        logging.info(funcName+"进入发现选项卡成功")
        return 1
    except:
        logging.error(funcName+"进入发现选项卡失败")
        return 0
def getNumber(str):
    mode = re.compile(r'\d+')
    return mode.findall(str)[0]

def actionTypeMessageCode(actionType,driver,picFlile,appType):
    if actionType == 2001:
        return {"driver":driver,"picFlile":picFlile,"homeIconType":0,"appType":appType}
    elif actionType == 2002:
        return {"driver":driver,"picFlile":picFlile,"homeIconType":1,"appType":appType}
    elif actionType == 2003:
        return {"driver":driver,"picFlile":picFlile,"homeIconType":2,"appType":appType}
    elif actionType == 2004:
        return {"driver":driver,"picFlile":picFlile,"homeIconType":3,"appType":appType}
    elif actionType == 2005:
        return {"driver":driver,"picFlile":picFlile,"homeIconType":4,"appType":appType}
    elif actionType == 2006:
        return {"driver":driver,"picFlile":picFlile,"homeIconType":6,"appType":appType}
    elif actionType == 2007:
        return {"driver":driver,"picFlile":picFlile,"homeIconType":7,"appType":appType}
    elif actionType == 2008:
        return {"driver":driver,"picFlile":picFlile,"homeIconType":8,"appType":appType}
    elif actionType == 2009:
        return {"driver":driver,"picFlile":picFlile,"homeIconType":9,"appType":appType}
    elif actionType == 1001:
        return {"driver":driver,"picFlile":picFlile,"homeIconType":9,"appType":appType}
    elif actionType == 1002:
        return {"driver":driver,"picFlile":picFlile,"homeIconType":9,"appType":appType}