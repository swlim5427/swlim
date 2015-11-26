# -*- coding: utf-8 -*-
from pubaction import *

def messageCloudCardList(driver,picFlile):

    funcName = "云卫士刷卡_"
    if checkTag(driver) == "message":
        inTagMessageAtion = 1
    else:
        picName_in ="message_main_yws.png"
        inTagMessageAtion = inTagMessage(driver,picFlile,picName_in,funcName)

    if inTagMessageAtion == 1:
        try:
            driver.find_element_by_name('云卫士刷卡').click()
            time.sleep(1)
            path = picFlile+"weixueyuan_ywslist.png"
            screenshot(driver,path)
            logging.info(u"进入云卫士刷卡列表")
            time.sleep(1)

            try:
                checkInList = driver.find_elements_by_id("com.tuxing.app.teacher:id/home_current_card_head")
                checkInListPic = driver.find_elements_by_class_name("android.widget.ImageView")
                checkInListPic[1].click()
                path = picFlile+"weixueyuan_ywslist_pic.png"
                screenshot(driver,path)
                logging.info(u"查看刷卡照片成功")
                time.sleep(2)
            except:
                logging.error(u"查看刷卡照片失败")
            try:
                driver.find_element_by_id("com.tuxing.app.teacher:id/wivPhoto").click()
                path = picFlile+"weixueyuan_ywslist_pic_back.png"
                screenshot(driver,path)
                logging.info(u"刷卡照片返回成功")
                time.sleep(2)
            except:
                logging.error(u"刷卡照片返回失败")

            picName_list_back = "weixueyuan_ywslist_list_back.png"
            backButton(driver,picFlile,picName_list_back,funcName+"列表_")

        except:
            logging.error(u"打开云卫士刷卡记录失败")
    else:
        try:
            logging.info("进入消息返回值 = "+str(inTagHomeAtion))
        except:
            print traceback.print_exc()
