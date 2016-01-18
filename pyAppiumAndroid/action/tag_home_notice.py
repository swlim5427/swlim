# -*- coding: utf-8 -*-
from pubaction import *
import StringIO

def tagHomeNotice(actionTypeMessage):
    driver = actionTypeMessage["driver"]
    picFlile = actionTypeMessage["picFlile"]
    homeIconType = int(actionTypeMessage["homeIconType"])
    appType = actionTypeMessage["appType"]
    funcName = "通知_"
    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in =u"家园_主页_通知.png"
        inTagHomeAtion = inTagMessage(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        try:
            driver.find_elements_by_id("com.tuxing.app.teacher:id/home_item_icon")[homeIconType].click()
            time.sleep(2)
            screenshot(driver,picFlile+"jiayuan_notice_list.png")
            logging.info(u"进入通知成功")
            time.sleep(1)

        except:
            logging.error(u"进入通知失败")