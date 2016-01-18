from pubaction import *

def tatMyChildAttendance(actionTypeMessage):
    driver = actionTypeMessage["driver"]
    picFlile = actionTypeMessage["picFlile"]
    homeIconType = int(actionTypeMessage["homeIconType"])
    appType = actionTypeMessage["appType"]
    funcName = "±¦±¦¿¼ÇÚ_"

    if checkTag(driver) == "home":
        inTagHomeAtion = 1
    else:
        picName_in ="jiayuan_main_childattendance.png"
        inTagHomeAtion = inTagHome(driver,picFlile,picName_in,funcName)

    if inTagHomeAtion == 1:
        try:
            driver.find_elements_by_id("com.tuxing.app.teacher:id/home_item_icon")[homeIconType].click()
            time.sleep(2)
            screenshot(driver,picFlile+u"¼ÒÔ°_½øÈë±¦±¦¿¼ÇÚ.png")
            logging.info(u"½øÈë±¦±¦¿¼ÇÚ³É¹¦")
            time.sleep(2)
            try:
                driver.find_element_by_id("com.tuxing.app.home:id/prevMonth").click()
                time.sleep(2)
                screenshot(driver,picFlile+u"±¦±¦¿¼ÇÚ-ÉÏÒ»ÔÂ.png")
                logging.info(u"±¦±¦¿¼ÇÚ-·­ÉÏÒ»ÔÂ³É¹¦")
                time.sleep(1)
                try:
                    driver.find_element_by_id("com.tuxing.app.home:id/nextMonth").click()
                    time.sleep(2)
                    screenshot(driver,picFlile+u"±¦±¦¿¼ÇÚ-ÏÂÒ»ÔÂ.png")
                    logging.info(u"±¦±¦¿¼ÇÚ-·­ÏÂÒ»ÔÂ³É¹¦")
                    time.sleep(1)
                except:
                    logging.info(u"±¦±¦¿¼ÇÚ-·­ÏÂÒ»ÔÂÊ§°Ü")
            except:
                logging.error(u"±¦±¦¿¼ÇÚ-·­ÉÏÒ»ÔÂÊ§°Ü")

            try:
                driver.find_element_by_name("Ë¢¿¨¼ÇÂ¼")
                try:
                    checkInList = driver.find_elements_by_id("com.tuxing.app.home:id/home_card_head")
                    checkInListPic = driver.find_elements_by_class_name("android.widget.ImageView")
                    checkInListPic[1].click()
                    path = picFlile+u"±¦±¦¿¼ÇÚ_Ë¢¿¨ÁÐ±í_Í¼Æ¬.png"
                    screenshot(driver,path)
                    logging.info(u"±¦±¦¿¼ÇÚ_²é¿´Ë¢¿¨ÕÕÆ¬³É¹¦")
                    time.sleep(2)
                except:
                    logging.error(u"±¦±¦¿¼ÇÚ_²é¿´Ë¢¿¨ÕÕÆ¬Ê§°Ü")
                try:
                    driver.find_element_by_id("com.tuxing.app.home:id/wivPhoto").click()
                    path = picFlile+u"±¦±¦¿¼ÇÚ_ÔÆÎÀÊ¿Ë¢¿¨ÁÐ±í_Í¼Æ¬·µ»Ø.png"
                    screenshot(driver,path)
                    logging.info(u"±¦±¦¿¼ÇÚ_Ë¢¿¨ÕÕÆ¬·µ»Ø³É¹¦")
                    time.sleep(2)
                except:
                    logging.error(u"±¦±¦¿¼ÇÚ_Ë¢¿¨ÕÕÆ¬·µ»ØÊ§°Ü")
                try:
                    for j in range(3):
                        driver.swipe(start_x=313,start_y=1163,end_x=313,end_y=209,duration=600)
                        time.sleep(1)
                        path = picFlile+u"±¦±¦¿¼ÇÚ-Ë¢¿¨¼ÇÂ¼ÏÂÀ­"+str(j+1)+".png"
                        screenshot(driver,path)
                        logging.info(u"±¦±¦¿¼ÇÚ-Ë¢¿¨¼ÇÂ¼ÏÂÀ­³É¹¦"+str(j+1))
                        time.sleep(1)
                    for i in range(3):
                        driver.swipe(start_x=313,start_y=209,end_x=313,end_y=1163,duration=600)
                        time.sleep(1)
                        path = picFlile+u"±¦±¦¿¼ÇÚ-Ë¢¿¨¼ÇÂ¼ÉÏÀ­"+str(i+1)+".png"
                        screenshot(driver,path)
                        logging.info(u"±¦±¦¿¼ÇÚ-Ë¢¿¨¼ÇÂ¼ÉÏÀ­³É¹¦"+str(i+1))
                        time.sleep(1)

                except:
                    logging.error(u"±¦±¦¿¼ÇÚ-Ë¢¿¨¼ÇÂ¼ÍÏ¶¯Ê§°Ü")
            except:
                logging.error(u"½øÈë±¦±¦¿¼ÇÚ-Ë¢¿¨¼ÇÂ¼Ê§°Ü")

            picName_list_back = u"±¦±¦¿¼ÇÚ-Ë¢¿¨ÁÐ±í·µ»Ø.png"
            backButton(driver,picFlile,picName_list_back,funcName+"Ë¢¿¨ÁÐ±í_")

            picName_list_back = u"±¦±¦¿¼ÇÚ-·µ»Ø.png"
            backButton(driver,picFlile,picName_list_back,funcName)
        except:
            logging.error(u"½øÈë±¦±¦¿¼ÇÚÊ§°Ü")