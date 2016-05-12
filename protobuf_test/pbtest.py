
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
    resMessage.ParseFromString(postMessage.text)
    #print resMessage
    logInResponse = wjy_pb2.LoginResponse()
#    print logInResponse
#    print resMessage.body.encode('gbk','ignore')
#    res = u'\x08\x01\x12700e5831b6804412ad9505b50cb9395a\x1a\x83\x01\x08\xdc\xc7\x8c\x01\x12\ttx2302940\x1a\x0fmorgen\xe7\x9a\x84\xe7\x88\xb8\xe7\x88\xb8(\xdb\xc7\x8c\x012\x0b14011000005@\x02z\x12\xe7\xba\xa2\xe9\xbb\x84\xe8\x93\x9d\xe5\xb9\xbc\xe5\x84\xbf\xe5\x9b\xad\x82\x01\t\xe5\xbd\xa9\xe8\x99\xb9\xe7\x8f\xad\x88\x01\x01\x90\x01\xa4\xd8>\x98\x01\x8d\xd9>\xb8\x01\x01\xca\x01\t\x08\xdb\xc7\x8c\x01\x10\x01\x18\x01\xd2\x01\x0fmorgen\xe7\x9a\x84\xe7\x88\xb8\xe7\x88\xb8"\x08\n\x04mute\x12\x00"G\n\thome_menu\x12:announcement,activity,recipes,checkIn,notice,medicine,mail"\x11\n\x0ccloud_lesson\x12\x011"\x14\n\x0fbaby_playground\x12\x011'
    #logInResponse.ParseFromString(resMessage.body.encode('gbk'))

    try:
        logInResponse.ParseFromString(resMessage.body)
    except Exception as e:
        print e



if __name__ == '__main__':
    getConPara =  SysConstants().SysConstants()
    logIn(getConPara)