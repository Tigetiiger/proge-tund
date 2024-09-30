import turtle as t
import tkinter as tk
import random

varvi_list= [
    'blue',
    'green',
    'red',
    'cyan',
    'magenta',
    'yellow',
    'white'
]

def turtle_circle():
     t.pendown()
     t.speed(100)
     t.pensize(2)
     t.bgcolor('black')
     for i in range(100):
         for j in range(i):
            t.forward(2)
            t.left(40/i)
         t.color(random.choice(varvi_list))
     t.penup()





class joonistaja(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('lol see on joonistaja')
        self.geometry(f'{500}x{300}')
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.valik1 = tk.Button(self, text='varviline spiraal', command=turtle_circle)
        self.valik1.grid(column=0, row=0, sticky='nsew')
        self.valik2 = tk.Button(self, text='kujund2', command=self.turtel_kujund2)
        self.valik2.grid(column=1, row=0, sticky='nsew')
        self.valik3 = tk.Label(self, text='pane number:')
        self.valik3.grid(column=0, row=1, sticky='e')
        self.valik4 = tk.Entry(self)
        self.valik4.grid(column=1, row=1, sticky='w')
        self.mainloop()

    def turtel_kujund2(self):
        t.pendown()
        t.speed(100)
        t.pensize(2)
        t.bgcolor('black')
        for i in range(100):
            t.forward(i * 5)
            t.left((i % 3 + 3) * int(self.valik4.get()))
            t.color(random.choice(varvi_list))
        t.penup()


joonistaja()

