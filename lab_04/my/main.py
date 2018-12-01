from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPen, QPainter, QColor, QBrush, QImage, QPixmap
from PyQt5.QtCore import Qt
from math import sqrt, pi, cos, sin


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window.ui", self)
        self.scene = QtWidgets.QGraphicsScene(0, 0, 500, 500)
        self.canvas.setScene(self.scene)
        self.image = QImage(511, 511, QImage.Format_ARGB32_Premultiplied)
        self.pen = QPen()
        self.draw.clicked.connect(lambda: self.draw_one())
        self.clear.clicked.connect(lambda: self.clear_canvas())
        self.bg_color.clicked.connect(lambda: self.set_bg_color())
        self.line_color.clicked.connect(lambda: self.set_line_color())
        self.concentr.clicked.connect(lambda: self.draw_konc())
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.what)
        layout.addWidget(self.other)
        # self.setLayout(layout)
        self.circle.setChecked(True)
        self.canon.setChecked(True)

    def circle_canon(self, cx, cy, r):
        for x in range(0, r + 1, 1):
            y = round(sqrt(r ** 2 - x ** 2))
            self.image.setPixel(cx + x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx + x, cy - y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy - y, self.pen.color().rgb())

        for y in range(0, r + 1, 1):
            x = round(sqrt(r ** 2 - y ** 2))

            self.image.setPixel(cx + x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx + x, cy - y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy - y, self.pen.color().rgb())

    def circle_param(self, cx, cy, r):
        len_of_circle = round(2 * pi * r) + 1  # длина окружности
        for i in range(len_of_circle):
            x = (cx + r * cos(i/r))
            y = (cy + r * sin(i/r))
            self.image.setPixel(x, y, self.pen.color().rgb())



    def circle_brez(self, cx, cy, r):
        x = 0  # задание начальных значений
        y = r
        d = 2 - 2 * r  # значение D(x,y)  при (0,R)
        while y >= 0:
            # высвечивание текущего пиксела
            self.image.setPixel(cx + x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx + x, cy - y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy - y, self.pen.color().rgb())

            if d < 0:  # пиксель лежит внутри окружности
                buf = 2 * d + 2 * y - 1
                x += 1

                if buf <= 0:  # горизонтальный шаг
                    d = d + 2 * x + 1
                else:  # диагональный шаг
                    y -= 1
                    d = d + 2 * x - 2 * y + 2

                continue

            if d > 0:  # пиксель лежит вне окружности
                buf = 2 * d - 2 * x - 1
                y -= 1

                if buf > 0:  # вертикальный шаг
                    d = d - 2 * y + 1
                else:  # диагональный шаг
                    x += 1
                    d = d + 2 * x - 2 * y + 2

                continue

            if d == 0.0:  # пиксель лежит на окружности
                x += 1  # диагональный шаг
                y -= 1
                d = d + 2 * x - 2 * y + 2

    def circle_middle(self, cx, cy, r):
        x = 0  # начальные значения
        y = r
        p = 5 / 4 - r  # (x + 1)^2 + (y - 1/2)^2 - r^2
        while True:
            self.image.setPixel(cx - x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx + x, cy - y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy - y, self.pen.color().rgb())
            self.image.setPixel(cx + x, cy + y, self.pen.color().rgb())

            self.image.setPixel(cx - y, cy + x, self.pen.color().rgb())
            self.image.setPixel(cx + y, cy - x, self.pen.color().rgb())
            self.image.setPixel(cx - y, cy - x, self.pen.color().rgb())
            self.image.setPixel(cx + y, cy + x, self.pen.color().rgb())

            x += 1

            if p < 0:  # средняя точка внутри окружности, ближе верхний пиксел, горизонтальный шаг
                p += 2 * x + 1
            else:  # средняя точка вне окружности, ближе диагональный пиксел, диагональный шаг
                p += 2 * x - 2 * y + 5
                y -= 1

            if x > y:
                break

    def ellips_canon(self, cx, cy, a, b):
        for x in range(0, a + 1, 1):
            y = round(b * sqrt(1.0 - x ** 2 / a / a))
            self.image.setPixel(cx + x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx + x, cy - y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy - y, self.pen.color().rgb())

        for y in range(0, b + 1, 1):
            x = round(a * sqrt(1.0 - y ** 2 / b / b))
            self.image.setPixel(cx + x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx + x, cy - y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy - y, self.pen.color().rgb())

    def ellips_param(self, cx, cy, a, b):
        m = max(a, b)
        l = round(pi * m / 2)
        for i in range(0, l + 1, 1):
            x = round(a * cos(i / m))
            y = round(b * sin(i / m))
            self.image.setPixel(cx + x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx + x, cy - y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy - y, self.pen.color().rgb())


    def ellips_brez(self, cx, cy, a, b):
        x = 0  # начальные значения
        y = b
        a = a ** 2
        d = round(b * b / 2 - a * b * 2 + a / 2)
        b = b ** 2
        while y >= 0:
            self.image.setPixel(cx + x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx + x, cy - y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy - y, self.pen.color().rgb())
            if d < 0:  # пиксель лежит внутри эллипса
                buf = 2 * d + 2 * a * y - a
                x += 1
                if buf <= 0:  # горизотальный шаг
                    d = d + 2 * b * x + b
                else:  # диагональный шаг
                    y -= 1
                    d = d + 2 * b * x - 2 * a * y + a + b

                continue

            if d > 0:  # пиксель лежит вне эллипса
                buf = 2 * d - 2 * b * x - b
                y -= 1

                if buf > 0:  # вертикальный шаг
                    d = d - 2 * y * a + a
                else:  # диагональный шаг
                    x += 1
                    d = d + 2 * x * b - 2 * y * a + a + b

                continue

            if d == 0.0:  # пиксель лежит на окружности
                x += 1  # диагональный шаг
                y -= 1
                d = d + 2 * x * b - 2 * y * a + a + b

    def ellips_middle(self, cx, cy, a, b):
        x = 0  # начальные положения
        y = b
        p = b * b - a * a * b + 0.25 * a * a  # начальное значение параметра принятия решения в области tg<1
        while 2 * (b ** 2) * x < 2 * a * a * y:  # пока тангенс угла наклона меньше 1
            self.image.setPixel(cx - x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx + x, cy - y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy - y, self.pen.color().rgb())
            self.image.setPixel(cx + x, cy + y, self.pen.color().rgb())

            x += 1

            if p < 0:  # средняя точка внутри эллипса, ближе верхний пиксел, горизонтальный шаг
                p += 2 * b * b * x + b * b
            else:  # средняя точка вне эллипса, ближе диагональный пиксел, диагональный шаг
                y -= 1
                p += 2 * b * b * x - 2 * a * a * y + b * b

        p = b * b * (x + 0.5) * (x + 0.5) + a * a * (y - 1) * (y - 1) - a * a * b * b
        # начальное значение параметра принятия решения в области tg>1 в точке (х + 0.5, y - 1) полседнего положения

        while y >= 0:
            self.image.setPixel(cx - x, cy + y, self.pen.color().rgb())
            self.image.setPixel(cx + x, cy - y, self.pen.color().rgb())
            self.image.setPixel(cx - x, cy - y, self.pen.color().rgb())
            self.image.setPixel(cx + x, cy + y, self.pen.color().rgb())

            y -= 1

            if p > 0:
                p -= 2 * a * a * y + a * a
            else:
                x += 1
                p += 2 * b * b * x - 2 * a * a * y + a * a

    def draw_one(self):
        is_standart = False
        x = int(self.xc.text())
        y = int(self.yc.text())

        if self.circle.isChecked():
            r = int(self.radius.text())

            if self.canon.isChecked():
                self.circle_canon(x+250, y+250, r)
            if self.param.isChecked():
                self.circle_canon(x+250, y+250, r)
            if self.brez.isChecked():
                self.circle_canon(x+250, y+250, r)
            if self.middleDot.isChecked():
                self.circle_canon(x+250, y+250, r)
            if self.bibl.isChecked():
                is_standart = True
                self.scene.addEllipse(x + 250 - r, y + 250 - r, r * 2, r * 2, self.pen)

        if self.ellips.isChecked():
            a = int(self.A.text())
            b = int(self.B.text())

            if self.canon.isChecked():
                self.ellips_canon(x+250, y+250, b, a)
            if self.param.isChecked():
                self.ellips_canon(x+250, y+250, b, a)
            if self.brez.isChecked():
                self.ellips_canon(x+250, y+250, b, a)
            if self.middleDot.isChecked():
                self.ellips_canon(x+250, y+250, b, a)
            if self.bibl.isChecked():
                is_standart = True
                self.scene.addEllipse(x +250- b, y+250 - a, b * 2, a * 2, self.pen)

        if not is_standart:
            pix = QPixmap(511, 511)
            pix.convertFromImage(self.image)
            self.scene.addPixmap(pix)


    def draw_konc(self):
        is_standart = False
        x = int(self.xc.text())
        y = int(self.yc.text())
        d = int(self.step.text())
        c = int(self.amount.text())

        if self.circle.isChecked():
            for i in range(d, d * c + d, d):

                if self.canon.isChecked():
                    self.circle_canon(x+250, y+250, i)
                if self.param.isChecked():
                    self.circle_canon(x+250, y+250, i)
                if self.brez.isChecked():
                    self.circle_canon(x+250, y+250, i)
                if self.middleDot.isChecked():
                    self.circle_canon(x+250, y+250, i)
                if self.bibl.isChecked():
                    is_standart = True
                    self.scene.addEllipse(x+250 - i, y+250 - i, i * 2, i * 2, self.pen)

        if self.ellips.isChecked():
            for i in range(d, d * c + d, d):
                if self.canon.isChecked():
                    self.ellips_canon(x+250, y+250, i * 2, i)
                if self.param.isChecked():
                    self.ellips_canon(x+250, y+250, i * 2, i)
                if self.brez.isChecked():
                    self.ellips_canon(x+250, y+250, i * 2, i)
                if self.middleDot.isChecked():
                    self.ellips_canon(x+250, y+250, i * 2, i)
                if self.bibl.isChecked():
                    self.is_standart = True
                    self.scene.addEllipse(x+250 - i * 2, y+250 - i, i * 4, i * 2, self.pen)

        if not is_standart:
            pix = QPixmap(511, 511)
            pix.convertFromImage(self.image)
            self.scene.addPixmap(pix)

    def set_bg_color(self):
        color = QtWidgets.QColorDialog.getColor(initial=Qt.white, title='Цвет фона',
                                                options=QtWidgets.QColorDialog.DontUseNativeDialog)
        if color.isValid():
            self.color_bground = color
            self.image.fill(color)
            s = QtWidgets.QGraphicsScene(0, 0, 10, 10)
            s.setBackgroundBrush(color)
            self.bg_color_win.setScene(s)
            self.scene.setBackgroundBrush(color)

    def set_line_color(self):
        color = QtWidgets.QColorDialog.getColor(initial=Qt.black, title='Цвет линии',
                                                options=QtWidgets.QColorDialog.DontUseNativeDialog)
        if color.isValid():
            self.color_line = color
            self.pen.setColor(color)
            s = QtWidgets.QGraphicsScene(0, 0, 10, 10)
            s.setBackgroundBrush(color)
            self.line_color_win.setScene(s)

    def clear_canvas(self):
        self.image.fill(Qt.color0)
        self.scene.clear()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())