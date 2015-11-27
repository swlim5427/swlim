import sys
from PyQt4 import QtGui
import time
import datetime
import StringIO
import cStringIO


def timeAction():

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
    return nowTime

startTime = timeAction()

timeInIO = StringIO.StringIO(startTime)
#timeInIO.write(startTime)
time.sleep(2)
timeOutIO = timeInIO.getvalue()
print timeAction()
print timeOutIO
timeInIO.close()



'''
app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('swlim')
widget.show()
sys.exit(app.exec_())
'''