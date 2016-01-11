# -*- coding: utf-8 -*-
from pubaction import *

def tagDiscoveryQzq(driver,picFlile):
    funcName = "发现_"
    if checkTag(driver) == "discovery":
        inTagDiscoveryAtion = 1
    else:
        picName_in =u"家园_主页_活动.png"
        inTagDiscoveryAtion = inTagDiscovery(driver,picFlile,picName_in,funcName)
    if inTagDiscoveryAtion == 1:
        try:
            driver.find_element_by_name('亲子圈').click()
            time.sleep(2)
            path = picFlile+u"发现_亲子圈列表.png"
            screenshot(driver,path)
            logging.info(u"进入发现-亲子圈成功")
            time.sleep(1)
            try:
                driver.find_element_by_id("com.tuxing.app.teacher:id/ll_portrait").click()
                time.sleep(2)
                path = picFlile+u"发现_亲子圈_教师头像进入.png"
                screenshot(driver,path)
                logging.info(u"进入发现-亲子圈教师头像进入成功")
                try:
                    driver.find_element_by_id("com.tuxing.app.teacher:id/ll_right").click()
                    time.sleep(1)
                    path = picFlile+u"发现_亲子圈_教师头像_消息列表.png"
                    screenshot(driver,path)
                    logging.info(u"进入发现-亲子圈_教师头像-进入消息列表成功")

                    try:
                        driver.find_elements_by_id("com.tuxing.app.teacher:id/ll_unread_layout")[0].click()
                        time.sleep(1)
                        screenshot(driver,path)
                        logging.info(u"进入发现-亲子圈_教师头像-消息列表选择消息成功")
                        time.sleep(1)

                        try:
                            driver.find_elements_by_id("com.tuxing.app.teacher:id/feed_icon")[0].click()
                            time.sleep(1)
                            screenshot(driver,path)
                            logging.info(u"进入发现-亲子圈_教师头像-列表-消息详情-选择'赞'头像")
                            picName_list_back = u"发现_亲子圈_教师头像-列表-'赞'头像用户_返回.png"
                            backButton(driver,picFlile,picName_list_back,"发现_亲子圈_教师头像-'赞'头像用户_")
                        except:
                            logging.info(u"进入发现-亲子圈_教师头像-消息详情-没有赞")

                        try:
                            driver.find_elements_by_id("com.tuxing.app.teacher:id/comment_user_icon")[0].click()
                            time.sleep(1)
                            screenshot(driver,path)
                            logging.info(u"进入发现-亲子圈_教师头像-消息列表-消息详情-选择'评论'头像")
                            picName_list_back = u"发现_亲子圈_教师头像-列表-'评论'头像用户_返回.png"
                            backButton(driver,picFlile,picName_list_back,"发现_亲子圈_教师头像-'评论'头像用户_")
                        except:
                            logging.info(u"进入发现-亲子圈_教师头像-列表-消息详情-没有评论")

                        picName_list_back = u"发现_亲子圈_教师头像-消息列表详情_返回.png"
                        backButton(driver,picFlile,picName_list_back,"发现-亲子圈_教师头像-消息列表详情_")
                        picName_list_back = u"发现_亲子圈_教师头像-消息列表_返回.png"
                        backButton(driver,picFlile,picName_list_back,"发现-亲子圈_教师头像-消息列表_")

                    except:
                        try:
                            driver.find_elements_by_id("com.tuxing.app.teacher:id/tv_time")
                        except:
                            logging.error(u"进入发现-亲子圈_教师头像-消息列表为空")

                            picName_list_back = u"发现_亲子圈_教师头像-消息列表_返回.png"
                            backButton(driver,picFlile,picName_list_back,"发现-亲子圈_教师头像-消息列表_")

                        logging.error(u"进入发现-亲子圈_教师头像-消息列表选择消息失败")
                except:
                    logging.error(u"进入发现-亲子圈_教师头像-进入消息列表失败  ")

                try:
                    driver.find_elements_by_id("com.tuxing.app.teacher:id/tv_content")[0].click()
                    time.sleep(1)
                    screenshot(driver,path)
                    logging.info(u"进入发现-亲子圈-教师头像-消息详情成功")

                except:
                    try:
                        driver.find_elements_by_id("com.tuxing.app.teacher:id/tv_content_1")[0].click()
                        time.sleep(1)
                        screenshot(driver,path)
                        logging.info(u"进入发现-亲子圈-教师头像-消息详情成功")

                        try:
                            driver.find_elements_by_id("com.tuxing.app.teacher:id/feed_icon")[0].click()
                            time.sleep(1)
                            screenshot(driver,path)
                            logging.info(u"进入发现-亲子圈_教师头像-消息详情-选择'赞'头像")
                            picName_list_back = u"发现_亲子圈_教师头像- '赞'头像用户_返回.png"
                            backButton(driver,picFlile,picName_list_back,"发现_亲子圈_教师头像-'赞'头像用户_")
                        except:
                            logging.info(u"进入发现-亲子圈_教师头像-消息详情-没有赞")
                        try:
                            driver.find_elements_by_id("com.tuxing.app.teacher:id/comment_user_icon")[0].click()
                            time.sleep(1)
                            screenshot(driver,path)
                            logging.info(u"进入发现-亲子圈_教师头像-消息详情-选择'评论'头像")
                            picName_list_back = u"发现_亲子圈_教师头像-'评论'头像用户_返回.png"
                            backButton(driver,picFlile,picName_list_back,"发现-亲子圈_教师头像-'评论'头像用户_")
                        except:
                            logging.info(u"进入发现-亲子圈_教师头像-消息详情-没有评论")
                    except:
                        logging.info(u"进入发现-亲子圈_教师头像-消息详情失败")

                    picName_list_back = u"发现_亲子圈_教师头像-消息详情_返回.png"
                    backButton(driver,picFlile,picName_list_back,"发现-亲子圈_教师头像-消息详情_")

                picName_list_back = u"发现_亲子圈_教师头像-返回.png"
                backButton(driver,picFlile,picName_list_back,"发现-亲子圈_教师头像_")
                time.sleep(1)

            except:
                logging.error(u"进入发现-亲子圈_教师头像进入失败")

            try:
                driver.find_element_by_id("com.tuxing.app.teacher:id/rl_my_list").click()
                time.sleep(1)
                screenshot(driver,path)
                logging.info(u"进入发现-亲子圈-与我相关成功")

                try:
                    driver.find_elements_by_id("com.tuxing.app.teacher:id/ll_unread_layout")[0].click()
                    time.sleep(1)
                    screenshot(driver,path)
                    logging.info(u"进入发现-亲子圈-与我相关-消息详情成功")

                    try:
                        driver.find_elements_by_id("com.tuxing.app.teacher:id/feed_icon")[0].click()
                        time.sleep(1)
                        screenshot(driver,path)
                        logging.info(u"进入发现-亲子圈_与我相关-消息详情-选择'赞'头像")
                        picName_list_back = u"发现_亲子圈_与我相关- '赞'头像用户_返回.png"
                        backButton(driver,picFlile,picName_list_back,"发现_亲子圈_教师头像-'赞'头像用户_")
                    except:
                        logging.info(u"进入发现-亲子圈_与我相关-消息详情-没有赞")
                    try:
                        driver.find_elements_by_id("com.tuxing.app.teacher:id/comment_user_icon")[0].click()
                        time.sleep(1)
                        screenshot(driver,path)
                        logging.info(u"进入发现-亲子圈_与我相关-消息详情-选择'评论'头像")
                        picName_list_back = u"发现_亲子圈_与我相关-'评论'头像用户_返回.png"
                        backButton(driver,picFlile,picName_list_back,"发现-亲子圈_教师头像-'评论'头像用户_")
                    except:
                        logging.info(u"进入发现-亲子圈_与我相关-消息详情-没有评论")
                except:
                    logging.error(u"进入发现-亲子圈_与我相关-消息详情失败")

                picName_list_back = u"发现_亲子圈_与我相关-消息详情_返回.png"
                backButton(driver,picFlile,picName_list_back,"发现-亲子圈-与我相关-消息详情_")
                picName_list_back = u"发现_亲子圈_与我相关-消息列表-返回.png"
                backButton(driver,picFlile,picName_list_back,"发现-亲子圈-与我相关-消息详情列表")

            except:
                logging.error(u"进入发现-亲子圈-与我相关失败")

            try:
                driver.find_element_by_id("com.tuxing.app.teacher:id/rl_class_pictures").click()
                time.sleep(1)
                screenshot(driver,path)
                logging.info(u"进入发现-亲子圈-进入班级相册成功")
                try:
                    for i in range(3):
                        driver.swipe(start_x=313,start_y=209,end_x=313,end_y=1163,duration=600)
                        time.sleep(1)
                        path = picFlile+u"亲子圈-班级相册成-内容上拉"+str(i+1)+".png"
                        screenshot(driver,path)
                        logging.info(u"上拉成功"+str(i+1))
                        time.sleep(1)
                    for j in range(3):
                        driver.swipe(start_x=313,start_y=1163,end_x=313,end_y=209,duration=600)
                        time.sleep(1)
                        path = picFlile+u"亲子圈-班级相册成-内容下拉"+str(j+1)+".png"
                        screenshot(driver,path)
                        logging.info(u"下拉成功"+str(j+1))
                        time.sleep(1)
                except:
                    logging.error(u"详情拖动失败")

                try:
                    driver.find_elements_by_id("com.tuxing.app.teacher:id/iv")[2].click()
                    time.sleep(1)
                    screenshot(driver,path)
                    logging.info(u"亲子圈-班级相册-打开图片成功")
                    try:
                        driver.find_element_by_id("com.tuxing.app.teacher:id/wivPhoto").click()
                        time.sleep(1)
                        screenshot(driver,path)
                        logging.info(u"亲子圈-班级相册-图片返回成功")
                    except:
                        logging.info(u"亲子圈-班级相册-图片返回失败")
                except:
                    logging.error(u"亲子圈-班级相册-打开图片失败")

                try:
                    driver.find_element_by_id("com.tuxing.app.teacher:id/tv_title").click()
                    time.sleep(1)
                    screenshot(driver,path)
                    logging.info(u"亲子圈-班级相册-打开班级列表成功")
                    try:
                        driver.find_elements_by_id("com.tuxing.app.teacher:id/title_tv")[1].click()
                        time.sleep(1)
                        screenshot(driver,path)
                        logging.error(u"亲子圈-班级相册-切换班级成功")
                    except:
                        logging.error(u"亲子圈-班级相册-切换班级失败或只有一个班级")
                except:
                    logging.error(u"亲子圈-班级相册-打开班级列表失败")
            except:
                logging.error(u"进入发现-亲子圈-进入班级相册失败")

            picName_list_back = u"发现_亲子圈_班级相册_返回.png"
            backButton(driver,picFlile,picName_list_back,"发现-亲子圈-班级相册_")

            try:
                driver.find_element_by_id("com.tuxing.app.teacher:id/tv_title").click()
                time.sleep(1)
                screenshot(driver,path)
                logging.info(u"亲子圈-打开班级列表成功")
                try:
                    driver.find_elements_by_id("com.tuxing.app.teacher:id/title_tv")[2].click()
                    time.sleep(1)
                    screenshot(driver,path)
                    logging.error(u"亲子圈-切换班级成功")
                except:
                    logging.error(u"亲子圈-切换班级失败或只有一个班级")
            except:
                logging.error(u"亲子圈-打开班级列表失败")

        except:
            logging.error(u"进入发现-亲子圈失败")