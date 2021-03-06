# -*- coding: utf-8 -*-
from pubaction import *

def messageCloudCardList(actionTypeMessage):
    driver = actionTypeMessage["driver"]
    picFlile = actionTypeMessage["picFlile"]
    funcName = "云卫士刷卡_"
    if checkTag(driver) == "message":
        inTagMessageAtion = 1
    else:
        picName_in =u"消息_云卫士刷卡.png"
        inTagMessageAtion = inTagMessage(driver,picFlile,picName_in,funcName)

    if inTagMessageAtion == 1:
        try:
            driver.find_element_by_name('云卫士刷卡').click()
            time.sleep(1)
            path = picFlile+u"消息_云卫士刷卡列表.png"
            screenshot(driver,path)
            logging.info(u"进入云卫士刷卡列表")
            time.sleep(1)

            try:
                checkInList = driver.find_elements_by_id("com.tuxing.app.teacher:id/home_current_card_head")
                checkInListPic = driver.find_elements_by_class_name("android.widget.ImageView")
                checkInListPic[1].click()
                path = picFlile+u"消息_云卫士刷卡列表_图片.png"
                screenshot(driver,path)
                logging.info(u"查看刷卡照片成功")
                time.sleep(2)
            except:
                logging.error(u"查看刷卡照片失败")
            try:
                driver.find_element_by_id("com.tuxing.app.teacher:id/wivPhoto").click()
                path = picFlile+u"消息_云卫士刷卡列表_图片返回.png"
                screenshot(driver,path)
                logging.info(u"刷卡照片返回成功")
                time.sleep(2)
            except:
                logging.error(u"刷卡照片返回失败")

            picName_list_back = u"消息_云卫士刷卡列表返回.png"
            backButton(driver,picFlile,picName_list_back,funcName+"列表_")

        except:
            logging.error(u"打开云卫士刷卡记录失败")
    else:
        try:
            logging.info("进入消息返回值 = "+str(inTagMessageAtion))
        except:
            print traceback.print_exc()
