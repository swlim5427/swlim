# -*- coding: utf-8 -*-
from pubaction import *

def tatMyChildAttendance(actionTypeMessage):
    driver = actionTypeMessage["driver"]
    picFlile = actionTypeMessage["picFlile"]
#    homeIconType = int(actionTypeMessage["homeIconType"])
    appType = actionTypeMessage["appType"]
    funcName = "宝宝考勤_"

    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in ="jiayuan_main_childattendance.png"
        inTagHomeAtion = inTagHome(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        try:
            homeIconType = checkAcction(driver,u"宝宝考勤")
        except Exception as e:
            print(e)
        except IOError as f :
            print(f)
        try:
            driver.find_elements_by_id("com.tuxing.app.teacher:id/home_item_icon")[homeIconType].click()
            time.sleep(2)
            screenshot(driver,picFlile+u"家园_进入宝宝考勤.png")
            logging.info(u"进入宝宝考勤成功")
            time.sleep(2)
            try:
                driver.find_element_by_id("com.tuxing.app.home:id/prevMonth").click()
                time.sleep(2)
                screenshot(driver,picFlile+u"宝宝考勤-上一月.png")
                logging.info(u"宝宝考勤-翻上一月成功")
                time.sleep(1)
                try:
                    driver.find_element_by_id("com.tuxing.app.home:id/nextMonth").click()
                    time.sleep(2)
                    screenshot(driver,picFlile+u"宝宝考勤-下一月.png")
                    logging.info(u"宝宝考勤-翻下一月成功")
                    time.sleep(1)
                except:
                    logging.info(u"宝宝考勤-翻下一月失败")
            except:
                logging.error(u"宝宝考勤-翻上一月失败")

            try:
                driver.find_element_by_name("刷卡记录")
                try:
                    checkInList = driver.find_elements_by_id("com.tuxing.app.home:id/home_card_head")
                    checkInListPic = driver.find_elements_by_class_name("android.widget.ImageView")
                    checkInListPic[1].click()
                    path = picFlile+u"宝宝考勤_刷卡列表_图片.png"
                    screenshot(driver,path)
                    logging.info(u"宝宝考勤_查看刷卡照片成功")
                    time.sleep(2)
                except:
                    logging.error(u"宝宝考勤_查看刷卡照片失败")
                try:
                    driver.find_element_by_id("com.tuxing.app.home:id/wivPhoto").click()
                    path = picFlile+u"宝宝考勤_云卫士刷卡列表_图片返回.png"
                    screenshot(driver,path)
                    logging.info(u"宝宝考勤_刷卡照片返回成功")
                    time.sleep(2)
                except:
                    logging.error(u"宝宝考勤_刷卡照片返回失败")
                try:
                    for j in range(3):
                        driver.swipe(start_x=313,start_y=1163,end_x=313,end_y=209,duration=600)
                        time.sleep(1)
                        path = picFlile+u"宝宝考勤-刷卡记录下拉"+str(j+1)+".png"
                        screenshot(driver,path)
                        logging.info(u"宝宝考勤-刷卡记录下拉成功"+str(j+1))
                        time.sleep(1)
                    for i in range(3):
                        driver.swipe(start_x=313,start_y=209,end_x=313,end_y=1163,duration=600)
                        time.sleep(1)
                        path = picFlile+u"宝宝考勤-刷卡记录上拉"+str(i+1)+".png"
                        screenshot(driver,path)
                        logging.info(u"宝宝考勤-刷卡记录上拉成功"+str(i+1))
                        time.sleep(1)

                except:
                    logging.error(u"宝宝考勤-刷卡记录拖动失败")
            except:
                logging.error(u"进入宝宝考勤-刷卡记录失败")

            picName_list_back = u"宝宝考勤-刷卡列表返回.png"
            backButton(driver,picFlile,picName_list_back,funcName+"刷卡列表_")

            picName_list_back = u"宝宝考勤-返回.png"
            backButton(driver,picFlile,picName_list_back,funcName)
        except:
            logging.error(u"进入宝宝考勤失败")