import tkinter as tk
from tkinter import filedialog
from tkinter import StringVar
import trains

train_frame, staff_frame, composition_frame = trains.build_initial_frames()

def  build_frame():
    
   
    
    items = train_frame.display()
    # items = staff_frame.display()
    # print(items)
    
    
    if items:
        message = items
        # message = "Вы можете создать следующие изделия: " + " или ".join(items)
    else:
        message = "Вы не можете создать ни одно изделие."
    output.delete("1.0", tk.END)
    output.insert(tk.END, message )

def add_pers_frame():
    dol = input_dol.get()
    name = input_name.get()
    staj = input_staj.get()
    
    staff_frame.add_related_frame(dol, trains.Frame(dol))
    staff_frame.related_frames[dol].add_attribute("Имя", name)
    staff_frame.related_frames[dol].add_attribute("Стаж", staj)
    output.delete("1.0", tk.END)
    build_frame()

    
def get_requirements():


    # Вставляем сообщение в текстовое поле
    output_requirements.insert(tk.END)



win = tk.Tk()   #создаем окно

win.title('Фреймы')
win.geometry('1075x595+100+100') #?х? - размер окна, +?+? отступ от левой верхней точки
win.config(bg='#100d23')    #цвет фона

lable_dol = tk.Label(win, text='Введите должность:', 
                bg='#100d23',
                fg='#0aefc8',
                font=('Consolas')
                ).grid(row=4, column=0)

# input_dol = tk.Entry(win, 
#                 width=5, 
#                 font=('Consolas'),
#                 bg='#161329',
#                 fg='#0aefc8',)
# input_dol.grid(row=4, column=1)

lable_name = tk.Label(win, text='Введите имя:', 
                bg='#100d23',
                fg='#0aefc8',
                font=('Consolas')
                ).grid(row=0, column=0)

input_name = tk.Entry(win, 
                width=5, 
                font=('Consolas'),
                bg='#161329',
                fg='#0aefc8',)
input_name.grid(row=0, column=1)

lable_staj = tk.Label(win, text='Введите стаж', 
                bg='#100d23',
                fg='#0aefc8',
                font=('Consolas')
                ).grid(row=1, column=0)

input_staj = tk.Entry(win, 
                width=5, 
                font=('Consolas'),
                bg='#161329',
                fg='#0aefc8',)
input_staj.grid(row=1, column=1)

btn_add = tk.Button(win, text='добавить фрейм персонала',
                fg='#100d23',
                bg='#0aefc8',
                font=('Consolas'),
                activebackground='#c592ff',
                command=add_pers_frame
                ).grid(row=2, column=0)

# lable_thin_wire = tk.Label(win, text='Введите длину тонкой проволоки (см):', 
#                 bg='#100d23',
#                 fg='#0aefc8',
#                 font=('Consolas')
#                 ).grid(row=2, column=0)

input_dol = tk.Entry(win, 
                width=5, 
                font=('Consolas'),
                bg='#161329',
                fg='#0aefc8',)
input_dol.grid(row=2, column=1)

btn_build = tk.Button(win, text='построить фреймы',
                fg='#100d23',
                bg='#0aefc8',
                font=('Consolas'),
                activebackground='#c592ff',
                command=build_frame
                ).grid(row=3, column=0)

output = tk.Text(win, 
                width=63, 
                height=28,
                wrap="word",
                bg='#161329',
                fg='#0aefc8',)
output.grid(row=4, column=0)




lable_item = tk.Label(win, text='Какое изделие вы хотите сделать?', 
                bg='#100d23',
                fg='#0aefc8',
                font=('Consolas')
                ).grid(row=0, column=3)

var = tk.StringVar(value="")
radio_ring = tk.Radiobutton(win, text="Кольцо",
                variable=var,
                value="кольцо",
                bg='#100d23',
                fg='#0aefc8',
                command=get_requirements)
radio_ring.grid(row=1, column=3, padx=10, pady=5)

radio_pendant = tk.Radiobutton(win, text="Подвеска",
                variable=var,
                value="подвеска",
                bg='#100d23',
                fg='#0aefc8',
                command=get_requirements)
radio_pendant.grid(row=2, column=3, padx=10, pady=5)

radio_bracelet = tk.Radiobutton(win, text="Браслет",
                variable=var,
                value="браслет",
                bg='#100d23',
                fg='#0aefc8',
                command=get_requirements)
radio_bracelet.grid(row=3, column=3, padx=10, pady=5)

output_requirements = tk.Text(win, 
                width=63, 
                height=28,
                wrap="word",
                bg='#161329',
                fg='#0aefc8',)
output_requirements.grid(row=4, column=3)




win.mainloop()  #запускаем окно