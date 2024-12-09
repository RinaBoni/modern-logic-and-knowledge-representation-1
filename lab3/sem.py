import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import StringVar

# def create_semantic_network():
    # Создаем направленный граф
G = nx.DiGraph()

# Добавляем узлы (понятия)
G.add_node("Собака")
G.add_node("Кошка")
G.add_node("Млекопитающее")
G.add_node("Домашнее животное")
G.add_node("Животное")

# Добавляем связи (отношения)
G.add_edge("Собака", "Млекопитающее")
G.add_edge("Кошка", "Млекопитающее")
G.add_edge("Собака", "Домашнее животное")
G.add_edge("Кошка", "Домашнее животное")
G.add_edge("Млекопитающее", "Животное")
    
    # return G

def build_semantic_network():

    # Визуализируем граф
    pos = nx.spring_layout(G)  # Определяем расположение узлов
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', arrows=True)
    plt.title("Семантическая сеть")
    plt.show()


def add_node():
    node = input_staj.get()
    G.add_node(node)
    edge = input_lable_f.get()
    G.add_edge(edge, node)
    
    
win = tk.Tk()   #создаем окно

win.title('Фреймы')
win.geometry('1075x595+100+100') #?х? - размер окна, +?+? отступ от левой верхней точки
win.config(bg='#100d23')    #цвет фона



btn_build = tk.Button(win, text='построить базовую семантическую сеть',
                fg='#100d23',
                bg='#0aefc8',
                font=('Consolas'),
                activebackground='#c592ff',
                command=build_semantic_network
                ).grid(row=0, column=0)

lable_name = tk.Label(win, text='добавить узел', 
                bg='#100d23',
                fg='#0aefc8',
                font=('Consolas')
                ).grid(row=0, column=1)

lable_staj = tk.Label(win, text='введите название узла', 
                bg='#100d23',
                fg='#0aefc8',
                font=('Consolas')
                ).grid(row=1, column=2)

input_staj = tk.Entry(win, 
                width=5, 
                font=('Consolas'),
                bg='#161329',
                fg='#0aefc8',)
input_staj.grid(row=1, column=3)

lable_f = tk.Label(win, text='соединить этот узел с ', 
                bg='#100d23',
                fg='#0aefc8',
                font=('Consolas')
                ).grid(row=2, column=2)

input_lable_f = tk.Entry(win, 
                width=5, 
                font=('Consolas'),
                bg='#161329',
                fg='#0aefc8',)
input_lable_f.grid(row=2, column=3)


btn_refresh = tk.Button(win, text='обновить семантическую сеть',
                fg='#100d23',
                bg='#0aefc8',
                font=('Consolas'),
                activebackground='#c592ff',
                command=add_node
                ).grid(row=1, column=0)








win.mainloop()  #запускаем окно