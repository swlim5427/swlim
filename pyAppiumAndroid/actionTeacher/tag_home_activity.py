# -*- coding: utf-8 -*-
from pubaction import *

def tagHomeActivity(driver,picFlile):
    funcName = "活动_"
    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in ="jiayuan_main_activity.png"
        inTagHomeAtion = inTagHome(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        try:
            driver.find_element_by_name('活动').click()
            time.sleep(2)
            path = picFlile+"wjiayuan_activity_list.png"
            screenshot(driver,path)
            logging.info(u"进入家园-活动成功")
            time.sleep(1)

            try:
                homeActivityList = driver.find_elements_by_class_name("android.widget.LinearLayout")
                homeActivityList[5].click()
                time.sleep(2)
                path = picFlile+"wjiayuan_activity_details.png"
                screenshot(driver,path)
                time.sleep(1)
                logging.info(u"进入家园-活动详情成功")
            except:
                logging.info(u"进入家园-活动详情失败")

            picName_details_back = "wjiayuan_activity_details_back.png"
            backButton(driver,picFlile,picName_details_back,funcName+"详情_")

            picName_list_back = "wjiayuan_activity_list_back.png"
            backButton(driver,picFlile,picName_list_back,funcName+"列表_")
        except:
            logging.info(u"进入家园-活动失败")
    else:
        try:
            logging.info("进入家园返回值 = "+str(inTagHomeAtion))
        except:
            print traceback.print_exc()