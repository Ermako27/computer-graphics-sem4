from tkinter import *
from math import cos, sin, radians,pi

def poly_oval(x0,y0, x1,y1):
    steps = 1000
    a = (x1 - x0) / 2.0
    b = (y1 - y0) / 2.0
    xc = x0 + a
    yc = y0 + b
    point_list = []
    for i in range(steps):
        theta = (pi * 2) * (float(i) / steps)
        x = a * cos(theta)
        y = b * sin(theta)
        point_list.append([round(x + xc),round(y + yc)])

    return point_list

def dublicate(mtr2):
    mtr1 = []
    for i in range(len(mtr2)):
        mtr1.append([])
        for j in range(len(mtr2[i])):
            mtr1[i].append(mtr2[i][j])
    return mtr1

point_list = []
previous_position = []
door = poly_oval(500,390,580,530)
door_frame1 = [[540,390],[540,530]]
door_frame2 = [[500,465],[580,465]]
door_frame3 = [[540,390],[500,465],[540,530],[580,465],[540,390]]
house = [[300,350],[300,550],[600,550],[600,350],[300,350], [450,260], [600,350]]
high_window = [[415,340],[485,340], [485,285],[415,285],[415,340]]
high_frame1 = [[450,340],[450,285]]
high_frame2 = [[415,314],[485,314]]
low_window = poly_oval(350,380,400,440)
low_frame1 = [[375,380],[375,440]]
low_frame2 = [[350,410],[400,410]]
door_center = [530,390,580,530]
low_window_center = [350,380,400,440]
start_position = [house, high_window, high_frame1, high_frame2, low_window, low_frame1,low_frame2, door, door_frame1, door_frame2, door_frame3]
point_list = dublicate(start_position)
previous_position = dublicate(start_position)

def Quit(event):
    global root
    root.destroy()

def Draw():
    canvas.delete("all")
    for figure in point_list:
        canvas.create_line(figure)

def MoveObj(event):
    dx = move_x.get()
    dy = move_y.get()
    try:
        dx = float(dx)
        dy = float(dy)
    except:
        errorMsg = "Неподходящие значения"
        error.configure(text=errorMsg, font='Arial 22',justify='left', anchor='w')
    else:
        global point_list, previous_position
        previous_position = dublicate(point_list)
        errorMsg = ""
        error.configure(text=errorMsg, font='Arial 22')
        for i in range(len(point_list)):
            new_points = []
            for point in point_list[i]:
                x1 = point[0] + dx
                y1 = point[1] + dy
                new_points.append([x1, y1])
            point_list[i] = new_points
        Draw()

def RotateObj(event):
    x = rotate_x.get()
    y = rotate_y.get()
    angle = rotate_angle.get()
    try:
        x = float(x)
        y = float(y)
        angle = float(angle)
    except:
        errorMsg = "Неподходящие значения"
        error.configure(text=errorMsg, font='Arial 22',justify='left', anchor='w')
    else:
        global point_list, previous_position
        previous_position = dublicate(point_list)
        errorMsg = ""
        error.configure(text=errorMsg, font='Arial 22')
        for i in range(len(point_list)):
            new_points = []
            for point in point_list[i]:
                x1 = x + (point[0] - x)*cos(radians(angle)) + (point[1] - y)*sin(radians(angle))
                y1 = y - (point[0] - x)*sin(radians(angle)) + (point[1] - y)*cos(radians(angle))
                new_points.append([x1,y1])
            point_list[i] = new_points
        Draw()

def ScaleObj(event):
    x = rotate_x.get()
    y = rotate_y.get()
    kx = scale_kx.get()
    ky = scale_ky.get()
    try:
        x = float(x)
        y = float(y)
        kx = float(kx)
        ky = float(ky)
    except:
        errorMsg = "Неподходящие значения"
        error.configure(text=errorMsg, font='Arial 22',justify='left', anchor='w')
    else:
        global point_list, previous_position
        previous_position = dublicate(point_list)
        errorMsg = ""
        error.configure(text=errorMsg, font='Arial 22')
        for i in range(len(point_list)):
            new_points = []
            for point in point_list[i]:
                x1 = kx*point[0] + (1 - kx)*x
                y1 = ky*point[1] + (1 - ky)*y
                new_points.append([x1,y1])
            point_list[i] = new_points
        Draw()

