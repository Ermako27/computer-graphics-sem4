from tkinter import *
from interface_func import Table
import pandas as pd
import math


def tb_create(frame):
    coordinates = []
    for row in frame.dropna().itertuples():
        coordinates.append((row[0], row[1], row[2], row[3]))
    return coordinates


def x_find(dot1, dot2, y):
    return (((y - dot1[1]) * (dot2[0] - dot1[0])) / (dot2[1] - dot1[1])) + dot1[0]


def circle(x, y, r, canvas, colour='black', out='black', t=None):  # построить окружность по радиусу и центру
    k = 25
    canvas.create_oval(500 + x * k - r, 500 - y * k - r, 500 + x * k + r, 500 - y * k + r, fill=colour, outline=out,
                       tag=t)


def create_triangle(dot1, dot2, dot3, canvas, triger=0):  # построение треугольника
    dot1 = [int(i) for i in dot1.split()]
    dot2 = [int(i) for i in dot2.split()]
    dot3 = [int(i) for i in dot3.split()]

    if triger == 0:
        canvas.create_line(500 + (dot1[0] * 25), 500 - (dot1[1] * 25), 500 + (dot2[0] * 25), 500 - (dot2[1] * 25),
                           width=2, fill='green', tag='del')

        canvas.create_line(500 + (dot1[0] * 25), 500 - (dot1[1] * 25), 500 + (dot3[0] * 25), 500 - (dot3[1] * 25),
                           width=2, fill='green', tag='del')

        canvas.create_line(500 + (dot2[0] * 25), 500 - (dot2[1] * 25), 500 + (dot3[0] * 25), 500 - (dot3[1] * 25),
                           width=2, fill='green', tag='del')
    elif triger == 1:
        if dot1[0] == dot2[0]:
            canvas.create_line(500 + dot1[0]*25, 0, 500 + dot1[0]*25, 1000, width=2, fill='green', tag='del')
        if dot1[0] == dot3[0]:
            canvas.create_line(500 + dot1[0]*25, 0, 500 + dot1[0]*25, 1000, width=2, fill='green', tag='del')
        if dot2[0] == dot3[0]:
            canvas.create_line(500 + dot2[0]*25, 0, 500 + dot2[0]*25, 1000, width=2, fill='green', tag='del')

        if dot1[1] == dot2[1]:
            canvas.create_line(0, 500 - dot1[1]*25, 1000, 500 - dot1[1]*25, width=2, fill='green', tag='del')
        if dot1[1] == dot3[1]:
            canvas.create_line(0, 500 - dot1[1]*25, 1000, 500 - dot1[1]*25, width=2, fill='green', tag='del')
        if dot2[1] == dot3[1]:
            canvas.create_line(0, 500 - dot2[1]*25, 1000, 500 - dot2[1]*25, width=2, fill='green', tag='del')

        if (dot1[0] != dot2[0]) & (dot1[1] != dot2[1]):
            x1 = x_find(dot1, dot2, 20)
            x2 = x_find(dot1,dot2,-20)
            canvas.create_line(500 + x1 * 25, 0, 500 + x2 * 25, 1000, width=2, fill='green', tag='del')

        if (dot1[0] != dot3[0]) & (dot1[1] != dot3[1]):
            x1 = x_find(dot1, dot3, 20)
            x2 = x_find(dot1, dot3, -20)
            canvas.create_line(500 + x1 * 25, 0, 500 + x2 * 25, 1000, width=2, fill='green', tag='del')

        if (dot2[0] != dot3[0]) & (dot2[1] != dot3[1]):
            x1 = x_find(dot2, dot3, 20)
            x2 = x_find(dot2, dot3, -20)
            canvas.create_line(500 + x1 * 25, 0, 500 + x2 * 25, 1000, width=2, fill='green', tag='del')

    circle(dot1[0], dot1[1], 3, canvas, 'green', t='del')
    circle(dot2[0], dot2[1], 3, canvas, 'green', t='del')
    circle(dot3[0], dot3[1], 3, canvas, 'green', t='del')


