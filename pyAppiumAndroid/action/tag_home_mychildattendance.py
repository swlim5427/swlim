from pubaction import *

def tatMyChildAttendance(actionTypeMessage):
    driver = actionTypeMessage["driver"]
    picFlile = actionTypeMessage["picFlile"]
    homeIconType = int(actionTypeMessage["homeIconType"])
    appType = actionTypeMessage["appType"]
    funcName = "��������_"

    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in ="jiayuan_main_childattendance.png"
        inTagHomeAtion = inTagHome(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        try:
            driver.find_elements_by_id("com.tuxing.app.teacher:id/home_item_icon")[homeIconType].click()
            time.sleep(2)
            screenshot(driver,picFlile+u"��԰_���뱦������.png")
            logging.info(u"���뱦�����ڳɹ�")
            time.sleep(2)
            try:
                driver.find_element_by_id("com.tuxing.app.home:id/prevMonth").click()
                time.sleep(2)
                screenshot(driver,picFlile+u"��������-��һ��.png")
                logging.info(u"��������-����һ�³ɹ�")
                time.sleep(1)
                try:
                    driver.find_element_by_id("com.tuxing.app.home:id/nextMonth").click()
                    time.sleep(2)
                    screenshot(driver,picFlile+u"��������-��һ��.png")
                    logging.info(u"��������-����һ�³ɹ�")
                    time.sleep(1)
                except:
                    logging.info(u"��������-����һ��ʧ��")
            except:
                logging.error(u"��������-����һ��ʧ��")

            try:
                driver.find_element_by_name("ˢ����¼")
                try:
                    checkInList = driver.find_elements_by_id("com.tuxing.app.home:id/home_card_head")
                    checkInListPic = driver.find_elements_by_class_name("android.widget.ImageView")
                    checkInListPic[1].click()
                    path = picFlile+u"��������_ˢ���б�_ͼƬ.png"
                    screenshot(driver,path)
                    logging.info(u"��������_�鿴ˢ����Ƭ�ɹ�")
                    time.sleep(2)
                except:
                    logging.error(u"��������_�鿴ˢ����Ƭʧ��")
                try:
                    driver.find_element_by_id("com.tuxing.app.home:id/wivPhoto").click()
                    path = picFlile+u"��������_����ʿˢ���б�_ͼƬ����.png"
                    screenshot(driver,path)
                    logging.info(u"��������_ˢ����Ƭ���سɹ�")
                    time.sleep(2)
                except:
                    logging.error(u"��������_ˢ����Ƭ����ʧ��")
                try:
                    for j in range(3):
                        driver.swipe(start_x=313,start_y=1163,end_x=313,end_y=209,duration=600)
                        time.sleep(1)
                        path = picFlile+u"��������-ˢ����¼����"+str(j+1)+".png"
                        screenshot(driver,path)
                        logging.info(u"��������-ˢ����¼�����ɹ�"+str(j+1))
                        time.sleep(1)
                    for i in range(3):
                        driver.swipe(start_x=313,start_y=209,end_x=313,end_y=1163,duration=600)
                        time.sleep(1)
                        path = picFlile+u"��������-ˢ����¼����"+str(i+1)+".png"
                        screenshot(driver,path)
                        logging.info(u"��������-ˢ����¼�����ɹ�"+str(i+1))
                        time.sleep(1)

                except:
                    logging.error(u"��������-ˢ����¼�϶�ʧ��")
            except:
                logging.error(u"���뱦������-ˢ����¼ʧ��")

            picName_list_back = u"��������-ˢ���б���.png"
            backButton(driver,picFlile,picName_list_back,funcName+"ˢ���б�_")

            picName_list_back = u"��������-����.png"
            backButton(driver,picFlile,picName_list_back,funcName)
        except:
            logging.error(u"���뱦������ʧ��")