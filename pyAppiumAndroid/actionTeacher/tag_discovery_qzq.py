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
            driver.find_element_by_name('亲子圈').click()
            time.sleep(2)
            path = picFlile+u"发现_亲子圈列表.png"
            screenshot(driver,path)
            logging.info(u"进入发现-亲子圈成功")
            time.sleep(1)
            try:
                driver.find_element_by_id("com.tuxing.app.teacher:id/ll_portrait").click()
                time.sleep(2)
                path = picFlile+u"发现_亲子圈_教师头像进入.png"
                screenshot(driver,path)
                logging.info(u"进入发现-教师头像进入成功")
                try:
                    driver.find_element_by_id("com.tuxing.app.teacher:id/ll_right").click()
                    time.sleep(1)
                    path = picFlile+u"发现_亲子圈_教师头像_消息列表.png"
                    screenshot(driver,path)
                    logging.info(u"进入发现-教师头像-进入消息列表成功")

                except:
                    logging.error(u"进入发现-教师头像-进入消息列表失败  ")
            except:
                logging.error(u"进入发现-教师头像进入失败")




        except:
            logging.error(u"进入发现-亲子圈失败")