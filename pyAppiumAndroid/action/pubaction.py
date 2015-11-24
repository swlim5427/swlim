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
               return "descovery"
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