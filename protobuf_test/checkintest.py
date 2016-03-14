#coding=utf-8
import sys
import os
import MySQLdb
import threading
import time
import datetime
import requests
import wjy_pb2
import Message_pb2

testCount = 1

ip = "123.57.150.40:8080"  #service ip
url = "http://123.57.43.111:8080/http_invoke" # pb url

sshUrl = "ssh -L 3306:tuxingdb.mysql.rds.aliyuncs.com:3306 -tt root@123.57.43.111"
dbName = "wjy_test"
dbUrl = "tuxingdb.mysql.rds.aliyuncs.com"
sql = '''SELECT card_code,garden_id FROM tx_user_card
WHERE id >=(SELECT FLOOR(RAND() * (SELECT MAX(id) FROM tx_user_card))) AND card_code>1 ORDER BY id LIMIT 1000;
'''
host = 'tuxingdb.mysql.rds.aliyuncs.com'
host = '127.0.0.1'

class checkintest():
    def checkMysqlPort(self):
        findPort = os.popen("netstat -nao|findstr 3306")
        findPortR = findPort.read()
        retList = findPortR.split(' ')
        processPid = retList[len(retList)-1]
        return processPid

    def mysqlAction(self):
        time.sleep(1)
        conn = MySQLdb.connect(host=host, user='tuxingadmin', passwd='Tx2010_Tuxing', db=dbName, port=3306)
        cur = conn.cursor()
        sqlResult = cur.execute(sql)
        rList = cur.fetchmany(sqlResult)
        conn.close()

    def ssh(self):
        os.system(sshUrl)

    def threadingAction(self,type):
        threads = []
        if type == "ssh":
            sshT = threading.Thread(target=self.ssh)
            sshMySqlT = threading.Thread(target=self.mysqlAction)
            threads.append(sshT)
            threads.append(sshMySqlT)
            for i in range(len(threads)):
                threads[i].start()
                threads[i].join(timeout = 2)

    def checkCruTest(self):
        print  ">1"

    def checkSigTest(self):
        print "1"

class checkIn():
    def checkIn(self,testCount):
        s = requests.session()
        headers ={"Content-type": "application/x-protobuf;charset=utf-8","Connection":"Keep-Alive"}
        s.headers.update(headers)
        s.get(url)

        if testCount == 1:
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
        elif testCount > 1:
            inputYear = datetime.datetime.now().year
            inputMonth = datetime.datetime.now().month
            inputDay = datetime.datetime.now().day
            inputHour = datetime.datetime.now().hour
            inputMinute = datetime.datetime.now().minute
            inputSecond = datetime.datetime.now().second

        mTime = datetime.datetime.now().microsecond
        imputDateTime = datetime.datetime(year=int(inputYear),month=int(inputMonth),day=int(inputDay),
                                          hour=int(inputHour),minute=int(inputMinute),second=int(inputSecond))
        formatTime = long(round(time.mktime(imputDateTime.timetuple())))
        nowTime =  long(str(formatTime)+str(mTime/1000))

        print nowTime

        messageAttach = wjy_pb2.Attach()
        messageAttach.fileurl = "b8a36af2-b151-4a62-8b44-839b3bfd4f4c"
        messageAttach.attachType = long("1")

        ##########Checkin
        messageCheckin = wjy_pb2.Checkin()
        messageCheckin.id = long("12313131321")
        messageCheckin.cardCode = str("10000035")
        messageCheckin.attach.fileurl= messageAttach.fileurl
        messageCheckin.attach.attachType = messageAttach.attachType
        messageCheckin.userId = long("2293831")
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

        ##########MessageRequest
        bodyMessageString = machineCheckin.SerializeToString()

        mainMessage = Message_pb2.Request()
        mainMessage.url="/checkin"
        mainMessage.body = bodyMessageString
        print(mainMessage)
        mainPostMessage = mainMessage.SerializeToString()

        postMessage = s.post(url,data=mainPostMessage)
        print postMessage

if __name__ == '__main__':
    if testCount > 1:
        checkintest = checkintest()
        if  checkintest.checkMysqlPort() != "":
            os.system("taskkill /F /pid "+str(checkintest.checkMysqlPort()))
            checkintest.threadingAction("ssh")
        else:
            checkintest.threadingAction("ssh")
    else:
        checkInSigTest = checkIn()
        checkInSigTest.checkIn(1)
