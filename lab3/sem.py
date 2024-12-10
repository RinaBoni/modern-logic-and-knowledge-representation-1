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
    plt.clf()
    # Визуализируем граф
    pos = nx.spring_layout(G)  # Определяем расположение узлов
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_color='black',
            font_weight='bold', arrows=True)
    plt.title("Семантическая сеть")
    plt.show()


def add_node():
    output.delete("1.0", tk.END)
    node = input_node.get()
    old_to_new = input_old_to_new.get()
    new_to_old = input_new_to_old.get()
    message = ''
    if node:
        if G.has_node(node):
            message += 'такой узел уже есть:'.join(node) + '\n'
        else:
            G.add_node(node)
    else:
        message += 'введите название узла' + '\n'

    if old_to_new:
        if G.has_node(old_to_new):
            G.add_edge(old_to_new, node)
        else:
            message += 'такого узла нет:'.join(old_to_new) + '\n'
    else:
        message += 'введите нужный вам узел(ребро от старого к новому)' + '\n'
    if new_to_old:
        if G.has_node(new_to_old):
            G.add_edge(node, new_to_old)
        else:
            message += 'такого узла нет'.join(new_to_old) + '\n'
    else:
        message += 'введите нужный вам узел(ребро от нового к старому)' + '\n'
    output.insert(tk.END, message)


win = tk.Tk()  # создаем окно

win.title('Фреймы')
win.geometry('1075x595+100+100')  # ?х? - размер окна, +?+? отступ от левой верхней точки
win.config(bg='#100d23')  # цвет фона

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
                      ).grid(row=1, column=0)

lable_node = tk.Label(win, text='введите название узла',
                      bg='#100d23',
                      fg='#0aefc8',
                      font=('Consolas')
                      ).grid(row=2, column=0)

input_node = tk.Entry(win,

                      font=('Consolas'),
                      bg='#161329',
                      fg='#0aefc8', )
input_node.grid(row=2, column=1)

lable_old_to_new = tk.Label(win, text='соединить с (стралка от существеющего к новому)',
                            bg='#100d23',
                            fg='#0aefc8',
                            font=('Consolas')
                            ).grid(row=3, column=0)

input_old_to_new = tk.Entry(win,

                            font=('Consolas'),
                            bg='#161329',
                            fg='#0aefc8', )
input_old_to_new.grid(row=3, column=1)

new_to_old = tk.Label(win, text='соединить с (стралка от нового к существующему)',
                   bg='#100d23',
                   fg='#0aefc8',
                   font=('Consolas')
                   ).grid(row=4, column=0)

input_new_to_old = tk.Entry(win,

                         font=('Consolas'),
                         bg='#161329',
                         fg='#0aefc8', )
input_new_to_old.grid(row=4, column=1)

btn_refresh = tk.Button(win, text='обновить семантическую сеть',
                        fg='#100d23',
                        bg='#0aefc8',
                        font=('Consolas'),
                        activebackground='#c592ff',
                        command=add_node
                        ).grid(row=5, column=0)

output = tk.Text(win,
                width=50,
                # height=28,
                wrap="word",
                bg='#161329',
                fg='#0aefc8',)
output.grid(row=0, column=3, rowspan=6,)

win.mainloop()  # запускаем окно
