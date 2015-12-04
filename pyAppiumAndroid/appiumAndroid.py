# -*- coding: utf-8 -*-
import os
from appium import webdriver
from actionTeacher.pubaction import *
from actionTeacher import *

appType = 1
actionTypeList = [1001,1002,2001,2002,2003,2004,2005,2006,2007,8,9,10,11,12,13,14,15,16,17,18,19,20]
#actionTypeList = [2004000]

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'Xiaomi 2014501'

if appType == 1:
    desired_caps['appPackage'] = 'com.tuxing.app.teacher'
elif appType == 2:
    desired_caps['appPackage'] = 'com.tuxing.app.home'
desired_caps['appActivity'] = 'com.tuxing.app.SplashActivity'

desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
#desired_caps['automationName']='Selendroid'

if appType == 1:
    resultPath = r"D:/android_result_pic/teacher/"
elif appType == 2:
    resultPath = r"D:/android_result_pic/home/"

for times in range(1,2):
    checkLogPath = os.path.isdir(resultPath)
    if not checkLogPath:
        os.makedirs(resultPath)
        logPath = resultPath
    else:
        logPath = resultPath
    checkPicPath = os.path.isdir(resultPath+str(times)+"/")
    if not checkPicPath:
        os.makedirs(resultPath+str(times)+"/")
        picFlile = (resultPath+str(times)+"/")
    else:
        picFlile = (resultPath+str(times)+"/")

    LOG_FILENAME = logPath+"testLog.log"
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=LOG_FILENAME,
                        filemode='w')
    try:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        time.sleep(5)
        screenshot(driver,picFlile+"login_main_message.png")
        if appType == 1:
            logging.info(u"打开教师版app")
            time.sleep(2)
            try:
                wxyLoin = driver.find_element_by_name("登 录")
                screenshot(driver,picFlile+"weixueyuan_login.png")
                wxyLoin_userName = driver.find_element_by_id("com.tuxing.app.teacher:id/et_username")
                wxyLoin_userName.send_keys("14100000001")
                time.sleep(1)
                screenshot(driver,picFlile+"weixueyuan_login_username.png")
                driver.find_element_by_id("com.tuxing.app.teacher:id/et_password").send_keys("111111")
                time.sleep(1)
                screenshot(driver,picFlile+"weixueyuan_login_password.png")
                wxyLoin.click()
                logging.info(u"登录成功")
                time.sleep(1)
            except:
                try:
                    driver.find_element_by_name('微学园')
                    logging.info(u"当前为免登陆状态")

                    for actionType in actionTypeList:
                        if actionType == 1001:
                            tag_message_wxy.weixueyuan(driver,picFlile)
                        elif actionType == 1002:
                            tag_message_cloudcardlist.messageCloudCardList(driver,picFlile)
                        while actionType == 2001:
                            tag_home_announcement.tagHomeAnnouncement(driver,picFlile)
                        while actionType == 2002:
                            tag_home_activity.tagHomeActivity(driver,picFlile)
                        while actionType == 2003:
                            tag_home_weeklydiet.tagHomeWeeklydiet(driver,picFlile)
                        while actionType == 2004:
                            tag_home_medicine.tagHomeMedicine(driver,picFlile,appType)
                        while actionType == 2005:
                            tag_home_myattendance.tagHomeMyAttendance(driver,picFlile)
                        while actionType == 2006:
                            tag_home_headmastermail.tagHeadMasterMail(driver,picFlile,appType)
                except:
                    print traceback.print_exc()
                    logging.error(u"登录失败")
        elif appType == 2:
            logging.info(u"打开家长版app")
            time.sleep(2)
    except :
        print traceback.print_exc()
        if appType == 1:
            logging.error(u"打开教师版失败")
        elif appType == 2:
            logging.error(u"打开家长版失败")

    driver.quit()
    time.sleep(5)

