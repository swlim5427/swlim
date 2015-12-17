#coding=utf-8
import sys
import requests
import Message_pb2
import wjy_pb2
import time
import datetime
import threading
import json

#url = "http://123.57.43.111:8080/http_invoke"
url = "http://123.57.150.40:8080/http_invoke"

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
inputMinute = raw_input("minute")
inputSecond = raw_input("second")
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
messageAttach.fileurl = "D:/Camera_20151102160429520.jpg"
messageAttach.attachType = long("1")

fetchAgreementRequest = wjy_pb2.FetchAgreementRequest()

##########Checkin
messageCheckin = wjy_pb2.Checkin()
messageCheckin.id = long("12313131321")
messageCheckin.cardCode = str("10000004")
messageCheckin.attach.fileurl= messageAttach.fileurl
messageCheckin.attach.attachType = messageAttach.attachType
messageCheckin.userId = long("2290987")
messageCheckin.checkinTime = long(nowTime)
messageCheckin.gardenId = long("1026510")

##########CheckinRequest
machineCheckin = wjy_pb2.CheckinRequest()
machineCheckin.machineId = "m00000000000002"

checkIn = machineCheckin.checkin.add()
checkIn.id = messageCheckin.id
checkIn.cardCode = messageCheckin.cardCode
checkIn.attach.fileurl = messageCheckin.attach.fileurl
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
#print(mainMessage)
mainPostMessage = mainMessage.SerializeToString()

postMessage = s.post(url,data=mainPostMessage)
#print postMessage
rMessage = Message_pb2.Response()
#rMessage = wjy_pb2.FetchAgreementResponse()
localprint = postMessage.text.encode('gbk','ignore')
print localprint
#print json.dumps(unicode( localprint , errors='ignore'))
#print rMessage.ParseFromString(postMessage.text)


