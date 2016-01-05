#coding=utf-8
import sys
#import requests
'''
import Message_pb2
import wjy_pb2
import time
import datetime
import threading
'''

def deco(func):
    
    print("before myfunc() called.")
    func()
    print ("after myfunc() called.")
    return func 
@deco

def myfunc():
    print ("myfunc() called.")
    
    
myfunc()
myfunc()



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