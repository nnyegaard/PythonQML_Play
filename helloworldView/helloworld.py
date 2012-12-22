import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *


app = QApplication(sys.argv)
view = QDeclarativeView()

view.setSource(QUrl("helloworldView.qml"))
view.setResizeMode(QDeclarativeView.SizeRootObjectToView)

view.show()

sys.exit(app.exec_())