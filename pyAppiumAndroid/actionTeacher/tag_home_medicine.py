# -*- coding: utf-8 -*-
from pubaction import *

def tagHomeMedicine(driver,picFlile,appType):
    funcName = "喂药_"
    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in =u"家园_主页_喂药.png"
        inTagHomeAtion = inTagHome(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        try:
            driver.find_element_by_name("喂药").click()
            time.sleep(2)
            screenshot(driver,picFlile+u"家园_喂药列表.png")
            logging.info(u"进入喂药成功")
            time.sleep(2)

            try:
                announcemenList = driver.find_elements_by_class_name("android.widget.ImageView")
                announcemenList[1].click()
                time.sleep(2)
                screenshot(driver,picFlile+u"家园_喂药详情.png")
                logging.info(u"查看喂药详情")
                time.sleep(2)
            except:
                logging.error(u"查看喂药详情失败")

            picName_details_back = u"家园_喂药详情_返回.png"
            backButton(driver,picFlile,picName_details_back,funcName+"详情_")
            picName_list_back = u"家园_喂药列表_返回.png"
            backButton(driver,picFlile,picName_list_back,funcName+"列表_")
        except:
            logging.error(u"进入喂药失败")


    else:
        try:
            logging.info("进入家园返回值 = "+str(inTagHomeAtion))
        except:
            print traceback.print_exc()
