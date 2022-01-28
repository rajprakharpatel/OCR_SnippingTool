import sys

import cv2
import numpy as np
from PIL import ImageGrab
from PyQt5 import QtWidgets, QtCore, QtGui


class SnipWidget(QtWidgets.QWidget):
    image = 0

    def __init__(self, scr_w, scr_h):
        super().__init__()
        # self.setGeometry(0, 0, scr_w, scr_h)
        self.setWindowTitle(' ')
        self.start = QtCore.QPoint()
        self.finish = QtCore.QPoint()
        self.setWindowOpacity(.15)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.X11BypassWindowManagerHint)

        # print('Capture the screen...')
        # self.showFullScreen()
        allScreens = QtWidgets.QApplication.desktop().geometry()
        self.setGeometry(allScreens)
        self.show()
        # print(allScreens)

    def paintEvent(self, paintEvent: QtGui.QPaintEvent) -> None:
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(10, 10, 50, 255))
        qp.drawRect(QtCore.QRect(self.start, self.finish))

    def mousePressEvent(self, mouseEvent: QtGui.QMouseEvent) -> None:
        self.start = mouseEvent.pos()
        self.finish = self.start
        self.update()

    def mouseMoveEvent(self, mouseEvent: QtGui.QMouseEvent) -> None:
        self.finish = mouseEvent.pos()
        self.update()

    def mouseReleaseEvent(self, mouseEvent: QtGui.QMouseEvent):
        self.close()
        # storing snip dimension coordinates
        x1 = min(self.start.x(), self.finish.x())
        y1 = min(self.start.y(), self.finish.y())
        x2 = max(self.start.x(), self.finish.x())
        y2 = max(self.start.y(), self.finish.y())

        if x1 == x2 or y1 == y2:
            exit(1)

        SnipWidget.image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        SnipWidget.image.save('capture.png')
        SnipWidget.image = cv2.cvtColor(
            np.array(SnipWidget.image), cv2.COLOR_BGR2RGB)
        # cv2.imshow('Captured Image', SnipWidget.image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    @classmethod
    def get_image(cls):
        return SnipWidget.image


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    size = app.primaryScreen().size()
    window = SnipWidget(size.width(), size.height())
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())
