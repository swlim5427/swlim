# -*- coding: utf-8 -*-
from pubaction import *

def tagHomeAnnouncement(actionTypeMessage):
    driver = actionTypeMessage["driver"]
    picFlile = actionTypeMessage["picFlile"]
#   homeIconType = int(actionTypeMessage["homeIconType"])
    appType = actionTypeMessage["appType"]
    funcName = "公告_"
    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in =u"家园_主页_公告.png"
        inTagHomeAtion = inTagHome(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        try:
            homeIconType = checkAcction(driver,u"公告")
        except Exception as e:
            print(e)
        except IOError as f :
            print(f)
        if appType == 1:

            try:
                driver.find_elements_by_id("com.tuxing.app.teacher:id/home_item_icon")[homeIconType].click()
                time.sleep(2)
                screenshot(driver,picFlile+u"家园_公告列表.png")
                logging.info(u"进入公告成功")
                time.sleep(2)

                try:
                    announcemenList = driver.find_elements_by_class_name("android.widget.LinearLayout")
                    announcemenList[5].click()
                    time.sleep(2)
                    screenshot(driver,picFlile+u"家园_公告详情.png")
                    logging.info(u"查看公告详情")
                    time.sleep(2)
                except:
                    logging.error(u"查看公告详情失败")

                picName_details_back = u"家园_公告详情_返回.png"
                backButton(driver,picFlile,picName_details_back,funcName+"详情_")
                picName_list_back = u"家园_公告列表_返回.png"
                backButton(driver,picFlile,picName_list_back,funcName+"列表_")

            except:
                logging.error(u"进入公告失败")
        elif appType == 2:
            try:
                driver.find_elements_by_id("com.tuxing.app.home:id/home_item_icon")[homeIconType].click()
                time.sleep(2)
                screenshot(driver,picFlile+u"家园_公告列表.png")
                logging.info(u"进入公告成功")
                time.sleep(2)

                try:
                    announcemenList = driver.find_elements_by_class_name("android.widget.LinearLayout")
                    announcemenList[5].click()
                    time.sleep(2)
                    screenshot(driver,picFlile+u"家园_公告详情.png")
                    logging.info(u"查看公告详情")
                    time.sleep(2)
                except:
                    logging.error(u"查看公告详情失败")

                picName_details_back = u"家园_公告详情_返回.png"
                backButton(driver,picFlile,picName_details_back,funcName+"详情_")
                picName_list_back = u"家园_公告列表_返回.png"
                backButton(driver,picFlile,picName_list_back,funcName+"列表_")

            except:
                logging.error(u"进入公告失败")
    else:
        try:
            logging.info("进入家园返回值 = "+str(inTagHomeAtion))
        except:
            print traceback.print_exc()
