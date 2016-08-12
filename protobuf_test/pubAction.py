# -*- coding: utf-8 -*-
#------公共方法----------

import requests
import Message_pb2
import MySQLdb
import datetime
import time
import platform
import wx
import sqlite3
#全局常量
def SysConstants():
    # ip = "192.168.10.210:9022"
    ip = "192.168.10.204:80"
    url = "http://"+ip+"/http_invoke"
    s = requests.session()
    headers ={"Content-type": "application/x-protobuf;charset=utf-8","Connection":"Keep-Alive"}
    connectList = [ip,url,s,headers]
    return connectList
#------------------------------

#pb消息发送和返回
def mainMessageRequest(parameter):

    mainMsg = Message_pb2.Request()
    mainMsg.url=parameter[0]
    mainMsg.version = parameter[1]
    mainMsg.osName = parameter[2]
    mainMsg.body = parameter[3]
    mainMsg.token = str(parameter[6])

    mainPostMsg = mainMsg.SerializeToString()
    postMessage = httpConnect(parameter,mainPostMsg)
    return postMessage

def mainMessageResponse(postMessage):
    try:
        # decode main
        invoke = Message_pb2.Response()
        invoke.ParseFromString(postMessage.content)
        if invoke.statusTxt != "":
            return invoke.statusTxt
        else:
            return invoke
    except:
        invoke.ParseFromString(postMessage.text.encode('utf8','ignore'))
        print invoke.statusTxt.encode('gbk','ignore')
#------------------------------

#http链接
def httpConnect(parameter,mainPostMsg):
    try:
        postMessage = parameter[5].post(parameter[4], data=mainPostMsg)
        return postMessage
    except Exception as e:
        print e
        return "http connect error"
#------------------------------

#mysql链接
def mySQLconnect(sql):
    conn = MySQLdb.connect(host='127.0.0.1',port= 3306,user= 'root',passwd= '111111',db= 'txtest' )
    cur = conn.cursor()
    try:
        sqlResult = cur.execute(sql)
        rList = cur.fetchmany(sqlResult)

        cur.close()
        conn.commit()
        conn.close()
        return rList

    except Exception as e:
        print e
#------------------------------

#sqlite链接
def sqliteConnect(sql):
    conn = sqlite3.connect('pbtest.db')
    try:
        cur = conn.execute(sql);
        conn.commit()
        conn.close()
        return cur
    except Exception as e:
        # print e
        return False
#------------------------------

#当前系统时间
def getTime():

    timeList = []

    inputYear = datetime.datetime.now().year
    inputMonth = datetime.datetime.now().month
    inputDay = datetime.datetime.now().day
    inputHour = datetime.datetime.now().hour
    inputMinute = datetime.datetime.now().minute
    inputSecond = datetime.datetime.now().second

    timeList.extend([inputYear,inputMonth,inputDay,inputHour,inputMinute,inputSecond])
    mTime = datetime.datetime.now().microsecond

    imputDateTime = datetime.datetime(year=int(timeList[0]),month=int(timeList[1]),day=int(timeList[2]),
                                      hour=int(timeList[3]),minute=int(timeList[4]),second=int(timeList[5]))
    formatTime = long(round(time.mktime(imputDateTime.timetuple())))

    rTime =  [long(str(formatTime)+str(mTime/1000)),
              inputYear,inputMonth,inputDay,
              inputHour,inputMinute,inputSecond]

    return rTime
#------------------------------

#系统类型
def systemType():
    if 'Windows' in platform.system():
        return 1
    elif 'Linux' in platform.system():
        return 2

#------------------------------

#WX 弹框
def dialog(self,dialog):
    dlg = wx.MessageDialog(None,dialog,'messge',wx.YES_NO|wx.ICON_QUESTION)
    result = dlg.ShowModal()
#        if (result == wx.ID_YES):
#            self.OnQuit2("yes")
#        elif (result == wx.ID_NO):
#            self.OnQuit2("no")
    dlg.Destroy()