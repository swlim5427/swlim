# -*- coding: utf-8 -*-

from pubaction import *

def weixueyuan(driver,picFlile):
    funcName = "微学园_"
    if checkTag(driver) == "message":
        inTagMessageAtion = 1
    else:
        picName_in =u"消息_进入微学园.png"
        inTagMessageAtion = inTagMessage(driver,picFlile,picName_in,funcName)

    if inTagMessageAtion == 1:
        try:
            wxy = driver.find_element_by_name('微学园')
            wxy.click()
            time.sleep(2)
            screenshot(driver,picFlile+u"消息_微学园列表.png")
            logging.info(u"进入微学园列表")
            time.sleep(2)

            try:
                for i in range(1):
                    driver.swipe(start_x=313,start_y=209,end_x=313,end_y=1163,duration=600)
                    time.sleep(1)
                    path = picFlile+u"消息_微学园列表上翻"+str(i+1)+".png"
                    screenshot(driver,path)
                    logging.info(u"微学园列表上翻:"+str(i+1))
                    time.sleep(1)
                for j in range(1):
                    driver.swipe(start_x=313,start_y=1163,end_x=313,end_y=209,duration=600)
                    time.sleep(1)
                    path = picFlile+u"消息_微学园列表下翻"+str(j+1)+".png"
                    screenshot(driver,path)
                    logging.info(u"微学园列表下翻:"+str(j+1))
                    time.sleep(1)
            except:
                logging.error(u"微学园列表翻页失败")
            try:
                time.sleep(1)
                wxyList = driver.find_element_by_id("com.tuxing.app.teacher:id/lyceum_top_pic")
                wxyList.click()
                #       positions = []
                #       positions.append((361,806))
                #       driver.tap(positions)
                time.sleep(1)
                path = picFlile+u"消息_微学园内容详情.png"
                screenshot(driver,path)
                logging.info(u"进入微学园内容详情")
                time.sleep(1)
            except:
                logging.error(u"微学园内容详情进入失败")
            try:
                for j in range(2):
                    driver.swipe(start_x=313,start_y=1163,end_x=313,end_y=209,duration=600)
                    time.sleep(1)
                    path = picFlile+u"消息_微学园内容详情下拉"+str(j+1)+".png"
                    screenshot(driver,path)
                    logging.info(u"详情下拉成功"+str(j+1))
                    time.sleep(1)
                for i in range(2):
                    driver.swipe(start_x=313,start_y=209,end_x=313,end_y=1163,duration=600)
                    time.sleep(1)
                    path = picFlile+u"消息_微学园内容详情上拉"+str(i+1)+".png"
                    screenshot(driver,path)
                    logging.info(u"详情上拉成功"+str(i+1))
                    time.sleep(1)
            except:
                logging.error(u"详情拖动失败")

            picName_details_back = u"消息_微学园内容详情_返回.png"
            backButton(driver,picFlile,picName_details_back,funcName+"详情_")

            picName_list_back = u"消息_微学园列表_返回.png"
            backButton(driver,picFlile,picName_list_back,funcName+"列表_")

        except:
            logging.error(u"微学园列表进入失败")
    else:
        try:
            logging.info("进入消息返回值 = "+str(inTagMessageAtion))
        except:
            print traceback.print_exc()