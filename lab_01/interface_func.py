from tkinter import *
# from logic_func import file_read
import pandas as pd


# вывод окна с таблицей координат
def show_dots_window(frame):
    print(frame)
    root = Tk()
    root.title('Таблица координат')
    root.geometry('200x500')

    table = Label(root, text=str(frame.dropna()), font=("Helvetica", 28))
    table.place(x=0, y=50)
    root.mainloop()


# добавление новой точки в dataframe
def insert_dot(frame, coordinates):
    frame.loc[len(frame)] = coordinates.split()


def insert_dot_window(frame):
    root = Tk()
    root.title('Добавление новой точки')
    root.geometry('500x200')

    insert_label = Label(root, text='Введите координаты через пробел')
    insert_label.place(x=0, y=30)

    insert_entry = Entry(root)
    insert_entry.place(x=0, y=50)

    insert_button = Button(root, text='Добавить')
    insert_button.bind('<Button-1>', lambda event: insert_dot(frame, insert_entry.get()))
    insert_button.place(x=0, y=80)
    root.mainloop()


# удаление точки из dataframe
def delete_dot(frame, index):
    tmp = frame.loc[frame.index == 3]
    frame.loc[frame.index == index] = tmp


def delete_dot_window(frame):
    root = Tk()
    root.title('Удаление точки')
    root.geometry('500x200')

    delete_label = Label(root, text='Введите индекс точки')
    delete_label.place(x=0, y=30)

    delete_entry = Entry(root)
    delete_entry.place(x=0, y=50)

    delete_button = Button(root, text='Удалить')
    delete_button.bind('<Button-1>', lambda event: delete_dot(frame, int(delete_entry.get())))
    delete_button.place(x=0, y=80)
    root.mainloop()


# изменение координато точки
def change_dot(frame, index_and_coordinates):
    index, x, y = [int(i) for i in index_and_coordinates.split()]
    frame.loc[index, 'x'] = x
    frame.loc[index, 'y'] = y


def change_dot_window(frame):
    root = Tk()
    root.title('Изменение координат')
    root.geometry('500x200')

    change_label = Label(root, text='Введите номер и новые координаты точки')
    change_label.place(x=0, y=30)

    change_entry = Entry(root)
    change_entry.place(x=0, y=50)

    change_button = Button(root, text='Изменить')
    change_button.bind('<Button-1>', lambda event: change_dot(frame, change_entry.get()))
    change_button.place(x=0, y=80)
    root.mainloop()


def input_test(v1, v2, v3):
    print(v1, v2, v3)
