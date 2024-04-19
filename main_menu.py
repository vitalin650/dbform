# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:02:37 2022

@author: Vasil
"""
from functools import partial  # TODO: replace lambda(s)

import tkinter as tk
from tkinter import ttk

from students_models import (
    table_creations,
    create, read, update, delete,
)

from forms import (
    f_add_student,  f_add_hobby,
    f_create_hobby, f_delete_hobby
)

state_params = dict(statusbar=None)

if __name__ == '__main__':
    root = tk.Tk()

    root.minsize(600, 300)
    root.title('PostMan')
    root.option_add("*Font", 'Verdana 14')

    mainframe = ttk.Frame(root, padding="2 5 2 2")
    mainframe.pack(side=tk.BOTTOM, fill=tk.X)

    mainmenu = tk.Menu(mainframe)
    mainmenu.option_add("*Font", 'Verdana 14')
    root.config(menu=mainmenu)

    handbook_menu = tk.Menu(mainmenu, tearoff=0)
    handbook_menu.add_command(label="Студенти", command=f_add_student)
    handbook_menu.add_command(label="Хоббі", command=f_add_hobby)

    create_menu = tk.Menu(mainmenu, tearoff=0)
    create_menu.add_command(label="... додати початок хоббі",
                            command=f_create_hobby)
    create_menu.add_command(
        label="... видалити початок хоббі",
        command=f_delete_hobby)

    export_menu = tk.Menu(mainmenu, tearoff=0)
    export_menu.add_command(label="... таблиця хобі")

    editing_menu = tk.Menu(mainmenu, tearoff=0)
    editing_menu.add_command(label="... студент")
    editing_menu.add_command(label="... хобі")

    create_tickets_menu = tk.Menu(mainmenu, tearoff=0)
    create_tickets_menu.add_command(label="... таблиця хобі",  command=f_create_hobby)

    exit_menu = tk.Menu(mainmenu, tearoff=0)
    # .quit - close frame - do not stop root
    exit_menu.add_command(label="Закрити програму", command=root.destroy)  # root.quit

    mainmenu.add_cascade(label="Довідники", menu=handbook_menu)
    mainmenu.add_cascade(label="Створити", menu=create_menu)
    mainmenu.add_cascade(label="Правка", menu=editing_menu)
    mainmenu.add_cascade(label="Експорт даних", menu=export_menu)
    mainmenu.add_cascade(label="Вихід", menu=exit_menu)

    # mainmenu.entryconfigure("Експорт даних", state=tk.DISABLED)

    var_lbl_statusbar = tk.StringVar()
    var_lbl_statusbar.set("Тут будуть підказки…")

    lbl_statusbar = ttk.Label(mainframe, text="Тут будуть підказки…",
                              relief=tk.SUNKEN, anchor=tk.W,
                              textvariable=var_lbl_statusbar,
                              # style=,
                              )  # bd=1,
    state_params['statusbar'] = var_lbl_statusbar
    lbl_statusbar.pack(side=tk.BOTTOM, padx=1, pady=1, fill=tk.X)

    root.mainloop()
