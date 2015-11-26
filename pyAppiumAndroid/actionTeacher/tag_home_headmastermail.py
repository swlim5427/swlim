# -*- coding: utf-8 -*-
from pubaction import *

def tagHomeHeadMasterMail(driver,picFlile,appType):
    if appType == 1:
        funcName = "园长信箱_"
        if checkTag(driver) == "home":
            inTagHomeAtion = 1
        else:
            picName_in ="jiayuan_main_headmashtermail.png"
            inTagHomeAtion = inTagHome(driver,picFlile,picName_in,funcName)

        if inTagHomeAtion == 1:
            try:
                driver.find_element_by_name("园长信箱").click()
                time.sleep(2)
                screenshot(driver,picFlile+"jiayuan_headmashtermail_list.png")
                logging.info(u"进入园长信箱成功")
                time.sleep(2)

                try:
                    announcemenList = driver.find_elements_by_class_name("android.widget.ImageView")
                    announcemenList[1].click()
                    time.sleep(2)
                    screenshot(driver,picFlile+"wjiayuan_headmashtermail_details.png")
                    logging.info(u"查看园长信箱详情")
                    time.sleep(2)
                except:
                    logging.error(u"查看园长信箱详情失败")

                picName_details_back = "wjiayuan_headmashtermail_details_back.png"
                backButton(driver,picFlile,picName_details_back,funcName+"详情_")
                picName_list_back = "wjiayuan_headmashtermail_list_back.png"
                backButton(driver,picFlile,picName_list_back,funcName+"列表_")
            except:
                logging.error(u"进入园长信箱失败")


        else:
            try:
                logging.info("进入家园返回值 = "+str(inTagHomeAtion))
            except:
                print traceback.print_exc()
