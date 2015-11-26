import sys
from PyQt4 import QtGui
import time



app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('swlim')
widget.show()
sys.exit(app.exec_())