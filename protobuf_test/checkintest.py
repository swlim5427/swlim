#coding=utf-8

import os
import MySQLdb
import threading
import time
import datetime
import requests
import wjy_pb2
import Message_pb2
import csv
import eventlet

# conTimes = 2
# checkInCount = 2
conTimes = raw_input("loop time:")
checkInCount = raw_input("count:")

#ip = "123.57.150.40:8080"  #service ip
ip = "123.56.200.12:8080"  #service ip
url = "http://"+ip+"/http_invoke" # pb url

# sshUrl = "ssh -L 3306:tuxingdb.mysql.rds.aliyuncs.com:3306 -tt root@123.57.43.111"
# #dbName = "wjy_test"
# dbName = "wjy"
# dbUrl = "rds0brggy02in39oo153o.mysql.rds.aliyuncs.com"
# #dbUrl = "rdsmzybjb2izzmjo.mysql.rds.aliyuncs.com"
# sql = "SELECT card_code,garden_id,user_id FROM tx_user_card WHERE garden_id = 1029881 and id >=(" \
#       "SELECT FLOOR(RAND() * (SELECT MAX(id) FROM tx_user_card))) AND card_code>1 ORDER BY id LIMIT "+str(checkInCount);
# #host = 'tuxingdb.mysql.rds.aliyuncs.com'
# host = 'rds0brggy02in39oo153o.mysql.rds.aliyuncs.com'

s = requests.session()
headers ={"Content-type": "application/x-protobuf;charset=utf-8","Connection":"Keep-Alive"}
s.headers.update(headers)
s.get(url)
testlist = []
class checkinTest():
    def checkMysqlPort(self):
    #     findPort = os.popen("netstat -nao|findstr 3306")
    #     findPortR = findPort.read()
    #     retList = findPortR.split(' ')
    #     processPid = retList[len(retList)-1]
         return "1"

    def csvAction(self):
        csvfile = file('checkin_test.csv', 'rb')
        csvReader = csv.reader(csvfile)
        for line in csvReader:
            testlist.append(line)
        csvfile.close()
        return testlist

 #    def mysqlAction(self):
 #        conn = MySQLdb.connect(host=host, user='tuxingadmin', passwd='Tx2010_Tuxing', db=dbName, port=3306)
 #        cur = conn.cursor()
 #        sqlResult = cur.execute(sql)
 #        rList = cur.fetchmany(sqlResult)
 # #       print rList
 #        conn.close()
 #        return rList
 #
 #    def ssh(self):
 #        os.system(sshUrl)

    def threadingAction(self,activation):
        threadsCur = []
        if activation == "ssh":
            # sshT = threading.Thread(target=self.ssh)
            # sshT.start()
            # sshT.join(timeout = 2)
            self.threadingAction("checkAction")
        elif activation == "checkAction":
            con = 1
            print "start"
            while (con <= conTimes):
                checkPara = self.csvAction()
#                print checkPara
                checkInCur = checkIn()
                checkInTime = checkInCur.checkIn(checkInCount)
                for i in range(0,int(checkInCount)):
                    checkInT = threading.Thread(target=checkInCur.doCheckin,
                                                args=(checkInTime,checkPara[i+1][0],checkPara[i+1][1],checkPara[i+1][2]))
                    threadsCur.append(checkInT)
                for i in range(0,int(checkInCount)):
                    checkInT.setDaemon(True)
                    threadsCur[i].start()
                for i in range(0,int(checkInCount)):
                    threadsCur[i].join(timeout=2)
                time.sleep(0.8)
                print len(threadsCur),":",con
                con += 1
                del threadsCur[:]
                if int(con) > int(conTimes):
                    break
            print "end"
class checkIn():

    def timeForamt(self,timeList):
        mTime = datetime.datetime.now().microsecond
        imputDateTime = datetime.datetime(year=int(timeList[0]),month=int(timeList[1]),day=int(timeList[2]),
                                          hour=int(timeList[3]),minute=int(timeList[4]),second=int(timeList[5]))
        formatTime = long(round(time.mktime(imputDateTime.timetuple())))
        checkInTime =  long(str(formatTime)+str(mTime/1000))
        return checkInTime

    def checkIn(self,testCount):
        timeList = []
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

            cardCode = "10000036"
            userId = "2290864"
            gardenId = "1026510"
            timeList.extend([inputYear,inputMonth,inputDay,inputHour,inputMinute,inputSecond])
            checkInTime = self.timeForamt(timeList)

            self.doCheckin(checkInTime,cardCode,userId,gardenId)

        elif testCount > 1:
            inputYear = datetime.datetime.now().year
            inputMonth = datetime.datetime.now().month
            inputDay = datetime.datetime.now().day
            inputHour = datetime.datetime.now().hour
            inputMinute = datetime.datetime.now().minute
            inputSecond = datetime.datetime.now().second
            timeList.extend([inputYear,inputMonth,inputDay,inputHour,inputMinute,inputSecond])
            checkInTime = self.timeForamt(timeList)
            return checkInTime

    def doCheckin(self,checkInTime,cardCode,gardenId,userId):

        messageAttach = wjy_pb2.Attach()
        messageAttach.fileurl = "7bdd56cd-29f1-40fb-a9d3-ac0d722fb01e"
        messageAttach.attachType = long("1")

        ##########Checkin
        print "cardCode: "+cardCode+",userId: "+userId
        messageCheckin = wjy_pb2.Checkin()
        messageCheckin.id = long("12313131321")
        messageCheckin.cardCode = str(cardCode)

        messageCheckin.attach.fileurl= messageAttach.fileurl
        messageCheckin.attach.attachType = messageAttach.attachType
        messageCheckin.userId = long(userId)
        messageCheckin.checkinTime = long(checkInTime)
        messageCheckin.gardenId = long(gardenId)

        ##########CheckinRequest
        machineCheckin = wjy_pb2.CheckinRequest()
        machineCheckin.machineId = "wlm000test00001"

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
 #       print(mainMessage)
        mainPostMessage = mainMessage.SerializeToString()
        postMessage = s.post(url,data=mainPostMessage)

if __name__ == '__main__':
    if checkInCount > 1:
        checkintest = checkinTest()
        if  checkintest.checkMysqlPort() != "":
            # os.system("taskkill /F /pid "+str(checkintest.checkMysqlPort()))
            checkintest.threadingAction("ssh")
        else:
            checkintest.threadingAction("ssh")

    else:
        checkInSigTest = checkIn()
        checkInSigTest.checkIn(1)
