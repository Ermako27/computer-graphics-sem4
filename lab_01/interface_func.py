from tkinter import *
from logic_func import file_read

def bunch():
    root = Tk()
    root.title('Ввод множества')
    root.geometry('500x500')

    # заголовок окна
    label_bunch = Label(root, text='Ввод координат точек из множества производится из файла')
    label_bunch.place(x=0, y=10)

    # ввод файла
    input_invite = Label(root, text='Введите название файла')
    input_invite.place(x=0, y=40)

    bunch_file_entry = Entry(root)
    bunch_file_entry.place(x=180, y=40)

    k = bunch_file_entry.get()
     print(k)

    bunch_button = Button(root, text='Создать')
    bunch_button.bind('<Button-1>', lambda event: file_read(str(bunch_file_entry.get())))
    bunch_button.place(x=10, y=100)


    root.mainloop()
