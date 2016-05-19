# -*- coding: UTF-8 -*-
import requests
import Message_pb2
import wjy_pb2
import base64

class SysConstants():
    def SysConstants(self):
        ip = "192.168.10.210:9022"
        url = "http://"+ip+"/http_invoke"
        s = requests.session()
        headers ={"Content-type": "application/x-protobuf;charset=utf-8","Connection":"Keep-Alive"}
        connectList = [ip,url,s,headers]
        return connectList

def logIn(getConPara):

    url = getConPara[1]
    s = getConPara[2]
    headers = getConPara[3]
    s.headers.update(headers)
    s.get(url)

    messageLogin = wjy_pb2.LoginRequest()
    messageLogin.username = "14011000005"
    messageLogin.password = "111111"
    bodyMessageString = messageLogin.SerializeToString()
    mainMessage = Message_pb2.Request()
    mainMessage.url="/login"
    mainMessage.version = "parent_2.2.5"
    mainMessage.osName = "android"
    mainMessage.osVersion = "4.4.2"
    mainMessage.body = bodyMessageString
    mainPostMessage = mainMessage.SerializeToString()

    postMessage = s.post(url,data=mainPostMessage)
    resMessage = Message_pb2.Response()
    try:
        resMessage.ParseFromString(postMessage.text)
    except:
        resMessage.ParseFromString(postMessage.text.encode('utf8','ignore'))
        print resMessage.statusTxt.encode('gbk','ignore')
    logInResponse = wjy_pb2.LoginResponse()
#    print logInResponse
#    print resMessage.body.encode('gbk','ignore')

    logInResponse.ParseFromString(resMessage.body.encode('utf8'))




if __name__ == '__main__':
    getConPara =  SysConstants().SysConstants()
    logIn(getConPara)