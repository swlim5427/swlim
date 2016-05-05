#coding=utf-8
import sys
import requests
import Message_pb2
import wjy_pb2
import time
import datetime
import MySQLdb
import wx
import threading
import logging

##
# class myFrame (wx.Frame):
#
#     messageApptoken = ""
#     def __init__(self,parent,id,title):
#         wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(450, 350))
#         hbox = wx.BoxSizer(wx.HORIZONTAL)
#         vbox = wx.BoxSizer(wx.VERTICAL)
#         panelLeft = wx.Panel(self, -1,size = (200,500))
#         self.panelRight = wx.Panel(self,-1,size = (500,500))
#         self.leftTree = wx.TreeCtrl(panelLeft,1,wx.DefaultPosition,(-1,-1),wx.TR_HAS_BUTTONS|wx.TR_HIDE_ROOT)
#         root = self.leftTree.AddRoot('test')
#         self.testLogin = self.leftTree.AppendItem(root,u'刷卡')
#         self.memberInCome = self.leftTree.AppendItem(root,"")
#         self.leftTree.Bind(wx.EVT_TREE_SEL_CHANGED,self.action,id = 1)
#         vbox.Add(self.leftTree, 1, wx.EXPAND)
#         hbox.Add(panelLeft, 1, wx.EXPAND)
#         hbox.Add(self.panelRight, 2, wx.EXPAND)
#         panelLeft.SetSizer(vbox)
#         self.SetSizer(hbox)
#         self.SetMinSize((800, 320))
#         self.SetMaxSize((800, 320))
#
#     def dialog(self,dialog):
#         dlg = wx.MessageDialog(None,dialog,'messge',wx.YES_NO|wx.ICON_QUESTION)
#         result = dlg.ShowModal()
# #        if (result == wx.ID_YES):
# #            self.OnQuit2("yes")
# #        elif (result == wx.ID_NO):
# #            self.OnQuit2("no")
#         dlg.Destroy()
#
#     def action (self,event):
#         item = event.GetItem()
#         self.messageItem = self.leftTree.GetItemText(item)
# #        print self.messageItem
#         if self.messageItem ==  u"刷卡":
#             try:
#                 self.panelRight.DestroyChildren()
#
#                 staticIp = wx.StaticText(self.panelRight,-1,"ip:port",(10,43))
#                 staticTextGardenId = wx.StaticText(self.panelRight,-1,u"幼儿园ID",(10,83))
#                 staticCustId = wx.StaticText(self.panelRight,-1,u"用户ID",(280,43))
#                 staticCardCode = wx.StaticText(self.panelRight,-1,u"卡号",(280,83))
#                 staticDate = wx.StaticText(self.panelRight,-1,u"刷卡日期和时间:",(10,123))
#                 staticDateYear = wx.StaticText(self.panelRight,-1,u"年",(55,163))
#                 staticDateMonth = wx.StaticText(self.panelRight,-1,u"月",(125,163))
#                 staticDateDay = wx.StaticText(self.panelRight,-1,u"日",(195,163))
#                 staticDateHour = wx.StaticText(self.panelRight,-1,u"时",(265,163))
#                 staticDateMinute = wx.StaticText(self.panelRight,-1,u"分",(335,163))
#                 staticDateSecond = wx.StaticText(self.panelRight,-1,u"秒",(405,163))
#
#                 self.messageIp = wx.TextCtrl(self.panelRight,-1,"123.57.150.40:8080",(60,35),size=(200,25))
#                 self.messageGardenId = wx.TextCtrl(self.panelRight,-1,"1026510",(60,75),size=(200,25))
#                 self.messageCustId = wx.TextCtrl(self.panelRight,-1,"",(320,35),size=(85,25))
#                 self.messageCardCode = wx.TextCtrl(self.panelRight,-1,"",(320,75),size=(85,25))
#                 self.messageDateYear = wx.TextCtrl(self.panelRight,-1,"",(10,155),size=(40,25))
#                 self.messageDateMonth = wx.TextCtrl(self.panelRight,-1,"",(80,155),size=(40,25))
#                 self.messageDateDay = wx.TextCtrl(self.panelRight,-1,"",(150,155),size=(40,25))
#                 self.messageDateHour = wx.TextCtrl(self.panelRight,-1,"",(220,155),size=(40,25))
#                 self.messageDateMinute = wx.TextCtrl(self.panelRight,-1,"",(290,155),size=(40,25))
#                 self.messageDateSecond = wx.TextCtrl(self.panelRight,-1,"",(360,155),size=(40,25))
#
#                 self.buttonSendMessage = wx.Button(self.panelRight,201,u"确认",(60,218))
#                 self.buttonSendMessage.Bind(wx.EVT_BUTTON,self.checkIn,self.buttonSendMessage)
#                 # self.buttonlogin.Bind(wx.EVT_BUTTON,self.login,self.buttonlogin)
#                 # self.buttonLoginRun.Bind(wx.EVT_BUTTON,self.loginAction,self.buttonLoginRun)
#             except Exception as e:
#                 print(e)
#                 logging.warning("error when close")
#
#     def checkIn(self,event):
#         messageIp = self.messageIp.GetValue()
#         messageGardenId = self.messageGardenId.GetValue()
#         messageCustId = self.messageCustId.GetValue()
#         messageCardCode = self.messageCardCode.GetValue()
#         messageDateYear = self.messageDateYear.GetValue()
#         messageDateMonth = self.messageDateMonth.GetValue()
#         messageDateDay = self.messageDateDay.GetValue()
#         messageDateHour = self.messageDateHour.GetValue()
#         messageDateMinute = self.messageDateMinute.GetValue()
#         messageDateSecond = self.messageDateSecond.GetValue()
#
#         if messageIp == "":
#             self.dialog(u"没输入IP")
#             return
#         if messageGardenId == "":
#             self.dialog(u"没输入幼儿园ID")
#             return
#         if messageCustId == "":
#             self.dialog(u"没输入用户ID")
#             return
#         if messageCardCode == "":
#             self.dialog(u"没输入卡号")
#             return
#         if messageDateYear == "" :
#             messageDateYear = datetime.datetime.now().year
#         if messageDateMonth == "" :
#             messageDateMonth = datetime.datetime.now().month
#         if messageDateDay == "" :
#             messageDateDay = datetime.datetime.now().day
#         if messageDateHour == "" :
#             messageDateHour = datetime.datetime.now().hour
#         if messageDateMinute == "" :
#             messageDateMinute = datetime.datetime.now().minute
#         if messageDateSecond == "" :
#             messageDateSecond = datetime.datetime.now().second
#
#         mTime = datetime.datetime.now().microsecond
#         imputDateTime = datetime.datetime(year=int(messageDateYear),month=int(messageDateMonth),day=int(messageDateDay),
#                                           hour=int(messageDateHour),minute=int(messageDateMinute),second=int(messageDateSecond))
#         formatTime = long(round(time.mktime(imputDateTime.timetuple())))
#         nowTime =  long(str(formatTime)+str(mTime/1000))
#         #nowTime = long(round(time.time()*1000))
#
#         url = "http://"+messageIp+"/http_invoke"
# #        print(url)
#         s = requests.session()
#         headers ={"Content-type": "application/x-protobuf;charset=utf-8","Connection":"Keep-Alive"}
#         s.headers.update(headers)
#         s.get(url)
#
#         ##########AttachType
#         #messageAttachType = wjy_pb2.AttachType()
#         ##########Attach
#         messageAttach = wjy_pb2.Attach()
#         messageAttach.fileurl = "D:/Camera_20151102160429520.jpg"
#         messageAttach.attachType = long("1")
#
#         fetchAgreementRequest = wjy_pb2.FetchAgreementRequest()
#
#         ##########Checkin
#         messageCheckin = wjy_pb2.Checkin()
#         messageCheckin.id = long("12313131321")
#         messageCheckin.cardCode = str(messageCardCode)
#         #10000004
#         messageCheckin.attach.fileurl= messageAttach.fileurl
#         messageCheckin.attach.attachType = messageAttach.attachType
#         messageCheckin.userId = long(messageCustId)
#         #2290987
#         messageCheckin.checkinTime = long(nowTime)
#         messageCheckin.gardenId = long(messageGardenId)
#
#         ##########CheckinRequest
#         machineCheckin = wjy_pb2.CheckinRequest()
#         machineCheckin.machineId = "m00000000000002"
#
#         checkIn = machineCheckin.checkin.add()
#         checkIn.id = messageCheckin.id
#         checkIn.cardCode = messageCheckin.cardCode
#         checkIn.attach.fileurl = messageCheckin.attach.fileurl
#         checkIn.attach.attachType = messageCheckin.attach.attachType
#         checkIn.userId = messageCheckin.userId
#         checkIn.checkinTime = messageCheckin.checkinTime
#         checkIn.gardenId = messageCheckin.gardenId
#         #print machineCheckin
#
#         ##########MessageRequest
#         bodyMessageString = machineCheckin.SerializeToString()
#         #bodyMessageString = fetchAgreementRequest.SerializeToString()
#
#         mainMessage = Message_pb2.Request()
#         mainMessage.url="/checkin"
#         #mainMessage.url="/fetch_postgroup"
#         mainMessage.body = bodyMessageString
#         #print(mainMessage)
#         mainPostMessage = mainMessage.SerializeToString()
#
#         postMessage = s.post(url,data=mainPostMessage)
#         #print postMessage
#         rMessage = Message_pb2.Response()
#         #rMessage = wjy_pb2.FetchAgreementResponse()
#         localprint = postMessage.text.encode('gbk','ignore')
# #        print localprint
#
#
# class myApp(wx.App):
#     def OnInit(self):
#         frame = myFrame(None,-1,'test')
#         frame.Show(True)
#         self.SetTopWindow(frame)
#         frame.Center()
#         return True
# app = myApp()
# app.MainLoop()
#




