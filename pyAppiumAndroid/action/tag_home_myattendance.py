# -*- coding: utf-8 -*-
from pubaction import *

def tagHomeMyAttendance(actionTypeMessage):
    driver = actionTypeMessage["driver"]
    picFlile = actionTypeMessage["picFlile"]
    homeIconType = int(actionTypeMessage["homeIconType"])
    appType = actionTypeMessage["appType"]
    funcName = "我的考勤_"
    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in =u"家园_主页_我的考勤.png"
        inTagHomeAtion = inTagMessage(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        try:
            driver.find_elements_by_id("com.tuxing.app.teacher:id/home_item_icon")[homeIconType].click()
            time.sleep(1)
            path = picFlile+u"家园_我的考勤列表.png"
            screenshot(driver,path)
            logging.info(u"进入我的考勤刷卡列表")
            time.sleep(1)

            try:
                checkInList = driver.find_elements_by_id("com.tuxing.app.teacher:id/home_current_card_head")
                checkInListPic = driver.find_elements_by_class_name("android.widget.ImageView")
                checkInListPic[1].click()
                path = picFlile+u"家园_我的考勤列表_图片.png"
                screenshot(driver,path)
                logging.info(u"我的考勤-查看刷卡照片成功")
                time.sleep(2)
            except:
                logging.error(u"我的考勤-查看刷卡照片失败")
            try:
                driver.find_element_by_id("com.tuxing.app.teacher:id/wivPhoto").click()
                path = picFlile+u"家园_我的考勤列表_图片_返回.png"
                screenshot(driver,path)
                logging.info(u"我的考勤-刷卡照片返回成功")
                time.sleep(2)
            except:
                logging.error(u"我的考勤-刷卡照片返回失败")

            picName_list_back = u"家园_我的考勤列表_返回.png"
            backButton(driver,picFlile,picName_list_back,funcName+"列表_")

        except:
            logging.error(u"进入我的考勤刷卡列表失败")
    else:
        try:
            logging.info("进入消息返回值 = "+str(inTagHomeAtion))
        except:
            print traceback.print_exc()
