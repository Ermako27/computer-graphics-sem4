from tkinter import *
import pandas as pd
from interface_func import show_dots_window, insert_dot_window, delete_dot_window, change_dot_window, error_message
from logic_func import print_all_figures, print_solution

df_text = pd.read_csv('dots.csv', sep=',')

root = Tk()

root.title('Меню')
root.geometry('1500x1000')

canvas = Canvas(root, width=1000, height=1000, bg='#FFFFFF')


# создание самих координатных осей
canvas.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
canvas.create_line(0, 500, 1000, 500, width=2, arrow=LAST)


text = -20
dy = 10  # цена деления
dx = 10
first_position_y = 1000
first_position_x = 1000
canvas.create_text(490, 490, text='0', fill='black', font=('Helvectica', '10'))


# создание делений на координатных осях
for i in range(100):
    canvas.create_line(495, first_position_y, 505, first_position_y, width=1, fill='black')
    canvas.create_line(first_position_x, 495, first_position_x, 505, width=1, fill='black')

    # создание подписей под каждой меткой
    #if text != 0:
    #    canvas.create_text(525, first_position_y, text=str(text), fill='black', font=('Helvectica', '10'))
    #    canvas.create_text(first_position_x, 535, text=str(-1*text), fill='black', font=('Helvectica', '10'))

    first_position_y -= dy
    first_position_x -= dx
    text += 1


# поля ввода вершин треугольника

triangle_label = Label(root, text='Введите координаты вершин треугольника', font=('Helvectica', '12'))
triangle_label.place(x=0, y=10)

x_label = Label(root, text='X')
x_label.place(x=180, y=40)
y_label = Label(root, text='Y')
y_label.place(x=280, y=40)

v1_label = Label(root, text='Вершина 1')
v1_label.place(x=0, y=60)

v1_x_entry = Entry(root)
v1_x_entry.place(x=130, y=60, width=100)

v1_y_entry = Entry(root)
v1_y_entry.place(x=250, y=60, width=100)

v2_label = Label(root, text='Вершина 2')
v2_label.place(x=0, y=80)

v2_x_entry = Entry(root)
v2_x_entry.place(x=130, y=80, width=100)

v2_y_entry = Entry(root)
v2_y_entry.place(x=250, y=80, width=100)

v3_label = Label(root, text='Вершина 3')
v3_label.place(x=0, y=100)

v3_x_entry = Entry(root)
v3_x_entry.place(x=130, y=100, width=100)

v3_y_entry = Entry(root)
v3_y_entry.place(x=250, y=100, width=100)


# построение всех фигур
bunch_button = Button(root, text='Построить все точки и фигуры')
bunch_button.bind('<Button-1>', lambda event: print_all_figures(' '.join([v1_x_entry.get(), v1_y_entry.get()]),
                                                                ' '.join([v2_x_entry.get(), v2_y_entry.get()]),
                                                                ' '.join([v3_x_entry.get(), v3_y_entry.get()]),

                                                                df_text, canvas))
bunch_button.place(x=10, y=350)

# построение искомых окружностей
solution_button = Button(root, text='Построить искомые окружности')
solution_button.bind('<Button-1>', lambda event: print_solution(' '.join([v1_x_entry.get(), v1_y_entry.get()]),
                                                                ' '.join([v2_x_entry.get(), v2_y_entry.get()]),
                                                                ' '.join([v3_x_entry.get(), v3_y_entry.get()]),
                                                                df_text, canvas))
solution_button.place(x=250, y=350)

# вывод таблицы
table_button = Button(root, text='Показать таблицу координат')
table_button.bind('<Button-1>', lambda event: show_dots_window(df_text))
table_button.place(x=10, y=180, width=270)



# добавление новой точки
insert_amount = Entry(root)
insert_amount.place(x=290, y=210, width=100)
insert_button = Button(root, text='Добавить точки (введите их количесво)', command=lambda: insert_dot_window(df_text, int(insert_amount.get())))
insert_button.place(x=10, y=210, width=270)

# удаление точки
delete_amount = Entry(root)
delete_amount.place(x=290, y=240, width=100)
delete_button = Button(root, text='Удалить точки (введите их количесво)', command=lambda: delete_dot_window(df_text, int(delete_amount.get())))
delete_button.place(x=10, y=240, width=270)


# изменение координат точки
change_button = Button(root, text='Изменить точку')
change_button.bind('<Button-1>', lambda event: change_dot_window(df_text))
change_button.place(x=10, y=270, width=270)


task = 'На плоскости дано множество точек \n' \
       'и треугольник (задан вершинами). \n' \
       'Найти все окружности, каждая из которых проходит хотя бы \n' \
       'через 3 различные точки заданного множества, \n' \
       'у которых прямая, проходящая через 2 вершины треугольника \n' \
       'проходит и через центр окружности. \n' \
       'Среди найденных окружностей выбрать ту, для которой искомая прямая \n' \
       'образует минимальный угол с осью ординат.'


caption_label = Label(root, text='Условие задачи:', font=('Helvectica', '16'))
caption_label.place(x=0, y=460)

task_label = Label(root, text=task, font=('Helvectica', '9'))
task_label.place(x=0, y=490)

canvas.pack(side='right')
root.mainloop()
