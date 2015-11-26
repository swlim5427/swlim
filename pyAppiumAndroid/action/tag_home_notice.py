# -*- coding: utf-8 -*-
from pubaction import *

def tagHomeNotice(driver,picFlile):
    funcName = "通知_"
    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in ="home_main_notice.png"
        inTagHomeAtion = inTagMessage(driver,picFlile,picName_in,funcName)

    try:
        name = driver.find_element_by_name("通知")
    except:
        print("")