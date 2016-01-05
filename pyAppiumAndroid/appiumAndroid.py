# -*- coding: utf-8 -*-

from actionTeacher.pubaction import *
from actionTeacher import *

appType = 1
actionTypeList = [1001,1002,2001,2002,2003,2004,2005,2006,2007,8,9,10,11,12,13,14,15,16,17,18,19,20]
#actionTypeList = [2000007]

for times in range(1,2):

    message = {"appType":appType,"runningTimes":times}

    try:
        requestMessage = pub_interactive_action.runAppType(message)
        driver = requestMessage["driver"]
        picFlile = requestMessage["picFlile"]

        def actionType():
            for actionType in actionTypeList:
                if actionType == 1001:
                    tag_message_wxy.weixueyuan(actionTypeMessageCode(actionType,driver,picFlile,appType))
                elif actionType == 1002:
                    tag_message_cloudcardlist.messageCloudCardList(actionTypeMessageCode(actionType,driver,picFlile,appType))
                elif actionType == 2001:
                    tag_home_announcement.tagHomeAnnouncement(actionTypeMessageCode(actionType,driver,picFlile,appType))
                elif actionType == 2002:
                    tag_home_activity.tagHomeActivity(actionTypeMessageCode(actionType,driver,picFlile,appType))
                elif actionType == 2003:
                    tag_home_weeklydiet.tagHomeWeeklydiet(actionTypeMessageCode(actionType,driver,picFlile,appType))
                elif actionType == 2004:
                    tag_home_childattendance.tagHomeChlidAttendance(actionTypeMessageCode(actionType,driver,picFlile,appType))
                elif actionType == 2005:
                    tag_home_myattendance.tagHomeMyAttendance(actionTypeMessageCode(actionType,driver,picFlile,appType))
                elif actionType == 2007:
                    tag_home_medicine.tagHomeMedicine(actionTypeMessageCode(actionType,driver,picFlile,appType))
                elif actionType == 2009:
                    tag_home_headmastermail.tagHeadMasterMail(actionTypeMessageCode(actionType,driver,picFlile,appType))



        time.sleep(5)
        screenshot(driver,picFlile+"login_main_message.png")
        if appType == 1:
            logging.info(u"打开教师版app")
            time.sleep(2)
            try:
                wxyLoin = driver.find_element_by_name("登 录")
                screenshot(driver,picFlile+u"登录.png")
                wxyLoin_userName = driver.find_element_by_id("com.tuxing.app.teacher:id/et_username")
                wxyLoin_userName.send_keys("14100000001")
                time.sleep(1)
                screenshot(driver,picFlile+u"登录_用户名.png")
                driver.find_element_by_id("com.tuxing.app.teacher:id/et_password").send_keys("111111")
                time.sleep(1)
                screenshot(driver,picFlile+u"登录_密码.png")
                wxyLoin.click()
                logging.info(u"登录成功")
                time.sleep(1)
                actionType()
            except:
                try:
                    driver.find_element_by_name('微学园')
                    logging.info(u"当前为免登陆状态")
                    time.sleep(2)
                    '''
                    appType2 = 2
                    message2 = {"appType":appType2,"runningTimes":times}
                    homeDriver = pub_interactive_action.runAppType(message2)["driver"]
                    time.sleep(5)
                    homeDriver.quit()
                    '''
                    actionType()
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

    try:
        driver.quit()
    except Exception as e:
        print "driver quit is :"+ str(e)
    time.sleep(5)


# 1001：消息-微学园，tag_message_wxy；
# 1002：消息-云卫士刷卡，tag_message_cloudcardlist
# 1003：
# 2001：家园-公告，tag_home_announcenment
# 2002：家园-活动，tag_home_activity
# 2003：家园-食谱，tag_home_weklydiet
# 2004：家园-幼儿考勤，tag_home_chlidattendance
# 2005：家园-我的考勤，tag_home_myattendance
# 2006：家园-通知，tag_home_notice
# 2007：家园-喂药，tag_home_medicine
# 2009: 家园-园长信箱，tag_home_headmastermail

# actionTypeMessage = {"driver":driver,"picFlile":picFlile,"homeIconType":[0,1,2,3,4,5,6,7,8,9],"appType":[0,1]}
# actionTypeMessage   0:公告，1：活动，2：食谱，3：幼儿考勤，4：我的考勤，5：语音播报,6:通知，7：喂药，8：通讯录，9：园长信箱