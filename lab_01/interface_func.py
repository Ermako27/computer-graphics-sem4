from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
# from logic_func import file_read
import pandas as pd


def error_message(message):
    messagebox.showerror("Error", message)


def table_create(frame):
    coordinates = []
    for row in frame.dropna().itertuples():
        coordinates.append((row[0], float(row[1]), float(row[2])))
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
def insert_dot(frame, x, y, insert_amount):

    for i in range(insert_amount):

        insert_x = float(x[i].get())
        insert_y = float(y[i].get())
        frame.loc[len(frame)] = [insert_x, insert_y]

"""

       if float(x[i].get()) // 10 == 0:
            insert_x = int(x[i].get())
        else:
            insert_x = float(x[i].get())

        print(y[i].get())
        if float(y[i].get()) // 10 == 0:
            print('!')
            insert_y = int(y[i].get())
        else:
            print('%')
            insert_y = float(y[i].get())
"""




def insert_dot_window(frame, insert_amount):

    root = Tk()
    root.title('Добавление точек')
    root.geometry('250x'+str(insert_amount*100))
    dots_x = []
    dots_y = []
    x_label = Label(root, text='X', font=('Helvectica', '16'))
    x_label.place(x=50, y=10)

    y_label = Label(root, text='Y', font=('Helvectica', '16'))
    y_label.place(x=160, y=10)
    for i in range(insert_amount):
        dots_x.append(Entry(root))
        dots_y.append(Entry(root))
        dots_x[i].place(x=10, y=40*(i+1), width=100)
        dots_y[i].place(x=120, y=40*(i+1), width=100)

    insert_button = Button(root, text='Добавить', command=lambda: insert_dot(frame, dots_x, dots_y, insert_amount))
    insert_button.pack(side=BOTTOM)

    root.mainloop()


# удаление точки из dataframe
def delete_dot(frame, ind, delete_amount):
    tmp = frame.loc[frame.index == 3]
    for i in range(delete_amount):
        frame.loc[frame.index == int(ind[i].get())] = tmp


def delete_dot_window(frame, delete_amount):
    root = Tk()
    root.title('Удаление точки')
    root.geometry('250x'+str(delete_amount*100))
    ind = []
    delete_label = Label(root, text='Введите индексы точек')
    delete_label.place(x=0, y=10)

    for i in range(delete_amount):
        ind.append(Entry(root))
        ind[i].place(x=10, y=40*(i+1), width=100)

    delete_button = Button(root, text='Удалить', command=lambda: delete_dot(frame, ind, delete_amount))
    delete_button.pack(side=BOTTOM)
    root.mainloop()


# изменение координато точки
def change_dot(frame, index, x, y):
    x = float(x)
    y = float(y)
    frame.loc[index, 'x'] = x
    frame.loc[index, 'y'] = y


def change_dot_window(frame):
    root = Tk()
    root.title('Изменение координат')
    root.geometry('700x300')

    change_label = Label(root, text='Введите номер изменяемой точки и её новые координаты', font=('Helvectica', '16'))
    change_label.place(x=0, y=10)

    index_label = Label(root, text='№ точки')
    index_label.place(x=0, y=50)

    index_entry = Entry(root)
    index_entry.place(x=0, y=70, width=100)

    x_label = Label(root, text='X')
    x_label.place(x=140, y=50)

    x_entry = Entry(root)
    x_entry.place(x=120, y=70, width=100)

    y_label = Label(root, text='Y')
    y_label.place(x=260, y=50)

    y_entry = Entry(root)
    y_entry.place(x=240, y=70, width=100)

    change_button = Button(root, text='Изменить', command=lambda: change_dot(frame, int(index_entry.get()),
                                                                             x_entry.get(),
                                                                             y_entry.get()))
    change_button.place(x=0, y=100)
    root.mainloop()


def input_test(v1, v2, v3):
    print(v1, v2, v3)


def main():
    pass


if __name__ == '__main__':
    main()
