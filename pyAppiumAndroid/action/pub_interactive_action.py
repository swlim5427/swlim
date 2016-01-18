# -*- coding: utf-8 -*-
from appium import webdriver
import os
from pubaction import *

def runAppType(message):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = 'Xiaomi 2014501'

    appType = message["appType"]
    runningTimes = message["runningTimes"]

    if appType == 1:
        desired_caps['appPackage'] = 'com.tuxing.app.teacher'
    elif appType == 2:
        desired_caps['appPackage'] = 'com.tuxing.app.home'

    desired_caps['appActivity'] = 'com.tuxing.app.SplashActivity'

    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    #desired_caps['automationName']='Selendroid'

#    print desired_caps

    if appType == 1:
        resultPath = r"D:/android_result_pic/teacher/"
    elif appType == 2:
        resultPath = r"D:/android_result_pic/home/"

    checkLogPath = os.path.isdir(resultPath)
    if not checkLogPath:
        os.makedirs(resultPath)
        logPath = resultPath
    else:
        logPath = resultPath
    checkPicPath = os.path.isdir(resultPath+str(runningTimes)+"/")
    if not checkPicPath:
        os.makedirs(resultPath+str(runningTimes)+"/")
        picFlile = (resultPath+str(runningTimes)+"/")
    else:
        picFlile = (resultPath+str(runningTimes)+"/")

    LOG_FILENAME = logPath+"testLog.log"
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=LOG_FILENAME,
                        filemode='w')
    if appType == 1:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    elif appType == 2:
        driver = webdriver.Remote('http://127.0.0.1:4923/wd/hub',desired_caps)

    requestMessage = {"driver":driver,"picFlile":picFlile,"picName":"","funcName":""}
  #  print desired_caps
    return requestMessage


def interactive(message):
    interactiveType = message["interactiveType"]
    appType = message["appType"]
    picFlile = message["picFlile"]
    leaveReason = message["leaveReason"]

    if interactiveType == "1":
        if appType == "1":
            driver = message["driver"]
            try:
                picName_in ="jiayuan_main_childattendance_leavelist.png"
                funcName = "幼儿考勤_查看幼儿请假列表"
                inTagHomeAtion = inTagHome(driver,picFlile,picName_in,funcName)
                driver.find_element_by_name("幼儿请假").click()
                time.sleep(1)
                screenshot(driver,picFlile+u"幼儿考勤_幼儿请假.png")
                logging.info(u"幼儿考勤-进入幼儿请假成功")

                if inTagHomeAtion == "1":
                    try:
                        leaveType = driver.find_elements_by_id("com.tuxing.app.teacher:id/leave_record_item_state")
                        leavState = leaveType.text
                        for i in range(0,len(leaveType)):
                            if leavState[i] == "待处理":
                                leaveType[i].click()
                                time.sleep(1)
                                driver.find_element_by_name("待处理")
                                try:
                                    driver.find_element_by_name(leaveReason)
                                except:
                                    logging.info(u"幼儿考勤_幼儿请假理由为空")
                                    leaveReason = ""
                                screenshot(driver,picFlile+u"幼儿考勤_幼儿请假内容详情.png")
                                logging.info(u"幼儿考勤-进入幼儿请假内容详情成功")
                                try:
                                    teacherEdit = driver.find_elements_by_id("com.tuxing.app.teacher:id/leave_record_teacher_edit")
                                    teacherEdit.send_keys(leaveReason+"re")
                                    time.sleep(1)
                                    screenshot(driver,picFlile+u"幼儿考勤_幼儿请假_教师审批成功.png")
                                    logging.info(u"幼儿考勤-幼儿请假-教师审批成功")

                                except:
                                    logging.error(u"幼儿考勤-幼儿请假-教师审批失败")
                                break
                    except:
                        logging.error(u"幼儿考勤-进入幼儿请假内容详情失败")
                return 1
            except:
                logging.error(u"幼儿考勤-进入幼儿请假失败")





'''
 interactiveType:
1、请假
2、园长信箱
3、喂药
4、通知
'''