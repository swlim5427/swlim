# -*- coding: utf-8 -*-
from pubaction import *
import StringIO

def tagHomeNotice(driver,picFlile):
    funcName = "通知_"
    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in ="home_main_notice.png"
        inTagHomeAtion = inTagMessage(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        try:
            driver.find_element_by_name("通知").click()
            time.sleep(2)
            screenshot(driver,picFlile+"jiayuan_notice_list.png")
            logging.info(u"进入通知成功")
            time.sleep(1)

        except:
            logging.error(u"进入通知失败")