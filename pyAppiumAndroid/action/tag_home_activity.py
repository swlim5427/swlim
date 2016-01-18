# -*- coding: utf-8 -*-
from pubaction import *

def tagHomeActivity(actionTypeMessage):
    driver = actionTypeMessage["driver"]
    picFlile = actionTypeMessage["picFlile"]
    homeIconType = int(actionTypeMessage["homeIconType"])
    appType = actionTypeMessage["appType"]

    funcName = "活动_"
    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in =u"家园_主页_活动.png"
        inTagHomeAtion = inTagHome(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        if appType == 1:
            try:
                driver.find_elements_by_id("com.tuxing.app.teacher:id/home_item_icon")[homeIconType].click()
                time.sleep(2)
                path = picFlile+u"家园_活动列表.png"
                screenshot(driver,path)
                logging.info(u"进入家园-活动成功")
                time.sleep(1)

                try:
                    homeActivityList = driver.find_elements_by_class_name("android.widget.LinearLayout")
                    homeActivityList[5].click()
                    time.sleep(2)
                    path = picFlile+u"家园_活动详情.png"
                    screenshot(driver,path)
                    time.sleep(1)
                    logging.info(u"进入家园-活动详情成功")
                except:
                    logging.info(u"进入家园-活动详情失败")

                picName_details_back = u"家园_活动详情_返回.png"
                backButton(driver,picFlile,picName_details_back,funcName+"详情_")

                picName_list_back = u"家园_活动列表_返回.png"
                backButton(driver,picFlile,picName_list_back,funcName+"列表_")
            except:
                logging.info(u"进入家园-活动失败")
        elif appType == 2:
            try:
                driver.find_elements_by_id("com.tuxing.app.home:id/home_item_icon")[homeIconType].click()
                time.sleep(2)
                path = picFlile+u"家园_活动列表.png"
                screenshot(driver,path)
                logging.info(u"进入家园-活动成功")
                time.sleep(1)

                try:
                    homeActivityList = driver.find_elements_by_class_name("android.widget.LinearLayout")
                    homeActivityList[5].click()
                    time.sleep(2)
                    path = picFlile+u"家园_活动详情.png"
                    screenshot(driver,path)
                    time.sleep(1)
                    logging.info(u"进入家园-活动详情成功")
                except:
                    logging.info(u"进入家园-活动详情失败")

                picName_details_back = u"家园_活动详情_返回.png"
                backButton(driver,picFlile,picName_details_back,funcName+"详情_")

                picName_list_back = u"家园_活动列表_返回.png"
                backButton(driver,picFlile,picName_list_back,funcName+"列表_")
            except:
                logging.info(u"进入家园-活动失败")
    else:
        try:
            logging.info("进入家园返回值 = "+str(inTagHomeAtion))
        except:
            print traceback.print_exc()