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


        sql = "select * from checktable"
        res = pubAction.sqliteConnect(sql)
        if not res:
            for sql in open("testSql.txt"):
                pubAction.sqliteConnect(sql)

        if self.messageItem ==  u"刷卡":
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

                self.messageIp = wx.TextCtrl(self.panelRight,-1,"192.168.10.204",(60,35),size=(200,25))
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
                self.buttonFetchCard = wx.Button(self.panelRight,202,u"同步卡号",(262,218))
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
            self.dialog(u"没输入IP")
            return
        if messageGardenId == "":
            self.dialog(u"没输入幼儿园ID")
            return
        if messageCustId == "":
            self.dialog(u"没输入用户ID")
            return
        if messageCardCode == "":
            self.dialog(u"没输入卡号")
            return
        if messageDateYear == "" :
            messageDateYear = pubAction.getTime()[1]
        if messageDateMonth == "" :
            messageDateYear = pubAction.getTime()[2]
        if messageDateDay == "" :
            messageDateYear = pubAction.getTime()[3]
        if messageDateHour == "" :
            messageDateYear = pubAction.getTime()[4]
        if messageDateMinute == "" :
            messageDateYear = pubAction.getTime()[5]
        if messageDateSecond == "" :
            messageDateYear = pubAction.getTime()[6]

        mTime = datetime.datetime.now().microsecond
        imputDateTime = datetime.datetime(year=int(messageDateYear),month=int(messageDateMonth),day=int(messageDateDay),
                                          hour=int(messageDateHour),minute=int(messageDateMinute),second=int(messageDateSecond))
        formatTime = long(round(time.mktime(imputDateTime.timetuple())))
        nowTime =  long(str(formatTime)+str(mTime/1000))
        #nowTime = long(round(time.time()*1000))

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
        machineCheckin.machineId = "m00000000000002"

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
        else:
            self.messageResoult.SetValue(u"error:"+str(postMessage.status_code))

    def chackMoreAction(self,checkParemeter):

        messageFetchCardRequest = wjy_pb2.FetchCardRequest()

        gardenId = self.messageGardenId.GetValue()
        messageFetchCardRequest.gardenId = long(gardenId)
        messageFetchCardRequest.lastModifiedSince = checkParemeter[0]
        bodyMessageString = messageFetchCardRequest.SerializeToString()

        postMessage = pubAction.mainMessageRequest(["/fetch_card","","",bodyMessageString,checkParemeter[1],checkParemeter[2],""])
        # postMessage = pubAction.mainMessageRequest(["/checkin","","",checkParemeter[0],checkParemeter[1],checkParemeter[2],""])
        invoke = pubAction.mainMessageResponse(postMessage)
        invoke.ParseFromString(postMessage.content)
        fetchCardRes = wjy_pb2.FetchCardResponse()
        fetchCardRes.ParseFromString(invoke.body)


        return [fetchCardRes.fetchTime,fetchCardRes.card,fetchCardRes.hasMore]

    def fetchCard(self,event):

        messageIp = self.messageIp.GetValue()
        url = "http://"+messageIp+"/http_invoke"
        s = pubAction.SysConstants()[2]
        headers =pubAction.SysConstants()[3]
        s.headers.update(headers)
        s.get(url)

        checkParemeter = [0,url,s]
        moreCheck = self.chackMoreAction(checkParemeter)
        count = 0

        while moreCheck[2]:
            print moreCheck[2],"----",moreCheck[1][0].positionName
            count = len(moreCheck[1])+count
            checkParemeter = [moreCheck[0],url,s]
            moreCheck = self.chackMoreAction(checkParemeter)
            if moreCheck[2] == False:
                count = len(moreCheck[1])+count
                print moreCheck[2],"----",moreCheck[1][0].positionName
                # break-
        print count,"---------------",len(moreCheck[1])

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