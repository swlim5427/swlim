#coding=utf-8

from greenlet import greenlet

def test1():
    print 12
    gr2.switch()
    print 34
def test2():
    print 56
    gr1.switch()
    print 78

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
gr2.switch()





# import sys
# import os
# import MySQLdb
# import threading
# import time
# import requests
#
# sshUrl = "ssh -L 3306:tuxingdb.mysql.rds.aliyuncs.com:3306 -tt root@123.57.43.111"
# dbName = "wjy_test"
# dbUrl = "tuxingdb.mysql.rds.aliyuncs.com"
# sql = '''SELECT card_code,garden_id FROM tx_user_card
# WHERE id >=(SELECT FLOOR(RAND() * (SELECT MAX(id) FROM tx_user_card))) AND card_code>1 ORDER BY id LIMIT 1000;
# '''
# host = 'tuxingdb.mysql.rds.aliyuncs.com'
# host = '127.0.0.1'
#
#
# def checkMysqlPort():
#     findPort = os.popen("netstat -nao|findstr 3306")
#     findPortR = findPort.read()
#     retList = findPortR.split(' ')
#     processPid = retList[len(retList)-1]
#     return processPid
#
# def mysqlAction():
#     time.sleep(1)
#     conn = MySQLdb.connect(host=host, user='tuxingadmin', passwd='Tx2010_Tuxing', db=dbName, port=3306)
#     cur = conn.cursor()
#     sqlResult = cur.execute(sql)
#     rList = cur.fetchmany(sqlResult)
#     conn.close()
#     print rList
#  #   return rList
# def ssh():
#     os.system(sshUrl)
#
# def threadinga(type):
#     threads = []
#     if type == "ssh":
#         sshT = threading.Thread(target=ssh)
#         sshMySqlT = threading.Thread(target=mysqlAction)
#         threads.append(sshT)
#         threads.append(sshMySqlT)
#         for i in range(len(threads)):
#             threads[i].start()
#             threads[i].join(timeout = 2)
#
# if checkMysqlPort() !="":
#     os.system("taskkill /F /pid "+str(checkMysqlPort()))
#     threadinga("ssh")
#   #  os.system(sshUrl)
# else:
#     threadinga("ssh")
#  #x   os.system(sshUrl)
#
#
#


'''
global count
count = []

url = "http://123.57.43.111:8080/http_invoke"
s = requests.session()
headers ={"Content-type": "application/x-protobuf;charset=utf-8","Connection":"Keep-Alive"}
s.headers.update(headers)
s.get(url)

fetchAgreementRequest = wjy_pb2.FetchAgreementRequest()
bodyMessageString = fetchAgreementRequest.SerializeToString()

mainMessage = Message_pb2.Request()
mainMessage.url="/fetch_postgroup"
mainMessage.body = bodyMessageString

mainPostMessage = mainMessage.SerializeToString()
f = open('out', 'a+')

def postMessage(messageDelay):
    messageDelay = 2
    for runtimes in range(1,int(messageDelay)+1):
        try:
            postMessage = s.post(url,data=mainPostMessage,timeout=15)
            #localprint = postMessage.text.encode('gbk','ignore')
            print postMessage.elapsed.microseconds/1000,"ms"
            num  =  postMessage.elapsed.microseconds/1000
            count.append(num)
        #    print(localprint)
         #   print >>f,"ppp"+localprint+"ppp"
            postMessage.raise_for_status()
        except requests.RequestException as e:
            print(e)
            print "no 200"+"="+str(postMessage.status_code)
#        localprint = postMessage.text.encode('gbk','ignore')
#        time.sleep(1)
threads = []
times = 3
delay = int(0)
for i in range (0,int(times)):
    t = threading.Thread(target=postMessage,args=str(delay))
    threads.append(t)
for i in range(0,int(times)):
    t.setDaemon(True)
    threads[i].start()
for i in range(0,int(times)):
    threads[i].join(timeout=2)

print len(count)

print sum(count)/len(count)
'''