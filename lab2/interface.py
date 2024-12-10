import tkinter as tk
from tkinter import filedialog
from tkinter import StringVar
import trains

train_frame, staff_frame, composition_frame = trains.build_initial_frames()


def build_frame():
    items = train_frame.display()
    if items:
        message = items
    else:
        message = "Вы не можете создать ни одно изделие."
    output.delete("1.0", tk.END)
    output.insert(tk.END, message)


def add_pers_frame():
    dol = input_dol.get()
    name = input_name.get()
    staj = input_staj.get()

    staff_frame.add_related_frame(dol, trains.Frame(dol))
    staff_frame.related_frames[dol].add_attribute("Имя", name)
    staff_frame.related_frames[dol].add_attribute("Стаж", staj)
    output.delete("1.0", tk.END)
    build_frame()

def add_sost_frame():
    vag = input_vag.get()
    typeb = input_type.get()
    vmest = input_vmest.get()

    composition_frame.add_related_frame(vag, trains.Frame(vag))
    composition_frame.related_frames[vag].add_attribute("Тип", typeb)
    composition_frame.related_frames[vag].add_attribute("Вместимость", vmest)
    output.delete("1.0", tk.END)
    build_frame()


win = tk.Tk()  # создаем окно

win.title('Фреймы')
win.geometry('1700x595+100+100')  # ?х? - размер окна, +?+? отступ от левой верхней точки
win.config(bg='#100d23')  # цвет фона

lable = tk.Label(win, text='Добавить в фрейм персонал',
                     bg='#100d23',
                     fg='#0aefc8',
                     font=('Consolas')
                     ).grid(row=1, column=1)

lable_dol = tk.Label(win, text='Введите должность:',
                     bg='#100d23',
                     fg='#0aefc8',
                     font=('Consolas')
                     ).grid(row=2, column=1)

input_dol = tk.Entry(win,
                     font=('Consolas'),
                     bg='#161329',
                     fg='#0aefc8', )
input_dol.grid(row=2, column=2)

lable_name = tk.Label(win, text='Введите имя:',
                      bg='#100d23',
                      fg='#0aefc8',
                      font=('Consolas')
                      ).grid(row=3, column=1)

input_name = tk.Entry(win,
                      width=5,
                      font=('Consolas'),
                      bg='#161329',
                      fg='#0aefc8', )
input_name.grid(row=3, column=2)

lable_staj = tk.Label(win, text='Введите стаж',
                      bg='#100d23',
                      fg='#0aefc8',
                      font=('Consolas')
                      ).grid(row=4, column=1)

input_staj = tk.Entry(win,
                      width=5,
                      font=('Consolas'),
                      bg='#161329',
                      fg='#0aefc8', )
input_staj.grid(row=4, column=2)

btn_add = tk.Button(win, text='добавить фрейм персонала',
                    fg='#100d23',
                    bg='#0aefc8',
                    font=('Consolas'),
                    activebackground='#c592ff',
                    command=add_pers_frame
                    ).grid(row=5, column=1)

btn_build = tk.Button(win, text='построить фреймы',
                      fg='#100d23',
                      bg='#0aefc8',
                      font=('Consolas'),
                      activebackground='#c592ff',
                      command=build_frame
                      ).grid(row=0, column=1)

lablegg = tk.Label(win, text='Добавить в фрейм состав',
                     bg='#100d23',
                     fg='#0aefc8',
                     font=('Consolas')
                     ).grid(row=1, column=3)

lable_vag = tk.Label(win, text='Введите вагон:',
                     bg='#100d23',
                     fg='#0aefc8',
                     font=('Consolas')
                     ).grid(row=2, column=3)

input_vag = tk.Entry(win,
                     font=('Consolas'),
                     bg='#161329',
                     fg='#0aefc8', )
input_vag.grid(row=2, column=4)

lable_type = tk.Label(win, text='Введите тип:',
                      bg='#100d23',
                      fg='#0aefc8',
                      font=('Consolas')
                      ).grid(row=3, column=3)

input_type = tk.Entry(win,
                      width=5,
                      font=('Consolas'),
                      bg='#161329',
                      fg='#0aefc8', )
input_type.grid(row=3, column=4)

lable_vmest = tk.Label(win, text='Введите вместимость',
                      bg='#100d23',
                      fg='#0aefc8',
                      font=('Consolas')
                      ).grid(row=4, column=3)

input_vmest = tk.Entry(win,
                      width=5,
                      font=('Consolas'),
                      bg='#161329',
                      fg='#0aefc8', )
input_vmest.grid(row=4, column=4)

btn_add = tk.Button(win, text='добавить в фрейм состава',
                    fg='#100d23',
                    bg='#0aefc8',
                    font=('Consolas'),
                    activebackground='#c592ff',
                    command=add_sost_frame
                    ).grid(row=5, column=3)

output = tk.Text(win,
                 width=63,
                 height=28,
                 wrap="word",
                 bg='#161329',
                 fg='#0aefc8', )
output.grid(row=0, column=0, rowspan=6,)

win.mainloop()  # запускаем окно
