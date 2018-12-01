from PyQt5.QtWidgets import  QMainWindow, QWidget, QGraphicsScene, QApplication
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor, QImage, QPixmap
from math import cos,sin,pi,radians,copysign, fabs
import numpy as np
import time


class Window(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi('window.ui', self)

        self.scene = QGraphicsScene(0, 0, 500, 500)
        self.mainview.setScene(self.scene)

        self.image = QImage(500, 500, QImage.Format_ARGB32)
        self.pen = QPen()
        # self.color = QColor(Qt.black)
        # self.color_bg = QColor(Qt.white)

        self.drawLine.clicked.connect(lambda: draw_line(self))
        self.drawStar.clicked.connect(lambda: draw_star(self))
        self.clear.clicked.connect(lambda: clear_scene(self))


def sign(x):
    if x == 0:
        return 0
    if x > 0:
        return 1
    else:
        return -1


def dda(win, xn, yn, xk, yk):
    if xn == xk and yn == yk:
        win.image.setPixel(xn, yn, win.pen.color().rgb())
    else:
        xt = xn
        yt = yn

        dx = xk - xn
        dy = yk - yn

        if fabs(dx) > fabs(dy):
            l = fabs(dx)
        else:
            l = fabs(dy)

        dx = dx / l
        dy = dy / l

        while l > 0:
            win.image.setPixel(xt, yt, win.pen.color().rgb())
            xt += dx
            yt += dy
            l -= 1


def brez_float(win, xn, yn, xk, yk):
    print(xk,xn,yk,yn)

    if xn == xk and yn == yk:
        win.image.setPixel(xn, yn, win.pen.color().rgb())

    else:
        dx = xk - xn
        print(dx)
        dy = yk - yn

        sx = sign(dx)
        sy = sign(dy)

        dx = fabs(dx)
        dy = fabs(dy)

        m = dy / dx
        change = 0
        if m < 1:
            change = 0
        else:
            tmp = dx
            dx = dy
            dy = tmp
            change = 1
            m = 1 / m

        error = m - 0.5

        xt = xn
        yt = yn
        i = 1
        while i <= dx:
            win.image.setPixel(xt, yt, win.pen.color().rgb())
            if error >= 0:
                if change == 0:
                    yt += sy
                else:
                    xt += sx
                error -= 1
            if error < 0:
                if change == 0:
                    xt += sx
                else:
                    yt += sy
                error += 1
            i += 1


def brez_int(win, xn, yn, xk, yk):
    if xn == xk and yn == yk:
        win.image.setPixel(xn, yn, win.pen.color().rgb())
    else:
        xt = xn
        yt = yn

        dx = xk - xn
        dy = yk - yn

        sx = sign(dx)
        sy = sign(dy)

        dx = abs(dx)
        dy = abs(dy)

        change = 0

        if dx > dy:
            change = 0
        else:

            tmp = dy
            dy = dx
            dx = tmp
            change = 1
        error = 2 * dy - dx

        for i in range(dx):
            win.image.setPixel(xt, yt, win.pen.color().rgb())
            if error >= 0:
                if change == 0:
                    yt += sy
                else:
                    xt += sx
                error -= 2 * dx
            if error < 0:
                if change == 0:
                    xt += sx
                else:
                    yt += sy

                error += 2 * dy


def brez_smooth(win, xn, yn, xk, yk):
    if xn == xk and yn == yk:
        win.image.setPixel(xn, yn, win.pen.color().rgb())

    else:
        xt = xn
        yt = yn

        dx = xk - xn
        dy = yk - yn

        sx = sign(dx)
        sy = sign(dy)

        dx = abs(dx)
        dy = abs(dy)

        change = 0

        isBlack = False
        if win.pen.color() == Qt.black:
            i_max = 256
            isBlack = True
        else:
            i_max = 100

        m = dy / dx
        if m <= 1:
            change = 0
        else:
            tmp = dy
            dy = dx
            dx = tmp
            change = 1
            m = 1 / m

        m *= i_max
        error = i_max / 2
        w = i_max - m
        i = 1

        while i <= dx:
            if not isBlack:
                new = win.pen.color()
                new.lighter(100 + error)
                win.pen.setColor(new)
                win.image.setPixel(xt, yt, win.pen.color().rgba())
            else:
                new = QColor()
                new.setRgb(0, 0, 0, 255 - error)
                win.pen.setColor(new)
                win.image.setPixel(xt, yt, win.pen.color().rgba())
            if error <= w:
                if change:
                    yt += sy
                else:
                    xt += sx
                error += m
            else:
                xt += sx
                yt += sy
                error -= w
            i += 1


def set_color_line(win):
    if win.blackLine.isChecked():
        win.pen.setColor(QColor(Qt.black))

    if win.greenLine.isChecked():
        win.pen.setColor(QColor(Qt.green))

    if win.redLine.isChecked():
        win.pen.setColor(QColor(Qt.red))

    if win.blueLine.isChecked():
        win.pen.setColor(QColor(Qt.blue))


def set_color_bg(win):
    if win.blackBg.isChecked():
        win.image.fill(QColor(Qt.black))

    if win.greenBg.isChecked():
        win.image.fill(QColor(Qt.green))

    if win.redBg.isChecked():
        win.image.fill(QColor(Qt.red))

    if win.blueBg.isChecked():
        win.image.fill(QColor(Qt.blue))


def draw_line(win):
    xn = int(win.xn.text())
    yn = int(win.yn.text())
    xk = int(win.xk.text())
    yk = int(win.yk.text())

    set_color_line(win)
    # set_color_bg(win)
    if win.cda.isChecked():
        start = time.clock()
        dda(win, xn, yn, xk, yk)
        end = time.clock()
    if win.br_float.isChecked():
        start = time.clock()
        brez_float(win, xn, yn, xk, yk)
        end = time.clock()
    if win.br_int.isChecked():
        start = time.clock()
        brez_int(win, xn, yn, xk, yk)
        end = time.clock()
    if win.br_smooth.isChecked():
        start = time.clock()
        brez_smooth(win, xn, yn, xk, yk)
        end = time.clock()

    pix = QPixmap(500, 500)
    pix.convertFromImage(win.image)
    win.scene.addPixmap(pix)


# def draw_star(win):
#     d = int(win.length.text())
#     spin = int(win.step.text())
#     xn = 250
#     yn = 250
#
#     set_color_line(win)
#     set_color_bg(win)
#
#     for i in np.arange(0, 360, spin):
#         xk = cos(radians(i)) * d + 250
#         yk = sin(radians(i)) * d + 250
#
#         if win.cda.isChecked():
#             start = time.clock()
#             dda(win, xn, yn, xk, yk)
#             end = time.clock()
#         if win.br_float.isChecked():
#             start = time.clock()
#             brez_float(win, xn, yn, xk, yk)
#             end = time.clock()
#         if win.br_int.isChecked():
#             start = time.clock()
#             brez_int(win, xn, yn, xk, yk)
#             end = time.clock()
#         if win.br_smooth.isChecked():
#             start = time.clock()
#             brez_smooth(win, xn, yn, xk, yk)
#             end = time.clock()
#
#
#     pix = QPixmap(500, 500)
#     pix.convertFromImage(win.image)
#     win.scene.addPixmap(pix)

def draw_star(win):

    xn = 250
    yn = 250
    i = 0

    angle = float(win.step.text())

    d = float(win.length.text())
    if win.cda.isChecked():
        while i < 360:
            xk = cos(i * pi/180) * d + 251
            yk = sin(i * pi/180) * d + 251
            dda(win, xn, yn, xk, yk)
            i += angle

    if win.br_float.isChecked():
        while i < 360:
            xk = cos(i * pi/180) * d + 251
            yk = sin(i * pi/180) * d + 251
            brez_float(win, xn, yn, xk, yk)
            i += angle

    if win.br_int.isChecked():
        while i < 360:
            xk = cos(i * pi/180) * d + 251
            yk = sin(i * pi/180) * d + 251
            brez_int(win, xn, yn, xk, yk)
            i += angle


    if win.br_smooth.isChecked():
        while i < 360:
            xk = cos(i * pi/180) * d + 251
            yk = sin(i * pi/180) * d + 251
            brez_smooth(win, xn, yn, xk, yk)
            i += angle

    pix = QPixmap(500, 500)
    pix.convertFromImage(win.image)
    win.scene.addPixmap(pix)



def clear_scene(win):
    win.image.fill(Qt.color0)
    win.scene.clear()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())