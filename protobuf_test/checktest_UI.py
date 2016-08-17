# -*- coding: utf-8 -*-

import wjy_pb2
import time
import datetime
import wx
import logging
import pubAction
#
class myFrame (wx.Frame):

    messageApptoken = ""

    def __init__(self,parent,id,title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(450, 350))
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        panelLeft = wx.Panel(self, -1,size = (200,500))
        self.panelRight = wx.Panel(self,-1,size = (500,500))
        self.leftTree = wx.TreeCtrl(panelLeft,1,wx.DefaultPosition,(-1,-1),wx.TR_HAS_BUTTONS|wx.TR_HIDE_ROOT)
        root = self.leftTree.AddRoot('test')
        self.testLogin = self.leftTree.AppendItem(root,u'刷卡')
        self.memberInCome = self.leftTree.AppendItem(root,"")
        self.leftTree.Bind(wx.EVT_TREE_SEL_CHANGED,self.action,id = 1)
        vbox.Add(self.leftTree, 1, wx.EXPAND)
        hbox.Add(panelLeft, 1, wx.EXPAND)
        hbox.Add(self.panelRight, 2, wx.EXPAND)
        panelLeft.SetSizer(vbox)
        self.SetSizer(hbox)
        self.SetMinSize((800, 320))
        self.SetMaxSize((800, 320))


    def action (self,event):
        item = event.GetItem()
        self.messageItem = self.leftTree.GetItemText(item)

        if self.messageItem ==  u"刷卡":
            gGardenName =self.getGardenName()
            if gGardenName == False:
                gardenName = u"没有绑定幼儿园"
            elif gGardenName == "":
                gardenName = u"没有绑定幼儿园"
            else:
                gardenName = self.getGardenName()

            try:
                self.panelRight.DestroyChildren()

                staticIp = wx.StaticText(self.panelRight,-1,"ip:port",(10,43))
                staticTextGardenId = wx.StaticText(self.panelRight,-1,u"幼儿园ID",(10,83))
                staticCustId = wx.StaticText(self.panelRight,-1,u"用户ID",(280,43))
                staticCardCode = wx.StaticText(self.panelRight,-1,u"卡号",(280,83))
                staticDate = wx.StaticText(self.panelRight,-1,u"刷卡日期和时间:",(10,123))
                staticDateYear = wx.StaticText(self.panelRight,-1,u"年",(55,163))
                staticDateMonth = wx.StaticText(self.panelRight,-1,u"月",(125,163))
                staticDateDay = wx.StaticText(self.panelRight,-1,u"日",(195,163))
                staticDateHour = wx.StaticText(self.panelRight,-1,u"时",(265,163))
                staticDateMinute = wx.StaticText(self.panelRight,-1,u"分",(335,163))
                staticDateSecond = wx.StaticText(self.panelRight,-1,u"秒",(405,163))
                staticGardenName = wx.StaticText(self.panelRight,-1,gardenName,(382,218))

                self.messageIp = wx.TextCtrl(self.panelRight,-1,"123.57.150.40:8080",(60,35),size=(200,25))
                self.messageGardenId = wx.TextCtrl(self.panelRight,-1,"1026510",(60,75),size=(200,25))
                self.messageCustId = wx.TextCtrl(self.panelRight,-1,"2291018",(320,35),size=(85,25))
                self.messageCardCode = wx.TextCtrl(self.panelRight,-1,"10000018",(320,75),size=(85,25))
                self.messageDateYear = wx.TextCtrl(self.panelRight,-1,"",(10,155),size=(40,25))
                self.messageDateMonth = wx.TextCtrl(self.panelRight,-1,"",(80,155),size=(40,25))
                self.messageDateDay = wx.TextCtrl(self.panelRight,-1,"",(150,155),size=(40,25))
                self.messageDateHour = wx.TextCtrl(self.panelRight,-1,"",(220,155),size=(40,25))
                self.messageDateMinute = wx.TextCtrl(self.panelRight,-1,"",(290,155),size=(40,25))
                self.messageDateSecond = wx.TextCtrl(self.panelRight,-1,"",(360,155),size=(40,25))
                self.messageResoult = wx.TextCtrl(self.panelRight,-1,u"",(155,219),size=(50,22))

                self.buttonSendMessage = wx.Button(self.panelRight,201,u"确认",(60,218))
                self.buttonSendMessage.Bind(wx.EVT_BUTTON,self.checkIn,self.buttonSendMessage)
                self.buttonFetchCard = wx.Button(self.panelRight,202,u"绑定并同步卡号",(262,218))
                self.buttonFetchCard.Bind(wx.EVT_BUTTON,self.fetchCard,self.buttonFetchCard)

            except Exception as e:
                print(e)
                logging.warning("error when close")

    def checkIn(self,event):

        messageIp = self.messageIp.GetValue()
        messageGardenId = self.messageGardenId.GetValue()
        messageCustId = self.messageCustId.GetValue()
        messageCardCode = self.messageCardCode.GetValue()
        messageDateYear = self.messageDateYear.GetValue()
        messageDateMonth = self.messageDateMonth.GetValue()
        messageDateDay = self.messageDateDay.GetValue()
        messageDateHour = self.messageDateHour.GetValue()
        messageDateMinute = self.messageDateMinute.GetValue()
        messageDateSecond = self.messageDateSecond.GetValue()

        if messageIp == "":
            pubAction.dialog(self,u"没输入IP")
            return
        if messageGardenId == "":
            pubAction.dialog(self,u"没输入幼儿园ID")
            return
        if messageCustId == "":
            pubAction.dialog(self,u"没输入用户ID")
            return
        if messageCardCode == "":
            pubAction.dialog(self,u"没输入卡号")
            return
        if messageDateYear == "" :
            messageDateYear = pubAction.getTime()[1]
        if messageDateMonth == "" :
            messageDateMonth = pubAction.getTime()[2]
        if messageDateDay == "" :
            messageDateDay = pubAction.getTime()[3]
        if messageDateHour == "" :
            messageDateHour = pubAction.getTime()[4]
        if messageDateMinute == "" :
            messageDateMinute = pubAction.getTime()[5]
        if messageDateSecond == "" :
            messageDateSecond = pubAction.getTime()[6]

        mTime = datetime.datetime.now().microsecond
        imputDateTime = datetime.datetime(year=int(messageDateYear),month=int(messageDateMonth),day=int(messageDateDay),
                                          hour=int(messageDateHour),minute=int(messageDateMinute),second=int(messageDateSecond))
        formatTime = long(round(time.mktime(imputDateTime.timetuple())))
        nowTime =  long(str(formatTime)+str(mTime/1000))
        #nowTime = long(round(time.time()*1000))

        reList = []
        countSql = "select count(*) from fetchcard"
        countRes = pubAction.sqliteConnect([countSql,0])
        for checkCout in countRes:
            if checkCout[0] == 0:
                pubAction.dialog(self,u"先同步幼儿园卡号")
                self.messageResoult.SetValue(u"false")
            else:
                sSqlC = "select count(*) from fetchcard where cardcode = \""+messageCardCode+"\""
                sSqlU = "select count(*) from fetchcard where userid = \""+messageCustId+"\""
                sSqlG = "select count(*) from checktable where gardenid = \""+messageGardenId+"\""
                reCheckGardenId = pubAction.sqliteConnect([sSqlG,0])
                reCheckCardCode = pubAction.sqliteConnect([sSqlC,0])
                reCheckUserId = pubAction.sqliteConnect([sSqlU,0])

                for checkGardenId in reCheckGardenId:
                    if checkGardenId[0] == 0:
                        reList.append(checkGardenId[0])
                    else:
                        reList.append(1)
                for checkCardCode in reCheckCardCode:
                    if checkCardCode[0] == 0:
                        reList.append(checkCardCode[0])
                    else:
                        reList.append(1)
                for checkUserId in reCheckUserId:
                    if checkUserId[0] == 0:
                        reList.append(checkUserId[0])
                    else:
                        reList.append(1)
                if reList[0] == 0:
                    pubAction.dialog(self,u"没有同步ID为："+str(messageGardenId)+u" 幼儿园的数据，或幼儿园ID错误")
                    self.messageResoult.SetValue(u"false")
                elif reList[1] == 0:
                    pubAction.dialog(self,u"在ID为："+str(messageGardenId)+u"的幼儿园中找不到卡号为："+str(messageCardCode)+u" 的用户")
                    self.messageResoult.SetValue(u"false")
                elif reList[2] == 0:
                    pubAction.dialog(self,u"在ID为："+str(messageGardenId)+u"的幼儿园中找不到ID为："+str(messageCustId)+u" 的用户")
                    self.messageResoult.SetValue(u"false")
                else:
                    url = "http://"+messageIp+"/http_invoke"
                    s = pubAction.SysConstants()[2]
                    headers =pubAction.SysConstants()[3]
                    s.headers.update(headers)
                    s.get(url)

                    messageAttach = wjy_pb2.Attach()
                    messageAttach.fileurl = "0998c950-93d5-4ad5-8590-518dec6d1f57"
                    messageAttach.attachType = long("1")

                    ##########Checkin
                    messageCheckin = wjy_pb2.Checkin()
                    messageCheckin.id = long("12313131321")
                    messageCheckin.cardCode = str(messageCardCode)
                    #10000004
                    messageCheckin.attach.fileurl= messageAttach.fileurl
                    messageCheckin.attach.attachType = messageAttach.attachType
                    messageCheckin.userId = long(messageCustId)
                    #2290987
                    messageCheckin.checkinTime = long(nowTime)
                    messageCheckin.gardenId = long(messageGardenId)

                    ##########CheckinRequest
                    machineCheckin = wjy_pb2.CheckinRequest()
                    machineCheckin.machineId = "test001test0001"

                    checkIn = machineCheckin.checkin.add()
                    checkIn.id = messageCheckin.id
                    checkIn.cardCode = messageCheckin.cardCode
                    checkIn.attach.fileurl = messageCheckin.attach.fileurl
                    checkIn.userId = messageCheckin.userId
                    checkIn.attach.attachType = messageCheckin.attach.attachType
                    checkIn.checkinTime = messageCheckin.checkinTime
                    checkIn.gardenId = messageCheckin.gardenId
                    #print machineCheckin

                    ##########MessageRequest
                    bodyMessageString = machineCheckin.SerializeToString()

                    postMessage = pubAction.mainMessageRequest(["/checkin","","",bodyMessageString,url,s,""])
                    invoke = pubAction.mainMessageResponse(postMessage)

                    if postMessage.status_code == 200:
                        self.messageResoult.SetValue(u"success")
                        sSqlUname = "select username from fetchcard where userid = "+"\""+messageCustId+"\""
                        sUserName = pubAction.sqliteConnect([sSqlUname,0])
                        for userName in sUserName:
                            if userName[0] != "":
                                pubAction.dialog(self,u"用户ID："+str(messageCustId)+u"，用户名："+userName[0]+u",签到成功")
                            else:
                                pubAction.dialog(self,u"用户ID："+str(messageCustId)+u"，用户名："+userName[0]+u",签到失败")
                    else:
                        self.messageResoult.SetValue(u"error:"+str(postMessage.status_code))
        pubAction.sqliteConnect(["",2])

    def chackMoreAction(self,checkParemeter):

        messageFetchCardRequest = wjy_pb2.FetchCardRequest()

        gardenId = self.messageGardenId.GetValue()
        messageFetchCardRequest.gardenId = long(gardenId)
        messageFetchCardRequest.lastModifiedSince = checkParemeter[0]
        bodyMessageString = messageFetchCardRequest.SerializeToString()

        postMessage = pubAction.mainMessageRequest(["/fetch_card","","",bodyMessageString,checkParemeter[1],checkParemeter[2],""])
        invoke = pubAction.mainMessageResponse(postMessage)
        invoke.ParseFromString(postMessage.content)
        fetchCardRes = wjy_pb2.FetchCardResponse()
        fetchCardRes.ParseFromString(invoke.body)
        # print fetchCardRes
        return [fetchCardRes.fetchTime,fetchCardRes.card,fetchCardRes.hasMore]

    def fetchCard(self,event):

        gardenId = self.messageGardenId.GetValue()
        if gardenId == "":
            pubAction.dialog(self,u"没输入幼儿园ID")
            return

        messageIp = self.messageIp.GetValue()
        if messageIp == "":
            pubAction.dialog(self,u"没输入IP")
            return

        url = "http://"+messageIp+"/http_invoke"
        s = pubAction.SysConstants()[2]
        headers =pubAction.SysConstants()[3]
        s.headers.update(headers)
        s.get(url)

        getGardenName = self.registerCheckinMachine(gardenId)[0]


        wx.StaticText(self.panelRight,-1,getGardenName,(382,218))
        usql = "update checktable SET gardenid = "+"\""+gardenId+"\",gardenname ="+"\""+getGardenName+"\""

        pubAction.sqliteConnect([usql,1])

        checkParemeter = [0,url,s]
        moreCheck = self.chackMoreAction(checkParemeter)
        count = 0
        dsql = "delete from fetchcard"
        pubAction.sqliteConnect([dsql,1])

        while moreCheck[2]:
            self.exSql(moreCheck,0)
            count = len(moreCheck[1])+count
            checkParemeter = [moreCheck[0],url,s]
            moreCheck = self.chackMoreAction(checkParemeter)

        else:
            self.exSql(moreCheck,1)
            count = len(moreCheck[1])+count
            pubAction.dialog(self,u"幼儿园："+getGardenName+u"，同步完成，总计"+str(count)+u"个卡号")

    def exSql(self,moreCheck,c):

        for i in range(0,len(moreCheck[1])):
            try:
                isql ="insert into fetchcard VALUES ("+str(moreCheck[1][i].id)+","+str(moreCheck[1][i].userId)+","+str(moreCheck[1][i].parentUserId)+\
                      ",\""+moreCheck[1][i].cardCode+"\",\""+moreCheck[1][i].userName+"\",\""+moreCheck[1][i].parentName+\
                      "\",\""+str(moreCheck[1][i].actionType)+"\",\""+str(moreCheck[1][i].usertype)+"\",\""+moreCheck[1][i].positionName+\
                      "\",\""+moreCheck[1][i].departmentName+"\",\""+moreCheck[1][i].userNameUnison+"\")"
            except Exception as e:
                print e
            pubAction.sqliteConnect([isql,c])

    def getGardenName(self):

        sql = "select count(gardenname) from checktable"
        rsql = pubAction.sqliteConnect([sql,0])
        if rsql !=False:
            for gCount in rsql:
                if gCount[0] == 0:
                    gardenName = ""
                else:
                    sgSql = "select gardenname from checktable"
                    resSgSql = pubAction.sqliteConnect([sgSql,0])
                    for reGardenName in resSgSql:
                        # print reGardenName[0]
                        gardenName = reGardenName[0]
        elif not rsql:
            initSql = pubAction.checkSql()
            for sql in initSql:
                pubAction.sqliteConnect([sql,1])
                gardenName = ""
        pubAction.sqliteConnect(["",2])
        return gardenName

    def registerCheckinMachine(self,gardenId):

        messageIp = self.messageIp.GetValue()
        if messageIp == "":
            self.dialog(u"没输入IP")
            return
        # wx.StaticText(self.panelRight,-1,u"同步中……",(382,218))
        messageegisterMachine = wjy_pb2.RegisterCheckinMachineRequest()

        messageegisterMachine.gardenId = long(gardenId)
        messageegisterMachine.machineId = "test001test0001"
        messageegisterMachine.macAddress = "1122334455667788"
        bodyMessageString = messageegisterMachine.SerializeToString()

        url = "http://"+messageIp+"/http_invoke"
        s = pubAction.SysConstants()[2]
        headers =pubAction.SysConstants()[3]
        s.headers.update(headers)
        s.get(url)

        postMessage = pubAction.mainMessageRequest(["/register_checkin_machine","","",bodyMessageString,url,s,""])
        invoke = pubAction.mainMessageResponse(postMessage)
        invoke.ParseFromString(postMessage.content)
        registerCheckinMachineRes = wjy_pb2.RegisterCheckinMachineResponse()
        registerCheckinMachineRes.ParseFromString(invoke.body)

        return [registerCheckinMachineRes.gardenName,gardenId]
#------------------------------

class myApp(wx.App):
    def OnInit(self):
        frame = myFrame(None,-1,'test')
        frame.Show(True)
        self.SetTopWindow(frame)
        frame.Center()
        return True
app = myApp()
app.MainLoop()