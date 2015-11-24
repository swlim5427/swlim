# -*- coding: utf-8 -*-
import traceback
from pubaction import *

def tagHomeAnnouncement(driver,picFlile):
    funcName = "公告_"
    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in ="jiayuan_main_announcement.png"
        inTagHomeAtion = inTagHome(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        try:
            driver.find_element_by_name("公告").click()
            time.sleep(2)
            screenshot(driver,picFlile+"jiayuan_announcement_list.png")
            logging.info(u"进入公告成功")
            time.sleep(2)

            try:
                announcemenList = driver.find_elements_by_class_name("android.widget.LinearLayout")
                announcemenList[5].click()
                screenshot(driver,picFlile+"jiayuan_announcement_details.png")
                time.sleep(2)
                logging.info(u"查看公告详情")
                time.sleep(2)
            except:
                logging.error(u"查看公告详情失败")

            picName_details_back = "wjiayuan_announcement_details_back.png"
            backButton(driver,picFlile,picName_details_back,funcName+"详情_")
            picName_list_back = "wjiayuan_announcement_list_back.png"
            backButton(driver,picFlile,picName_list_back,funcName+"列表_")

        except:
            logging.error(u"进入公告失败")


    else:
        try:
            logging.info("进入家园返回值 = "+str(inTagHomeAtion))
        except:
            print traceback.print_exc()
