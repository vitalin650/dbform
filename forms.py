# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:18:18 2022

@author: Vasil
"""
from functools import partial  # TODO: replace lambda(s)

import tkinter as tk
from tkinter import ttk

from students_models import create


def clear_inputs(entries_tuple):
    for entry in entries_tuple:
        entry.delete(0, tk.END)
    print("Очистка полів")


def add_student_to_DB(name, nick):
    create('students', ['student_full_name', 'latin_nickname'], (name.get(), nick.get()))
    print("Додано студента в базу")

def add_hobby_start_to_DB(student_id, hobby_id, start_date):
    create('hobby_starts', ['student_id', 'hobby_id', 'start_date'], (student_id.get(), hobby_id.get(), start_date.get()))
    print("Додано студента в базу")


def f_add_student():
    """Show form for student adding."""
    root_frame = tk.Tk()

    root_frame.minsize(420, 120)
    root_frame.title('Додати студента:')

    lbl_fullname = ttk.Label(root_frame, text='ПІБ',  font=("Arial", 12))
    lbl_fullname.grid(row=0, column=0, sticky=tk.W, padx=12)
    ent_fullname = ttk.Entry(root_frame, width=30)
    ent_fullname.grid(row=0, column=1, pady=2, padx=20)

    lbl_nickname = ttk.Label(root_frame, text='Прізвисько латиницею',  font=("Arial", 12))
    lbl_nickname.grid(row=1, column=0, sticky=tk.W, padx=12)
    ent_nickname = ttk.Entry(root_frame, width=30)
    ent_nickname.grid(row=1, column=1, pady=2, padx=20)

    submit_btn = ttk.Button(
        root_frame,
        text='Додати поля до бази',
        command=partial(add_student_to_DB, ent_fullname, ent_nickname)
    )
    submit_btn.grid(row=2, column=0, pady=10, padx=10, ipadx=40)

    clear_btn = ttk.Button(
        root_frame, text='Очистити всі поля',
        command=partial(clear_inputs, (ent_fullname, ent_nickname))
    )
    clear_btn.grid(row=2, column=1, pady=10, padx=10, ipadx=40)

    root_frame.mainloop()


def f_add_hobby():
    root_frame = tk.Tk()

    root_frame.minsize(420, 100)
    root_frame.title('Додати хобі:')

    lbl_hobby = ttk.Label(root_frame, text='Хобі',  font=("Arial", 12))
    lbl_hobby.grid(row=0, column=0, sticky=tk.W, padx=12)
    ent_hobby = ttk.Entry(root_frame, width=30)
    ent_hobby.grid(row=0, column=1, pady=2, padx=20)

    submit_btn = ttk.Button(
        root_frame, text='Додати поля до бази',
        command=partial(add_hobby_to_DB, ent_hobby)
    )
    submit_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=40)

    clear_btn = ttk.Button(
        root_frame, text='Очистити всі поля',
        command=partial(clear_inputs, (ent_hobby, ))
    )
    clear_btn.grid(row=1, column=1, pady=10, padx=10, ipadx=40)

    root_frame.mainloop()


def add_hobby_to_DB(hobby_name):
    create('hobbies', ['hobbies_name', ], (hobby_name.get(), ))
    print("Додано хобі в базу")


def f_create_hobby():
    root_frame = tk.Tk()

    root_frame.minsize(420, 100)
    root_frame.title('Додати початок хобі:')

    lbl_student_id = ttk.Label(root_frame, text='Cтуд ІД',  font=("Arial", 12))
    lbl_student_id.grid(row=0, column=0, padx=12)
    
    ent_student_id = ttk.Entry(root_frame, width=30)
    ent_student_id.grid(row=0, column=1, pady=2, padx=20)

    lbl_hobby_id = ttk.Label(root_frame, text='Хобі ІД',  font=("Arial", 12))
    lbl_hobby_id.grid(row=0, column=2, sticky=tk.W, padx=12)
    ent_hobby_id = ttk.Entry(root_frame, width=30)
    ent_hobby_id.grid(row=0, column=3, pady=2, padx=20)
    lbl_start_date = ttk.Label(root_frame, text='Дата',  font=("Arial", 12))
    lbl_start_date.grid(row=0, column=4, sticky=tk.W, padx=12)
    ent_start_date = ttk.Entry(root_frame, width=30)
    ent_start_date.grid(row=0, column=5, pady=2, padx=20)

    submit_btn = ttk.Button(
        root_frame, text='Додати поля до бази',
        command=partial(add_hobby_start_to_DB, ent_student_id, ent_hobby_id, ent_start_date)
    )
    submit_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=40)

    clear_btn = ttk.Button(
        root_frame, text='Очистити всі поля',
        command=partial(clear_inputs, (ent_student_id, ent_hobby_id, ent_start_date ))
    )
    clear_btn.grid(row=1, column=1, pady=10, padx=10, ipadx=40)

    root_frame.mainloop()


def f_delete_hobby():
    ...


