import tkinter as tk
from tkinter import filedialog
from tkinter import StringVar
import jewerly



def  calculate():
    time = int(input_time.get())
    thick_wire = int(input_thick_wire.get())
    thin_wire = int(input_thin_wire.get())
    output.delete("1.0", tk.END)
    
    maker = jewerly.JewelryMaker()
    items = maker.can_make_items(time, thick_wire, thin_wire)
    
    if items:
        message = "Вы можете создать следующие изделия: " + " или ".join(items)
    else:
        message = "Вы не можете создать ни одно изделие."
    output.insert(tk.END, message )

def get_requirements():
    item_name= var.get()
    maker = jewerly.JewelryMaker()
    requirements = maker.get_item_requirements(item_name)
    output_requirements.delete("1.0", tk.END)
    
    if requirements:
        message = f"Для создания {item_name} потребуется:\n"
        message += f"- Время: {requirements['time']} минут\n"
        message += f"- Толстая проволока: {requirements['thick_wire']} сантиметров\n"
        message += f"- Тонкая проволока: {requirements['thin_wire']} сантиметров"
    else:
        message = "Изделие не найдено. Пожалуйста, выберите кольцо, подвеску или браслет."

    # Вставляем сообщение в текстовое поле
    output_requirements.insert(tk.END, message)



win = tk.Tk()   #создаем окно

win.title('Лексический анализатор')
win.geometry('1075x595+100+100') #?х? - размер окна, +?+? отступ от левой верхней точки
win.config(bg='#100d23')    #цвет фона



lable_time = tk.Label(win, text='Введите время (минуты):', 
                bg='#100d23',
                fg='#0aefc8',
                font=('Consolas')
                ).grid(row=0, column=0)

input_time = tk.Entry(win, 
                width=5, 
                font=('Consolas'),
                bg='#161329',
                fg='#0aefc8',)
input_time.grid(row=0, column=1)

lable_thick_wire = tk.Label(win, text='Введите длину толстой проволоки (см):', 
                bg='#100d23',
                fg='#0aefc8',
                font=('Consolas')
                ).grid(row=1, column=0)

input_thick_wire = tk.Entry(win, 
                width=5, 
                font=('Consolas'),
                bg='#161329',
                fg='#0aefc8',)
input_thick_wire.grid(row=1, column=1)

lable_thin_wire = tk.Label(win, text='Введите длину тонкой проволоки (см):', 
                bg='#100d23',
                fg='#0aefc8',
                font=('Consolas')
                ).grid(row=2, column=0)

input_thin_wire = tk.Entry(win, 
                width=5, 
                font=('Consolas'),
                bg='#161329',
                fg='#0aefc8',)
input_thin_wire.grid(row=2, column=1)

btn_calculate = tk.Button(win, text='Обработать',
                fg='#100d23',
                bg='#0aefc8',
                font=('Consolas'),
                activebackground='#c592ff',
                command=calculate
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