# ip = "101.200.139.197:80"
ip = "192.168.10.202:8080"
#ip = "123.57.150.40:8080"
#url = "http://123.57.43.111:8080/http_invoke"
url = "http://"+ip+"/http_invoke"
dbName = "wjy_test"
dbUrl = "tuxingdb.mysql.rds.aliyuncs.com"

s = requests.session()
headers ={"Content-type": "application/x-protobuf;charset=utf-8","Connection":"Keep-Alive"}
s.headers.update(headers)
s.get(url)
#print s.get(url)
# checkin

inputYear = raw_input("year(enter default):")
inputMonth = raw_input("month:")
inputDay = raw_input("day:")
inputHour = raw_input("hour:")
inputMinute = raw_input("minute:")
inputSecond = raw_input("second:")
if inputYear == "" :
    inputYear = datetime.datetime.now().year
if inputMonth == "" :
    inputMonth = datetime.datetime.now().month
if inputDay == "" :
    inputDay = datetime.datetime.now().day
if inputHour == "" :
    inputHour = datetime.datetime.now().hour
if inputMinute == "" :
    inputMinute = datetime.datetime.now().minute
if inputSecond == "" :
    inputSecond = datetime.datetime.now().second

mTime = datetime.datetime.now().microsecond
imputDateTime = datetime.datetime(year=int(inputYear),month=int(inputMonth),day=int(inputDay),
                                  hour=int(inputHour),minute=int(inputMinute),second=int(inputSecond))