def print_all_figures(dot1, dot2, dot3, frame, canvas):  # напечатать все точки из датафрэйм
    canvas.delete('del')
    canvas.delete('all_del')
    i = 0
    create_triangle(dot1, dot2, dot3, canvas)
    for row in frame.dropna().itertuples():
        circle(int(row[1]), int(row[2]), 3, canvas, t='all_del')
        text = str(i) + '.' + str((row[1], row[2]))
        canvas.create_text(500 + row[1]*25 + 10, 500 - row[2]*25 + 10, text=text, fill='blue', font=('Helvectica', '12'), tag='all_del')
        i += 1

    comb = dots_combinations(frame)

    for elem in comb:  # отрисовка всевозможных окружностей
        center = center_coordinates_find(elem[0], elem[1], elem[2])  # находим центр окружности
        radius = len_of_line(elem[0], center)  # находим радиус
        circle(center[0], center[1], radius*25, canvas, None, t='del')


def insert_answer(frame, coordinates):
    frame.loc[len(frame)] = coordinates


def print_solution(dot1, dot2, dot3, frame, canvas):
    i = 0
    df = pd.DataFrame(columns=['x', 'y', 'радиус'])
    canvas.delete('del')
    create_triangle(dot1, dot2, dot3, canvas, 1)


    dot1 = [int(i) for i in dot1.split()]
    dot2 = [int(i) for i in dot2.split()]
    dot3 = [int(i) for i in dot3.split()]
    comb = dots_combinations(frame.dropna())

    for elem in comb:
        center = center_coordinates_find(elem[0], elem[1], elem[2])  # находим центр окружности
        if belonging(dot1, dot2, dot3, center):
            radius = len_of_line(elem[0], center)  # находим радиус
            circle(center[0], center[1], radius*25, canvas, None, 'red', 'del')
            circle(center[0], center[1], 3, canvas, 'red', 'red', 'del')
            text = str(i) + '.' + str(center)
            canvas.create_text(500 + center[0] * 25 + 10, 500 - center[1] * 25 + 10, text=text,
                               fill='red', font=('Helvectica', '12'), tag='del')
            insert_answer(df, (center[0], center[1], round(radius, 2)))
            i += 1

    coordinates = tb_create(df)
    root = Tk()
    root.title('Таблица ответов')
    root.geometry('700x500')
    tb = Table(root, ('№', 'X', 'Y', 'RADIUS'), coordinates)
    tb.pack(expand=YES, fill=BOTH)



    print(df)



def dots_combinations(frame):
    x = []
    d = []
    length = len(frame) - 2
    for i in range(length):
        for j in range(length-i):
            for k in range(length-(j+i)):
                d.append((frame.loc[i, 'x'], frame.loc[i, 'y']))
                d.append((frame.loc[j+i+1, 'x'], frame.loc[j+i+1, 'y']))
                d.append((frame.loc[k+j+i+1+1, 'x'], frame.loc[k+j+i+1+1, 'y']))
                x.append(d)
                d = []
    return x


def len_of_line(dot1, dot2):  # нахождение длины отрезка
    return math.sqrt(math.pow(dot2[0] - dot1[0], 2) + math.pow(dot2[1] - dot1[1], 2))


def center_coordinates_find(dot1, dot2, dot3):
    cx = 0
    cy = 0
    a = dot2[0] - dot1[0]
    b = dot2[1] - dot1[1]
    c = dot3[0] - dot1[0]
    d = dot3[1] - dot1[1]
    e = a * (dot1[0] + dot2[0]) + b * (dot1[1] + dot2[1])
    f = c * (dot1[0] + dot3[0]) + d * (dot1[1] + dot3[1])
    g = 2 * (a * (dot3[1] - dot2[1]) - b * (dot3[0] - dot2[0]))
    if g != 0:
        cx = (d * e - b * f) / g
        cy = (a * f - c * e) / g

    return (cx, cy)

def belonging(dot1, dot2, dot3, aim):

    if (dot1[0] == dot2[0] == aim[0]) or (dot1[0] == dot3[0] == aim[0]) or (dot2[0] == dot3[0] == aim[0]):
        return 1

    if (dot1[1] == dot2[1] == aim[1]) or (dot1[1] == dot3[1] == aim[1]) or (dot2[1] == dot3[1] == aim[1]):
        return 1

    if ((aim[1] - dot1[1])/(dot2[1] - dot1[1])) == ((aim[0] - dot1[0])/(dot2[0] - dot1[0])):
        return 1

    if ((aim[1] - dot1[1])/(dot3[1] - dot1[1])) == ((aim[0] - dot1[0])/(dot3[0] - dot1[0])):
        return 1

    if ((aim[1] - dot2[1])/(dot3[1] - dot2[1])) == ((aim[0] - dot2[0])/(dot3[0] - dot2[0])):
        return 1
    return 0


def main():
    read()


if __name__ == '__main__':
    main()