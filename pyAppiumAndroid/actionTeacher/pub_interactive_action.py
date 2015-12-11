from appium import webdriver
import os
import time
from pubaction import *

class pubInteractiveAction:

    def runAppType(interactiveType,appType,inType):
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

        if interactiveType == "1":
            if appType == "1":
                driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
                try:
                    driver.find_element_by_name("�׶����").click()
                    time.sleep(1)
                    screenshot(driver,picFlile+u"�׶�����_�׶����.png")
                    logging.info(u"�׶�����-�����׶���ٳɹ�")

                except:
                    logging.info(u"�׶�����-�����׶����ʧ��")





'''
 interactiveTyep:
1�����
2��԰������
3��ιҩ
4��֪ͨ
'''