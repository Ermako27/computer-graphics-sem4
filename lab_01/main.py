from tkinter import *
from interface_func import input_test, show_dots_window, insert_dot_window, delete_dot_window, change_dot_window
import pandas as pd

df_text = pd.read_csv('dots.csv', sep=',')
#print(df_text)

root = Tk()

root.title('Меню')
root.geometry('1500x1000')

canvas = Canvas(root, width=1000, height=1000, bg='#FFFFFF')

canvas.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
canvas.create_line(0, 500, 1000, 500, width=2, arrow=LAST)

text = -500
dy = 50
dx = 50
first_position_y = 1000
first_position_x = 1000
canvas.create_text(490, 490, text='0', fill='black', font=('Helvectica', '10'))

# создание делений на координатных осях
for i in range(20):
    canvas.create_line(495, first_position_y, 505, first_position_y, width=1, fill='black')
    canvas.create_line(first_position_x, 495, first_position_x, 505, width=1, fill='black')

    if text != 0:
        canvas.create_text(525, first_position_y, text=str(text), fill='black', font=('Helvectica', '10'))
        canvas.create_text(first_position_x, 535, text=str(-1*text), fill='black', font=('Helvectica', '10'))

    first_position_y -= dy
    first_position_x -= dx
    text += 50

# поля ввода файла
#bunch_label = Label(root, text='Введите имя файла')
#bunch_label.place(x=0, y=10)

#bunch_entry = Entry(root)
#bunch_entry.place(x=130, y=10)

# поля ввода вершин треугольника
v1_label = Label(root, text='Вершина 1')
v1_label.place(x=0, y=30)

v1_entry = Entry(root)
v1_entry.place(x=130, y=30)

v2_label = Label(root, text='Вершина 2')
v2_label.place(x=0, y=50)

v2_entry = Entry(root)
v2_entry.place(x=130, y=50)

v3_label = Label(root, text='Вершина 3')
v3_label.place(x=0, y=70)

v3_entry = Entry(root)
v3_entry.place(x=130, y=70)

# построение всех фигур
bunch_button = Button(root, text='Построить все точки и фигуры')
bunch_button.bind('<Button-1>', lambda event: input_test(v1_entry.get(),
                                                         v2_entry.get(),
                                                         v3_entry.get()))
bunch_button.place(x=10, y=100)

# вывод таблицы
table_button = Button(root, text='Показать таблицу координат')
table_button.bind('<Button-1>', lambda event: show_dots_window(df_text))
table_button.place(x=10, y=150)

# добавление новой точки
insert_button = Button(root, text='Добавить новую точку')
insert_button.bind('<Button-1>', lambda event: insert_dot_window(df_text))
insert_button.place(x=10, y=180)

# удаление точки
delete_button = Button(root, text='Удалить точку')
delete_button.bind('<Button-1>', lambda event: delete_dot_window(df_text))
delete_button.place(x=10, y=210)

# изменение координат точки
change_button = Button(root, text='Изменить точку точку')
change_button.bind('<Button-1>', lambda event: change_dot_window(df_text))
change_button.place(x=10, y=240)

canvas.pack(side='right')
root.mainloop()