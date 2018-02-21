from tkinter import *
import tkinter.ttk as ttk
# from logic_func import file_read
import pandas as pd


df = pd.read_csv('dots.csv', sep=',')


def table_create(frame):
    coordinates = []
    for row in frame.dropna().itertuples():
        coordinates.append((row[0], row[1], row[2]))
    return coordinates


class Table(Frame):
    def __init__(self, parent=None, headings=tuple(), data_set=list()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings

        # read_points(rows, data_set)

        for head in headings:
            table.heading(head, text=head, anchor=CENTER)
            table.column(head, anchor=CENTER)

        for row in data_set:
            table.insert('', END, values=row)

        scrolltable = Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=RIGHT, fill=Y)
        table.pack(expand=YES, fill=BOTH)


# вывод окна с таблицей координат

def show_dots_window(frame):
    coordinates = table_create(frame)
    root = Tk()
    root.title('Таблица координат')
    root.geometry('700x500')
    tb = Table(root, ('№', 'X', 'Y'), coordinates)
    tb.pack(expand=YES, fill=BOTH)


    #table = Label(root, text=str(frame.dropna()), font=("Helvetica", 28))
    #table.place(x=0, y=50)


# добавление новой точки в dataframe
def insert_dot(frame, coordinates):
    frame.loc[len(frame)] = [int(i) for i in coordinates.split()]


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


def main():
    pass


if __name__ == '__main__':
    main()