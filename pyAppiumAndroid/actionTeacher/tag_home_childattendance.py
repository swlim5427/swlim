# -*- coding: utf-8 -*-
from pubaction import *

childNum = 3
selectClild = []

def tagHomeChlidAttendance(driver,picFlile):
    funcName = "幼儿考勤_"
    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in ="jiayuan_main_childattendance.png"
        inTagHomeAtion = inTagHome(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        try:
            driver.find_element_by_name(u"幼儿考勤").click()
            time.sleep(2)
            screenshot(driver,picFlile+u"家园_进入幼儿考勤.png")
            logging.info(u"进入幼儿考勤成功")
            time.sleep(2)
#            persentNumEnter = 0
#            absenceNumEnter = 0
#            leaveNumEnter = 0
#            persentNumChange = 0
#            absenceNumChange = 0
#            leaveNumChange = 0
            try:
                presentEnter = driver.find_element_by_id("com.tuxing.app.teacher:id/tv_tab_1")
                presentEnter.click()
                time.sleep(1)
                persentNumEnter = getNumber(presentEnter.text)
                screenshot(driver,picFlile+u"幼儿考勤_已到列表初始.png")

                absenceEnter = driver.find_element_by_id("com.tuxing.app.teacher:id/tv_tab_2")
                absenceEnter.click()
                time.sleep(1)
                absenceNumEnter = getNumber(absenceEnter.text)
                screenshot(driver,picFlile+u"幼儿考勤_缺勤列表初始.png")

                leaveEnter = driver.find_element_by_id("com.tuxing.app.teacher:id/tv_tab_3")
                leaveEnter.click()
                time.sleep(1)
                leaveNumEnter = getNumber(leaveEnter.text)
                screenshot(driver,picFlile+u"幼儿考勤_请假列表初始.png")

                try:
                    absenceEnter.click()
                    time.sleep(1)
                    screenshot(driver,picFlile+"jiayuan_childattendance_absence.png")
                    time.sleep(1)
                    logging.info(u"进入幼儿考勤-未到 成功")
                    if absenceNumEnter != "0":
                        try:
                            absenceList = driver.find_element_by_id("com.tuxing.app.teacher:id/myGridView")\
                                .find_elements_by_class_name("android.widget.RelativeLayout")
                            for i in  range(childNum):
                                selectClild.append(absenceList[i].find_element_by_id("com.tuxing.app.teacher:id/tv_name").text)
                            print selectClild

                            absenceList[0].click()
                            time.sleep(1)
                            screenshot(driver,picFlile+u"幼儿考勤_选中幼儿1.png")
                            absenceList[0].click()
                            time.sleep(1)
                            screenshot(driver,picFlile+u"幼儿考勤_取消选中幼儿1.png")

                            for i in range(len(selectClild)):
                                absenceList[i+i].click()
                                time.sleep(1)
                            screenshot(driver,picFlile+u"幼儿考勤_选中幼儿1,2,3.png")
                            for i in range(len(selectClild)):
                                absenceList[i+i].click()
                                time.sleep(1)
                            screenshot(driver,picFlile+u"幼儿考勤_取消选中幼儿1,2,3.png")
                            time.sleep(1)
                            try:
                                for i in range(len(selectClild)):
                                    absenceList[i+i].click()
                                    time.sleep(1)
                                driver.find_element_by_id("com.tuxing.app.teacher:id/btn_patch").click()
                                time.sleep(2)

                                absenceEnter = driver.find_element_by_id("com.tuxing.app.teacher:id/tv_tab_2")
                                absenceNumChange = getNumber(absenceEnter.text)

                                print(absenceNumEnter),"@@",(absenceNumChange)

                                if int(absenceNumChange)-int(absenceNumEnter) == len(selectClild):
                                    try:
                                        presentEnter.click()
                                        time.sleep(1)
                                        persentNumChange = getNumber(presentEnter.text)
                                        if int(persentNumChange)-int(persentNumEnter) == len(selectClild):
                                            try:
                                                screenshot(driver,picFlile+u"幼儿考勤_补签后已到列表.png")
                                                time.sleep(1)
                                            except:
                                                logging.info(u"幼儿考勤_补签后进入已到列表失败")
                                        else:
                                            logging.info(u"幼儿考勤_补签后已到幼儿数量错误")
                                    except Exception as e:
                                        logging.error(e)
                                else:
                                    logging.info(u"幼儿考勤_补签幼儿与实际选择数量不符")
                            except:
                                logging.info(u"幼儿考勤_补签失败")

                            try:
                                presentEnter.click()
                                persentNumEnter = getNumber(presentEnter.text)
                                for i in range(len(selectClild)):
                                    absenceList[i+i].click()
                                    time.sleep(1)
                                driver.find_element_by_id("com.tuxing.app.teacher:id/btn_leave").click()
                                time.sleep(2)
                                absenceEnter = driver.find_element_by_id("com.tuxing.app.teacher:id/tv_tab_2")
                                absenceNumChange = getNumber(absenceEnter.text)

                                if int(absenceNumChange)-int(absenceNumEnter) == len(selectClild):
                                    try:
                                        leaveEnter.click()
                                        time.sleep(1)
                                        leaveNumChange = getNumber(leaveEnter.text)
                                        if int(leaveNumChange)-int(leaveNumEnter) == len(selectClild):
                                            try:
                                                screenshot(driver,picFlile+u"幼儿考勤_补签后已到列表.png")
                                                time.sleep(1)
                                            except:
                                                logging.info(u"幼儿考勤_请假后进入请假列表失败")
                                        else:
                                            logging.info(u"幼儿考勤_请假后已到幼儿数量错误")
                                    except Exception as e:
                                        logging.error(e)
                                else:
                                    logging.info(u"幼儿考勤_请假幼儿与实际选择数量不符")
                            except:
                                logging.info(u"幼儿考勤_请假失败")

                        except:
                            logging.info(u"幼儿考勤_选中/取消选中失败")
                    else:
                        logging.info(u"没有未出勤记录")
                except:
                    logging.info(u"幼儿考勤_进入幼儿考勤成功")

            except Exception as e:
                print traceback.print_exc()
                print e

            picName_details_back = u"微家园_幼儿考勤返回.png"
            backButton(driver,picFlile,picName_details_back,funcName)

        except:
            logging.error(u"进入幼儿考勤失败")
    else:
        try:
            logging.info(u"进入家园返回值 = "+str(inTagHomeAtion))
        except:
            print traceback.print_exc()