def BackPosition(event):
    global point_list, previous_position
    point_list, previous_position = previous_position, point_list
    Draw()

def StartPosition(event):
    global point_list, start_position
    point_list = []
    point_list = dublicate(start_position)
    Draw()

root = Tk()
root.geometry("1940x1080")
root.title("Лабораторная работа 2")

## Перемещение
move_x = Entry(root, bg='white', font='Arial 22')
move_x.place(x=50,y=60)
move_y = Entry(root, bg='white', font='Arial 22')
move_y.place(x=50,y=130)

lb = Label(root, text='Перемещение', font='Arial 22',  justify='left', anchor='w')
lb.place(x=60,y=10)
lb = Label(root, text='X', font='Arial 22')
lb.place(y=60)
lb = Label(root, text='Y', font='Arial 22')
lb.place(y=130)

moveBtn = Button(root, width=20, height=2,text="Перенести", font='Arial 22')
moveBtn.place(x=50, y=200)
moveBtn.bind('<Button-1>', MoveObj)

## Поворот
lb = Label(root, text='Центр поворота/масштабирования', font='Arial 22',  justify='left', anchor='w')
lb.place(x=50,y=280)
rotate_x = Entry(root, bg='white', font='Arial 22')
rotate_x.place(x=50,y=320)
rotate_y = Entry(root, bg='white', font='Arial 22')
rotate_y.place(x=50,y=390)
rotate_angle = Entry(root, bg='white', font='Arial 22')
rotate_angle.place(x=50,y=510)

lb = Label(root, text='Угол поворота', font='Arial 22',  justify='left', anchor='w')
lb.place(x=50,y=460)
lb = Label(root, text='X', font='Arial 22')
lb.place(y=320)
lb = Label(root, text='Y', font='Arial 22')
lb.place(y=390)

## Масштабирование
scale_kx = Entry(root, bg='white', font='Arial 22')
scale_kx.place(x=470,y=510)
scale_ky = Entry(root, bg='white', font='Arial 22')
scale_ky.place(x=470,y=560)


lb = Label(root, text='Масштабирование', font='Arial 22',  justify='left', anchor='w')
lb.place(x=400,y=460)
lb = Label(root, text='По X', font='Arial 22')
lb.place(x=400,y=510)
lb = Label(root, text='По Y', font='Arial 22')
lb.place(x=400,y=560)

scaleBtn = Button(root, width=20, height=2,text="Повернуть", font='Arial 22')
scaleBtn.place(x=50, y=630)
scaleBtn.bind('<Button-1>', RotateObj)
scaleBtn = Button(root, width=20, height=2,text="Масштабировать", font='Arial 22')
scaleBtn.place(x=430, y=630)
scaleBtn.bind('<Button-1>', ScaleObj)

backBtn = Button(root, width=20, height=2,text="Шаг назад", font='Arial 22')
backBtn.place(x=50, y=730)
backBtn.bind('<Button-1>', BackPosition)

initBtn = Button(root, width=20, height=2,text="Начальное состояние", font='Arial 22')
initBtn.place(x=50, y=830)
initBtn.bind('<Button-1>', StartPosition)

canvas = Canvas(root, width=900,height=900,bg='white')
canvas.place(relx=0.5,y=50)

quitBtn = Button(root, text="Завершение работы", width=20,height=2, font='Arial 22')
quitBtn.bind('<Button-1>', Quit)
quitBtn.place(relx=0.7, x=-50,rely=0.9, y=20)

## Ошибки
errorMsg = ''
lb = Label(root, text='Ошибки:', font='Arial 22')
lb.place(x=400,y=10)
error = Label(root, text=errorMsg, font='Arial 22', height=4,width=30)
error.place(x=400,y=60)

Draw()

root.mainloop()
