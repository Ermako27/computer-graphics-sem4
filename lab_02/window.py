import sys
from PyQt5.QtCore import Qt, QPointF, QPoint, QRectF
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5 import uic

from math import radians, cos, sin, pi
import numpy as np



class Picture(QGraphicsItem):
    def __init__(self):
        super(Picture, self).__init__()

        self.bottomX = [80*cos(-1*t) + 520 for t in np.arange(0, pi, 0.001)]  # нижная дуга
        self.bottomY = [15*sin(-1*t) + 580 for t in np.arange(0, pi, 0.001)]


        self.rightX = [520 + (self.bottomX[i] - 520) * cos(radians(120)) + (self.bottomY[i] - 580) *
                       sin(radians(120)) + 42 for i in range(len(self.bottomX))]  # правая дуга
        self.rightY = [580 - (self.bottomX[i] - 520) * sin(radians(120)) + (self.bottomY[i] - 580) *
                       cos(radians(120)) - 70 for i in range(len(self.bottomY))]


        self.leftX = [520 + (self.bottomX[i] - 520) * cos(radians(240)) + (self.bottomY[i] - 580) *
                       sin(radians(240)) - 42 for i in range(len(self.bottomX))]  # правая дуга
        self.leftY = [580 - (self.bottomX[i] - 520) * sin(radians(240)) + (self.bottomY[i] - 580) *
                       cos(radians(240)) - 70 for i in range(len(self.bottomY))]

        self.leftLine = [520, 440, 600, 580]  # линии
        self.rightLine = [520, 440, 440, 580]

        self.pTopleft = [440, 440]  # квадрат
        self.pTopright = [600, 440]
        self.pBotright = [600, 580]
        self.pBotleft = [440, 580]
        
        # предыдущее состояние
        self.prev_bottomX = self.bottomX  # дуги
        self.prev_bottomY = self.bottomY
        self.prev_leftX = self.leftX
        self.prev_leftY = self.leftY
        self.prev_rightX = self.rightX
        self.prev_rightY = self.rightY

        self.prev_leftLine = self.leftLine[:]  # линии
        self.prev_rightLine = self.rightLine[:]

        self.prev_pTopleft = self.pTopleft[:]  # квадрат
        self.prev_pTopright = self.pTopright[:]
        self.prev_pBotright = self.pBotright[:]
        self.prev_pBotleft = self.pBotleft[:]

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
        # предыдущее состояние
        self.prev_bottomX = self.bottomX  # дуги
        self.prev_bottomY = self.bottomY
        self.prev_leftX = self.leftX
        self.prev_leftY = self.leftY
        self.prev_rightX = self.rightX
        self.prev_rightY = self.rightY

        self.prev_leftLine = self.leftLine[:]  # линии
        self.prev_rightLine = self.rightLine[:]

        self.prev_pTopleft = self.pTopleft[:]  # квадрат
        self.prev_pTopright = self.pTopright[:]
        self.prev_pBotright = self.pBotright[:]
        self.prev_pBotleft = self.pBotleft[:]

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

        # предыдущее состояние
        self.prev_bottomX = self.bottomX  # дуги
        self.prev_bottomY = self.bottomY
        self.prev_leftX = self.leftX
        self.prev_leftY = self.leftY
        self.prev_rightX = self.rightX
        self.prev_rightY = self.rightY

        self.prev_leftLine = self.leftLine[:]  # линии
        self.prev_rightLine = self.rightLine[:]

        self.prev_pTopleft = self.pTopleft[:]  # квадрат
        self.prev_pTopright = self.pTopright[:]
        self.prev_pBotright = self.pBotright[:]
        self.prev_pBotleft = self.pBotleft[:]

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

        # предыдущее состояние
        self.prev_bottomX = self.bottomX  # дуги
        self.prev_bottomY = self.bottomY
        self.prev_leftX = self.leftX
        self.prev_leftY = self.leftY
        self.prev_rightX = self.rightX
        self.prev_rightY = self.rightY

        self.prev_leftLine = self.leftLine[:]  # линии
        self.prev_rightLine = self.rightLine[:]

        self.prev_pTopleft = self.pTopleft[:]  # квадрат
        self.prev_pTopright = self.pTopright[:]
        self.prev_pBotright = self.pBotright[:]
        self.prev_pBotleft = self.pBotleft[:]

        xc = float(place.rotateCentreX.text())  # центр поворота
        yc = float(place.rotateCentreY.text())

        ang = int(place.angle.text())  # угол поворота
        l = len(self.bottomX)

        # поворот дуг

        self.bottomX = [xc + (self.prev_bottomX[i] - xc) * cos(radians(ang)) + (self.prev_bottomY[i] - yc) * sin(radians(ang)) for i in range(l)]
        self.bottomY = [yc - (self.prev_bottomX[i] - xc) * sin(radians(ang)) + (self.prev_bottomY[i] - yc) * cos(radians(ang)) for i in range(l)]

        self.leftX = [xc + (self.prev_leftX[i] - xc) * cos(radians(ang)) + (self.prev_leftY[i] - yc) * sin(radians(ang))  for i in range(l)]
        self.leftY = [yc - (self.prev_leftX[i] - xc) * sin(radians(ang)) + (self.prev_leftY[i] - yc) * cos(radians(ang)) for i in range(l)]

        self.rightX = [xc + (self.prev_rightX[i] - xc) * cos(radians(ang)) + (self.prev_rightY[i] - yc) * sin(radians(ang)) for i in range(l)]
        self.rightY = [yc - (self.prev_rightX[i] - xc) * sin(radians(ang)) + (self.prev_rightY[i] - yc) * cos(radians(ang)) for i in range(l)]

        # поворот линий
        self.leftLine[0], self.leftLine[1] = [xc + (self.leftLine[0] - xc) * cos(radians(ang)) + (self.leftLine[1] - yc) * sin(radians(ang)),  
                        yc - (self.leftLine[0] - xc) * sin(radians(ang)) + (self.leftLine[1] - yc) * cos(radians(ang))]
        self.leftLine[2], self.leftLine[3] = [xc + (self.leftLine[2] - xc) * cos(radians(ang)) + (self.leftLine[3] - yc) * sin(radians(ang)),  
                        yc - (self.leftLine[2] - xc) * sin(radians(ang)) + (self.leftLine[3] - yc) * cos(radians(ang))]
        
        self.rightLine[0], self.rightLine[1] = [xc + (self.rightLine[0] - xc) * cos(radians(ang)) + (self.rightLine[1] - yc) * sin(radians(ang)),  
                        yc - (self.rightLine[0] - xc) * sin(radians(ang)) + (self.rightLine[1] - yc) * cos(radians(ang))]
        self.rightLine[2], self.rightLine[3] = [xc + (self.rightLine[2] - xc) * cos(radians(ang)) + (self.rightLine[3] - yc) * sin(radians(ang)),  
                        yc - (self.rightLine[2] - xc) * sin(radians(ang)) + (self.rightLine[3] - yc) * cos(radians(ang))]
                                                
        # поворот прямоугольника
        self.pTopleft[0], self.pTopleft[1] = [xc + (self.pTopleft[0] - xc) * cos(radians(ang)) + (self.pTopleft[1] - yc) * sin(radians(ang)),  
                        yc - (self.pTopleft[0] - xc) * sin(radians(ang)) + (self.pTopleft[1] - yc) * cos(radians(ang))]
        self.pTopright[0], self.pTopright[1] = [xc + (self.pTopright[0] - xc) * cos(radians(ang)) + (self.pTopright[1] - yc) * sin(radians(ang)),  
                        yc - (self.pTopright[0] - xc) * sin(radians(ang)) + (self.pTopright[1] - yc) * cos(radians(ang))]
        self.pBotleft[0], self.pBotleft[1] = [xc + (self.pBotleft[0] - xc) * cos(radians(ang)) + (self.pBotleft[1] - yc) * sin(radians(ang)),  
                        yc - (self.pBotleft[0] - xc) * sin(radians(ang)) + (self.pBotleft[1] - yc) * cos(radians(ang))]
        self.pBotright[0], self.pBotright[1] = [xc + (self.pBotright[0] - xc) * cos(radians(ang)) + (self.pBotright[1] - yc) * sin(radians(ang)),  
                        yc - (self.pBotright[0] - xc) * sin(radians(ang)) + (self.pBotright[1] - yc) * cos(radians(ang))]

        self.update()

    def start(self):
        self.bottomX = [80*cos(-1*t) + 520 for t in np.arange(0, pi, 0.001)]  # нижная дуга
        self.bottomY = [15*sin(-1*t) + 580 for t in np.arange(0, pi, 0.001)]


        self.rightX = [520 + (self.bottomX[i] - 520) * cos(radians(120)) + (self.bottomY[i] - 580) *
                       sin(radians(120)) + 42 for i in range(len(self.bottomX))]  # правая дуга
        self.rightY = [580 - (self.bottomX[i] - 520) * sin(radians(120)) + (self.bottomY[i] - 580) *
                       cos(radians(120)) - 70 for i in range(len(self.bottomY))]


        self.leftX = [520 + (self.bottomX[i] - 520) * cos(radians(240)) + (self.bottomY[i] - 580) *
                       sin(radians(240)) - 42 for i in range(len(self.bottomX))]  # правая дуга
        self.leftY = [580 - (self.bottomX[i] - 520) * sin(radians(240)) + (self.bottomY[i] - 580) *
                       cos(radians(240)) - 70 for i in range(len(self.bottomY))]

        self.leftLine = [520, 440, 600, 580]  # линии
        self.rightLine = [520, 440, 440, 580]

        self.pTopleft = [440, 440]  # квадрат
        self.pTopright = [600, 440]
        self.pBotright = [600, 580]
        self.pBotleft = [440, 580]
        self.update()

    def back(self):
        # предыдущее состояние
        self.bottomX = self.prev_bottomX  # дуги
        self.bottomY = self.prev_bottomY
        self.leftX = self.prev_leftX
        self.leftY = self.prev_leftY
        self.rightX = self.prev_rightX
        self.rightY = self.prev_rightY

        self.leftLine = self.prev_leftLine[:]  # линии
        self.rightLine = self.prev_rightLine[:]

        self.pTopleft = self.prev_pTopleft[:]  # квадрат
        self.pTopright = self.prev_pTopright[:]
        self.pBotright = self.prev_pBotright[:]
        self.pBotleft = self.prev_pBotleft[:]
        self.update()




class Wind(QGraphicsView):
    def __init__(self):
        super(Wind, self).__init__()
        self.place = uic.loadUi('window.ui')  # атрибут окна
        self.object = Picture()  # артибут картинки
        scene = QGraphicsScene(self)
        scene.setSceneRect(10, 10, 1000, 1000)
        scene.addItem(self.object)
        self.place.image.setScene(scene)
        self.place.move.clicked.connect(lambda: self.object.moveFunc(self.place))
        self.place.scale.clicked.connect(lambda: self.object.scaleFunc(self.place))
        self.place.rotate.clicked.connect(lambda: self.object.rotateFunc(self.place))
        self.place.toStart.clicked.connect(lambda: self.object.start())
        self.place.stepBack.clicked.connect(lambda: self.object.back())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Wind()
    ex.place.show()
    sys.exit(app.exec_())

