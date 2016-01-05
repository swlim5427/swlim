# -*- coding: utf-8 -*-
from pubaction import *

childNum = 1
selectClild = []

def tagHomeChlidAttendance(actionTypeMessage):
    driver = actionTypeMessage["driver"]
    picFlile = actionTypeMessage["picFlile"]
    homeIconType = int(actionTypeMessage["homeIconType"])
    appType = actionTypeMessage["appType"]
    funcName = "幼儿考勤_"

    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in ="jiayuan_main_childattendance.png"
        inTagHomeAtion = inTagHome(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        try:
            driver.find_elements_by_id("com.tuxing.app.teacher:id/home_item_icon")[homeIconType].click()
            time.sleep(2)
            screenshot(driver,picFlile+u"家园_进入幼儿考勤.png")
            logging.info(u"进入幼儿考勤成功")
            time.sleep(2)

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

                logging.info(u"幼儿考勤_已到-未到-请假标签切换成功")
                try:
                    absenceEnter.click()
                    time.sleep(1)
#                    screenshot(driver,picFlile+"jiayuan_childattendance_absence.png")
                    time.sleep(1)
                    if absenceNumEnter != "0":
                        try:
                            absenceList = driver.find_element_by_id("com.tuxing.app.teacher:id/myGridView")\
                                .find_elements_by_class_name("android.widget.RelativeLayout")
                            for i in  range(childNum):
                                selectClild.append(absenceList[i].find_element_by_id("com.tuxing.app.teacher:id/tv_name").text)

                            absenceList[0].click()
                            time.sleep(1)
                            screenshot(driver,picFlile+u"幼儿考勤_选中幼儿1.png")
                            absenceList[0].click()
                            time.sleep(1)
                            screenshot(driver,picFlile+u"幼儿考勤_取消选中幼儿1.png")

                            for i in range(len(selectClild)):
                                absenceList[i+i].click()
                                time.sleep(1)
                            screenshot(driver,picFlile+u"幼儿考勤_批量选中幼儿数量"+str(len(selectClild))+".png")
                            for i in range(len(selectClild)):
                                absenceList[i+i].click()
                                time.sleep(1)
                            screenshot(driver,picFlile+u"幼儿考勤_批量取消选中幼儿数量"+str(len(selectClild))+".png")
                            time.sleep(1)
                            logging.info(u"幼儿考勤_选中/取消选中成功")
                            try:
                                for i in range(len(selectClild)):
                                    absenceList[i+i].click()
                                    time.sleep(1)
                                driver.find_element_by_id("com.tuxing.app.teacher:id/btn_patch").click()
                                time.sleep(2)

                                absenceEnter = driver.find_element_by_id("com.tuxing.app.teacher:id/tv_tab_2")
                                absenceNumChange = getNumber(absenceEnter.text)

                                if int(absenceNumEnter)-int(absenceNumChange) == len(selectClild):
                                    try:
                                        presentEnter.click()
                                        time.sleep(1)
                                        persentNumChange = getNumber(presentEnter.text)
                                        if int(persentNumChange)-int(persentNumEnter) == int(len(selectClild)):
                                            logging.info(u"幼儿考勤_补签后已到幼儿数量正确")
                                            try:
                                                screenshot(driver,picFlile+u"幼儿考勤_补签后已到列表.png")
                                                time.sleep(1)
                                                logging.info(u"幼儿考勤_补签成功")
                                            except:
                                                logging.info(u"幼儿考勤_补签后进入已到列表失败")
                                        else:
                                            logging.error(u"幼儿考勤_补签后已到幼儿数量错误")
                                    except Exception as e:
                                        logging.error(e)
                                else:
                                    logging.error(u"幼儿考勤_补签幼儿与实际选择数量不符")
                            except:
                                logging.error(u"幼儿考勤_补签失败")

                            try:
                                absenceEnter.click()
                                absenceNumEnter = getNumber(absenceEnter.text)
                                for i in range(len(selectClild)):
                                    absenceList[i+i].click()
                                    time.sleep(1)
                                driver.find_element_by_id("com.tuxing.app.teacher:id/btn_leave").click()
                                time.sleep(2)
                                absenceEnter = driver.find_element_by_id("com.tuxing.app.teacher:id/tv_tab_2")
                                absenceNumChange = getNumber(absenceEnter.text)

                                if int(absenceNumEnter)-int(absenceNumChange) == int(len(selectClild)):
                                    try:
                                        leaveEnter.click()
                                        time.sleep(1)
                                        leaveNumChange = getNumber(leaveEnter.text)
                                        if int(leaveNumChange)-int(leaveNumEnter) == len(selectClild):
                                            logging.info(u"幼儿考勤_请假后已到幼儿数量正确")
                                            try:
                                                screenshot(driver,picFlile+u"幼儿考勤_请假后请假列表.png")
                                                time.sleep(1)
                                                logging.info(u"幼儿考勤_请假后进入已到列表成功")
                                            except:
                                                logging.error(u"幼儿考勤_请假后进入请假列表失败")
                                        else:
                                            logging.error(u"幼儿考勤_请假后已到幼儿数量错误")
                                    except Exception as e:
                                        logging.error(e)
                                else:
                                    logging.error(u"幼儿考勤_请假幼儿与实际选择数量不符")
                            except:
                                logging.error(u"幼儿考勤_请假失败")

                        except:
                            logging.error(u"幼儿考勤_选中/取消选中失败")
                    else:
                        logging.info(u"没有未出勤记录")
                except Exception as e:
                    print traceback.print_exc()
                    print e

            except Exception as e:
                logging.error(u"幼儿考勤_已到-未到-请假标签切换成功")
                print traceback.print_exc()
                print e

            try:
                driver.find_element_by_id("com.tuxing.app.teacher:id/left").click()
                time.sleep(1)
                screenshot(driver,picFlile+u"幼儿考勤_左翻页.png")
                logging.info(u"幼儿考勤-左翻页成功")
                time.sleep(1)

                try:
                    driver.find_element_by_id("com.tuxing.app.teacher:id/right").click()
                    time.sleep(1)
                    screenshot(driver,picFlile+u"幼儿考勤_右翻页.png")
                    logging.info(u"幼儿考勤-右翻页成功")
                    time.sleep(1)
                except:
                    logging.error(u"幼儿考勤-右翻页失败")
            except:
                logging.error(u"幼儿考勤-翻页失败")

            try:
                classListButton = driver.find_element_by_id("com.tuxing.app.teacher:id/tv_title")
                classListButton.click()
                time.sleep(1)
                try:
                    classList = driver.find_elements_by_id("com.tuxing.app.teacher:id/content")
                    if len(classList) > 0:
                        screenshot(driver,picFlile+u"幼儿考勤_班级列表.png")
                        logging.info(u"幼儿考勤-打开班级列表成功")
                        try:
                            classList[1].click()
                            time.sleep(1)
                            screenshot(driver,picFlile+u"幼儿考勤_班级列表_选择班级"+
                                       str(classList[1].find_element_by_id("com.tuxing.app.teacher:id/title_tv").text)+".png")
                            logging.info(u"幼儿考勤-班级列表-选择班级成功")
                        except:
                            logging.info(u"幼儿考勤_班级列表_选择班级失败")
                    else:
                        logging.info(u"此教师名下只有一个班级")

                except Exception as e:
                    logging.info(u"此教师名下只有一个班级")
                    print traceback.print_exc()
                    print e
            except:
                logging.error(u"幼儿考勤-打开班级列表失败")

            try:
                dateList = driver.find_elements_by_class_name("android.widget.NumberPicker")
                dateListYear = dateList[0].find_elements_by_class_name("android.widget.Button")
                dateListMonth = dateList[1].find_elements_by_class_name("android.widget.Button")
                dateListDate = dateList[2].find_elements_by_class_name("android.widget.Button")

                dateListYear[0].click()
                time.sleep(1)
                screenshot(driver,picFlile+u"幼儿考勤_选择上一年.png")
                logging.info(u"选择上一年")
                dateListYear[1].click()
                time.sleep(1)
                screenshot(driver,picFlile+u"幼儿考勤_选择下一年.png")
                logging.info(u"选择下一年")

                dateListMonth[0].click()
                time.sleep(1)
                screenshot(driver,picFlile+u"幼儿考勤_选择上一月.png")
                logging.info(u"选择上一年")
                dateListMonth[1].click()
                time.sleep(1)
                screenshot(driver,picFlile+u"幼儿考勤_选择下一月.png")
                logging.info(u"选择下一年")

                dateListDate[0].click()
                time.sleep(1)
                screenshot(driver,picFlile+u"幼儿考勤_选择上一日.png")
                logging.info(u"选择上一年")
                dateListDate[1].click()
                time.sleep(1)
                screenshot(driver,picFlile+u"幼儿考勤_选择下一日.png")
                logging.info(u"选择下一年")

            except:
                logging.error(u"幼儿考勤-修改日期失败")

            picName_details_back = u"微家园_幼儿考勤返回.png"
            backButton(driver,picFlile,picName_details_back,funcName)

        except:
            logging.error(u"进入幼儿考勤失败")
    else:
        try:
            logging.info(u"进入家园返回值 = "+str(inTagHomeAtion))
        except:
            print traceback.print_exc()
