# -*- coding: utf-8 -*-
from pubaction import *

def tagDiscoveryQzq(driver,picFlile):
    funcName = "发现_"
    if checkTag(driver) == "discovery":
        inTagDiscoveryAtion = 1
    else:
        picName_in =u"家园_主页_活动.png"
        inTagDiscoveryAtion = inTagDiscovery(driver,picFlile,picName_in,funcName)
    if inTagDiscoveryAtion == 1:
        try:
            driver.find_element_by_name('活动').click()
            time.sleep(2)
            path = picFlile+u"发现_亲子圈列表.png"
            screenshot(driver,path)
            logging.info(u"进入发现-亲子圈成功")
            time.sleep(1)
        except:
            logging.info(u"进入发现-亲子圈失败")