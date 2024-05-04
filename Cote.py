from tkinter import *
from tkinter.colorchooser import *

def choose(inputic):
    global state, line_size
    if inputic == "plus":
        if line_size <= 98:
            line_size += 2
            size.configure(text=line_size)
        return
    elif inputic == "minus":
        if line_size >= 2:
            line_size -= 2
            size.configure(text=line_size)
        return
    state = inputic

def clear(event):
    canvas.create_rectangle(0, 0, 1000, 800, fill="white", outline="white")

def paint(event):
    if event.widget.__class__ is not Canvas:
        return
    if state == 'circle':
        canvas.create_oval(event.x - line_size, event.y - line_size, event.x + line_size, event.y + line_size, fill=color, outline=color)
    elif state == 'square':
        canvas.create_rectangle(event.x - line_size, event.y - line_size, event.x + line_size, event.y + line_size, fill=color, outline=color)
    elif state == 'line1':
        canvas.create_line(event.x - line_size, event.y - line_size, event.x + line_size, event.y + line_size, fill=color)
    elif state == 'line2':
        canvas.create_line(event.x + line_size, event.y - line_size, event.x - line_size, event.y + line_size, fill=color)

def rubber(event):
    if event.widget.__class__ is not Canvas:
        return
    canvas.create_oval(event.x - line_size, event.y - line_size, event.x + line_size, event.y + line_size, fill='white', outline="white")

def colorchooser1(event):
    global color
    if event.widget.__class__ is not Canvas:
        return
    colorchoos = askcolor(title="Выбери цвет")
    color = colorchoos[1]
    size.configure(fg=color)

state = 'circle'
line_size = 2
color = "black"

root = Tk()

root.geometry('1920x1080')

root.title('Рисовалка')

root['bg'] = 'gray75'

square_btn = Button(root, text="🟥", font=(None, 58), command=lambda: choose("square"))
square_btn.grid(row=0, column=1)
circle_btn = Button(root, text="🔴", font=(None, 58), command=lambda: choose("circle"))
circle_btn.grid(row=0, column=2)
line1_btn = Button(root, text="↘️", font=(None, 45), command=lambda: choose("line1"))
line1_btn.grid(row=0, column=3)
line2_btn = Button(root, text="↙️", font=(None, 45), command=lambda: choose("line2"))
line2_btn.grid(row=0, column=4)
plus_btn = Button(root, text="➕", font=(None, 52), command=lambda: choose("plus"))
plus_btn.grid(row=0, column=5)
minus_btn = Button(root, text="➖", font=(None, 52), command=lambda: choose("minus"))
minus_btn.grid(row=0, column=6)

canvas = Canvas(width=960, height=760, bg='white')
canvas.grid(row=0, column=0, rowspan=7)

size = Label(root, text=line_size, font=(None, 100), fg=color)
size.grid(row=6, column=1)

root.bind_all('<1>', paint)
root.bind_all('<B1-Motion>', paint)
root.bind_all('<3>', rubber)
root.bind_all('<B3-Motion>', rubber)
root.bind_all('<BackSpace>', clear)
root.bind_all('<2>', colorchooser1)

root.mainloop()
