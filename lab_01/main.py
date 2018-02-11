from tkinter import *
from interface_func import bunch

root = Tk()

root.title('Меню')
root.geometry('1300x1000')

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


bunch_button = Button(root, text='Ввод множества')
bunch_button.bind('<Button-1>', lambda event: bunch())
bunch_button.place(x=10, y=100)


canvas.pack(side='right')
root.mainloop()