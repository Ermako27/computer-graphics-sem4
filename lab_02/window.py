import sys
from PyQt5.QtCore import Qt, QPointF, QPoint, QRectF
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5 import uic

import math
import numpy as np

class Picture(QGraphicsItem):
    def __init__(self):
        super(Picture, self).__init__()

        self.bottomX = [80*math.cos(-1*t) + 520 for t in np.arange(0, math.pi, 0.001)]  # нижная дуга
        self.bottomY = [15*math.sin(-1*t) + 580 for t in np.arange(0, math.pi, 0.001)]


        self.rightX = [520 + (self.bottomX[i] - 520) * math.cos(math.radians(120)) + (self.bottomY[i] - 580) *
                       math.sin(math.radians(120)) + 42 for i in range(len(self.bottomX))]  # правая дуга
        self.rightY = [580 - (self.bottomX[i] - 520) * math.sin(math.radians(120)) + (self.bottomY[i] - 580) *
                       math.cos(math.radians(120)) - 70 for i in range(len(self.bottomY))]


        self.leftX = [520 + (self.bottomX[i] - 520) * math.cos(math.radians(240)) + (self.bottomY[i] - 580) *
                       math.sin(math.radians(240)) - 42 for i in range(len(self.bottomX))]  # правая дуга
        self.leftY = [580 - (self.bottomX[i] - 520) * math.sin(math.radians(240)) + (self.bottomY[i] - 580) *
                       math.cos(math.radians(240)) - 70 for i in range(len(self.bottomY))]

        self.leftLine = [520, 440, 600, 580]  # линии
        self.rightLine = [520, 440, 440, 580]

        self.pTopleft = [440, 440]  # квадрат
        self.pTopright = [600, 440]
        self.pBotright = [600, 580]
        self.pBotleft = [440, 580]

    def paint(self, painter, option, widget):
        # отрисовка дуг
        for i in range(len(self.bottomX)):
            painter.drawLine(self.bottomX[i], self.bottomY[i], self.bottomX[i] + 0.01, self.bottomY[i] + 0.01)
            painter.drawLine(self.rightX[i], self.rightY[i], self.rightX[i] + 0.01, self.rightY[i] + 0.01)
            painter.drawLine(self.leftX[i], self.leftY[i], self.leftX[i] + 0.01, self.leftY[i] + 0.01)
        # отрисовка прямоугольника
        painter.drawPolygon(
            QPointF(self.pTopleft[0], self.pTopleft[1]),
            QPointF(self.pTopright[0], self.pTopright[1]),
            QPointF(self.pBotright[0], self.pBotright[1]),
            QPointF(self.pBotleft[0], self.pBotleft[1]),
        )

        # отрисовка линий
        painter.drawLine(self.leftLine[0], self.leftLine[1], self.leftLine[2], self.leftLine[3])
        painter.drawLine(self.rightLine[0], self.rightLine[1], self.rightLine[2], self.rightLine[3])

    def boundingRect(self):
        return QRectF(10, 10, 1000, 1000)

    def moveFunc(self, place):
        dx = float(place.moveX.text())  # получаем значения с полей ввода
        dy = float(place.moveY.text())

        self.bottomX = [elem + dx for elem in self.bottomX]
        self.bottomY = [elem + dy for elem in self.bottomY]

        self.rightX = [elem + dx for elem in self.rightX]
        self.rightY = [elem + dy for elem in self.rightY]

        self.leftX = [elem + dx for elem in self.leftX]
        self.leftY = [elem + dy for elem in self.leftY]

        self.leftLine[0], self.leftLine[1] = self.leftLine[0] + dx, self.leftLine[1] + dy
        self.leftLine[2], self.leftLine[3] = self.leftLine[2] + dx, self.leftLine[3] + dy

        self.rightLine[0], self.rightLine[1] = self.rightLine[0] + dx, self.rightLine[1] + dy
        self.rightLine[2], self.rightLine[3] = self.rightLine[2] + dx, self.rightLine[3] + dy

        self.pTopleft[0], self.pTopleft[1] = self.pTopleft[0] + dx, self.pTopleft[1] + dy
        self.pTopright[0], self.pTopright[1] = self.pTopright[0] + dx, self.pTopright[1] + dy
        self.pBotleft[0], self.pBotleft[1] = self.pBotleft[0] + dx, self.pBotleft[1] + dy
        self.pBotright[0], self.pBotright[1] = self.pBotright[0] + dx, self.pBotright[1] + dy

        self.update()

    def scaleFunc(self, place):
        xm = float(place.scaleCentreX.text())  # центр масштабирования
        ym = float(place.scaleCentreY.text())

        kx = float(place.scaleX.text())  # коэффициенты масстабирования
        ky = float(place.scaleY.text())

        # масштабирование дуг
        self.bottomX = [kx * elem + (1 - kx) * xm for elem in self.bottomX]
        self.bottomY = [ky * elem + (1 - ky) * ym for elem in self.bottomY]

        self.leftX = [kx * elem + (1 - kx) * xm for elem in self.leftX]
        self.leftY = [ky * elem + (1 - ky) * ym for elem in self.leftY]

        self.rightX = [kx * elem + (1 - kx) * xm for elem in self.rightX]
        self.rightY = [ky * elem + (1 - ky) * ym for elem in self.rightY]

        # маштабирование линий
        self.leftLine[0], self.leftLine[1] = kx * self.leftLine[0] + (1 - kx) * xm, ky * self.leftLine[1] + (1 - ky) * ym
        self.leftLine[2], self.leftLine[3] = kx * self.leftLine[2] + (1 - kx) * xm, ky * self.leftLine[3] + (1 - ky) * ym

        self.rightLine[0], self.rightLine[1] = kx * self.rightLine[0] + (1 - kx) * xm, ky * self.rightLine[1] + (1 - ky) * ym
        self.rightLine[2], self.rightLine[3] = kx * self.rightLine[2] + (1 - kx) * xm, ky * self.rightLine[3] + (1 - ky) * ym

        # масштабирование прямоугольника
        self.pTopleft[0], self.pTopleft[1] = kx * self.pTopleft[0] + (1 - kx) * xm, ky * self.pTopleft[1] + (1 - ky) * ym
        self.pTopright[0], self.pTopright[1] = kx * self.pTopright[0] + (1 - kx) * xm, ky * self.pTopright[1] + (1 - ky) * ym
        self.pBotleft[0], self.pBotleft[1] = kx * self.pBotleft[0] + (1 - kx) * xm, ky * self.pBotleft[1] + (1 - ky) * ym
        self.pBotright[0], self.pBotright[1] = kx * self.pBotright[0] + (1 - kx) * xm, ky * self.pBotright[1] + (1 - ky) * ym

        self.update()





    def rotateFunc(self, place):
        pass

class Wind(QGraphicsView):
    def __init__(self):
        super(Wind, self).__init__()
        self.place = uic.loadUi('window.ui')  # атрибут окна
        self.object = Picture()  # артибут картинки
        scene = QGraphicsScene(self)
        scene.setSceneRect(10, 10, 2000, 2000)
        scene.addItem(self.object)
        self.place.image.setScene(scene)
        self.place.move.clicked.connect(lambda: self.object.moveFunc(self.place))
        self.place.scale.clicked.connect(lambda: self.object.scaleFunc(self.place))
        self.place.rotate.clicked.connect(lambda: self.object.rotateFunc(self.place))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Wind()
    ex.place.show()
    sys.exit(app.exec_())