formatTime = long(round(time.mktime(imputDateTime.timetuple())))
nowTime =  long(str(formatTime)+str(mTime/1000))
#nowTime = long(round(time.time()*1000))
print nowTime
##########AttachType
#messageAttachType = wjy_pb2.AttachType()
##########Attach
messageAttach = wjy_pb2.Attach()
# messageAttach.fileurl = "D:/Camera_20151102160429520.jpg"
messageAttach.fileurl = "b8a36af2-b151-4a62-8b44-839b3bfd4f4c"
messageAttach.attachType = long("1")

fetchAgreementRequest = wjy_pb2.FetchAgreementRequest()

##########Checkin
messageCheckin = wjy_pb2.Checkin()
messageCheckin.id = long("12313131321")
messageCheckin.cardCode = str("08217736")
#10000004
messageCheckin.attach.fileurl= messageAttach.fileurl
messageCheckin.attach.attachType = messageAttach.attachType
messageCheckin.userId = long("2294767")
#2290987
messageCheckin.checkinTime = long(nowTime)
messageCheckin.gardenId = long("1027094")

##########CheckinRequest
machineCheckin = wjy_pb2.CheckinRequest()
machineCheckin.machineId = "m00000000000002"

checkIn = machineCheckin.checkin.add()
checkIn.id = messageCheckin.id
checkIn.cardCode = messageCheckin.cardCode
checkIn.attach.fileurl = messageCheckin\
    .attach.fileurl
checkIn.attach.attachType = messageCheckin.attach.attachType
checkIn.userId = messageCheckin.userId
checkIn.checkinTime = messageCheckin.checkinTime
checkIn.gardenId = messageCheckin.gardenId
#print machineCheckin

##########MessageRequest
bodyMessageString = machineCheckin.SerializeToString()
#bodyMessageString = fetchAgreementRequest.SerializeToString()

mainMessage = Message_pb2.Request()
mainMessage.url="/checkin"
#mainMessage.url="/fetch_postgroup"
mainMessage.body = bodyMessageString
print(mainMessage)
mainPostMessage = mainMessage.SerializeToString()

postMessage = s.post(url,data=mainPostMessage)
print postMessage
rMessage = Message_pb2.Response()
print "asdfasdf"+str(rMessage)
#rMessage = wjy_pb2.FetchAgreementResponse()
localprint = postMessage.text.encode('gbk','ignore')
print localprint
#print json.dumps(unicode( localprint , errors='ignore'))
#print rMessage.ParseFromString(postMessage.text)