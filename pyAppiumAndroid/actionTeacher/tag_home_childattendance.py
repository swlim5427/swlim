# -*- coding: utf-8 -*-
from pubaction import *

def attendanceCount(driver):
    try:
        attendance = driver.find_element_by_id("com.tuxing.app.teacher:id/myGridView")\
            .find_elements_by_class_name("android.widget.RelativeLayout")
        return len(attendance)
    except Exception as e:
        return 0
        print traceback.print_exc()
        print e

def tagHomeChlidAttendance(driver,picFlile):
    funcName = "幼儿考勤_"
    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in ="jiayuan_main_childattendance.png"
        inTagHomeAtion = inTagHome(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        try:
            driver.find_element_by_name("幼儿考勤").click()
            time.sleep(2)
            screenshot(driver,picFlile+"jiayuan_childattendance_enter.png")
            logging.info(u"进入幼儿考勤成功")
            time.sleep(2)
            persentNumEnter = 0
            absenceNumEnter = 0
            leaveNumEnter = 0
            persentNumChange = 0
            absenceNumChange = 0
            leaveNumChange = 0
            try:
                presentEnter = driver.find_element_by_id("com.tuxing.app.teacher:id/tv_tab_1")
                presentEnter.click()
                time.sleep(1)
                persentNumEnter = attendanceCount(driver)
                absenceEnter = driver.find_element_by_id("com.tuxing.app.teacher:id/tv_tab_2")
                absenceEnter.click()
                time.sleep(1)
                absenceNumEnter = attendanceCount(driver)
                leaveEnter = driver.find_element_by_id("com.tuxing.app.teacher:id/tv_tab_3")
                leaveEnter.click()
                time.sleep(1)
                leaveNumEnter = attendanceCount(driver)

                try:
                    absenceEnter.click()
                    time.sleep(1)
                    screenshot(driver,picFlile+"jiayuan_childattendance_absence.png")
                    time.sleep(1)
                    logging.info(u"进入幼儿考勤-未到 成功")
                    if attendanceCount(driver) != "0":
                        try:
                            absenceList = driver.find_element_by_id("com.tuxing.app.teacher:id/myGridView")\
                                .find_elements_by_class_name("android.widget.RelativeLayout")
                            selectClild = [absenceList[0].find_element_by_id("com.tuxing.app.teacher:id/tv_name").text,
                                           absenceList[1].find_element_by_id("com.tuxing.app.teacher:id/tv_name").text,
                                           absenceList[2].find_element_by_id("com.tuxing.app.teacher:id/tv_name").text]
                            absenceList[0].click()
                            time.sleep(1)
                            screenshot(driver,picFlile+"幼儿考勤选中幼儿1.png")
                            absenceList[0].click()
                            time.sleep(1)
                            screenshot(driver,picFlile+"幼儿考勤取消选中幼儿1.png")
                            absenceList[0].click()
                            time.sleep(1)
                            absenceList[1].click()
                            time.sleep(1)
                            absenceList[2].click()
                            time.sleep(1)
                            screenshot(driver,picFlile+"幼儿考勤选中幼儿1,2,3.png")
                            absenceList[0].click()
                            time.sleep(1)
                            absenceList[1].click()
                            time.sleep(1)
                            absenceList[2].click()
                            time.sleep(1)
                            screenshot(driver,picFlile+"幼儿考勤取消选中幼儿1,2,3.png")
                            time.sleep(1)
                            try:
                                driver.find_element_by_id("com.tuxing.app.teacher:id/btn_leave").click()
                                time.sleep(2)


                            except:
                                print "2"
                        except:
                            logging.info(u"选中/取消选中失败")
                except:
                    logging.info(u"进入幼儿考勤成功")



            except Exception as e:
                print traceback.print_exc()
                print e

            picName_details_back = "wjiayuan_announcement_details_back.png"
            backButton(driver,picFlile,picName_details_back,funcName+"详情_")
            picName_list_back = "wjiayuan_announcement_list_back.png"
            backButton(driver,picFlile,picName_list_back,funcName+"列表_")

        except:
            logging.error(u"进入幼儿考勤失败")
    else:
        try:
            logging.info("进入家园返回值 = "+str(inTagHomeAtion))
        except:
            print traceback.print_exc()
