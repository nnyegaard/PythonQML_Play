import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *


class MainWindow(QDeclarativeView):
    """
     Doc string
    """

    def __init__(self, parent=None, qmlFile="view.qml"):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Main Window")
        self.setSource(QUrl(qmlFile))
        self.setResizeMode(QDeclarativeView.SizeRootObjectToView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow(qmlFile="mousePlayView.qml")
    window.show()
    sys.exit(app.exec_())