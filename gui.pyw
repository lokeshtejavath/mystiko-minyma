# -*- coding: utf-8 -*-

import tkinter
from tkinter import filedialog, ttk
from tkinter.constants import LEFT, RIGHT

import insert
import randstring
import retrive

root = tkinter.Tk()
root.geometry("700x350")
root.title("Mystiko-Minyma")
s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#b9bcfc")
s.configure('TNotebook.Tab', padding=[25, 3])
s.map("TNotebook.Tab", background=[("selected", "#8388fa")])
tabControl = ttk.Notebook(root)

rootHeight = root.winfo_height()
rootWidth = root.winfo_width()
tell = ttk.Frame(tabControl)
tell.pack()
listen = ttk.Frame(tabControl)
listen.pack()
"""akoúo légo"""

fileName = None


def open_file():
    file = filedialog.askopenfilename(filetypes=[("Image Files", ("*.jpeg", "*png", "*.jpg"))])
    if file != None:
        global fileName
        fileName = file


message_var = tkinter.StringVar()
key_var = tkinter.StringVar()
ran_var = tkinter.StringVar()


def copyToKeyboard(strin: str):
    root.clipboard_clear()
    root.clipboard_append(strin)
    root.update()


xpad = 30
ypad = 20


def telling():
    mess = message_var.get()
    key = randstring.randstring()
    basekey = key_var.get()
    i = insert.Inserter()
    savenanme = filedialog.asksaveasfile(mode="w", defaultextension=[("PNG", "*.png")], filetypes=[("PNG", "*.png")])
    i.insert(mess, key, fileName, savenanme.name, basekey)
    ttk.Label(tell, text="Oursecrect", justify=LEFT).grid(column=0, row=4, padx=0)
    copy = ttk.Button(tell, text=key, command=lambda: copyToKeyboard(key)).grid(column=1, row=4, padx=xpad, pady=ypad)


def listening():
    ran = ran_var.get()
    basekey = key_var.get()
    r = retrive.Retrive()
    mess = r.retriver(ran, fileName, basekey)
    ttk.Label(listen, text="Our not so little secrect", justify=LEFT).grid(column=0, row=4, padx=0)
    copy = ttk.Button(listen, text=mess, command=lambda: copyToKeyboard(mess)).grid(column=1, row=4, padx=xpad, pady=ypad)


tabControl.add(tell, text="légo")
tabControl.add(listen, text="akoúo")
tabControl.pack(expand=1, fill="both")
ttk.Label(tell, text="Where do we express the deepest secrets", justify=RIGHT).grid(column=0, row=0)
tellButton = ttk.Button(tell, text="open file", command=lambda: open_file()).grid(column=1, row=0, padx=xpad, pady=ypad)
ttk.Label(tell, text="Were we express the deepest secrets", justify=LEFT).grid(column=0, row=1, padx=0)
messageString = ttk.Entry(tell, textvariable=message_var).grid(column=1, row=1, padx=xpad, pady=ypad)
ttk.Label(tell, text="Say the magical keys", justify=RIGHT, anchor="e").grid(column=0, row=2)
messageString = ttk.Entry(tell, textvariable=key_var).grid(column=1, row=2, padx=xpad, pady=ypad)
letsTell = ttk.Button(tell, text="Let's Tell", command=lambda: telling()).grid(column=0, row=3, padx=xpad, pady=ypad)

ttk.Label(listen, text="here lies ones deepest secrects").grid(column=0, row=0)
listenButton = ttk.Button(listen, text="open file", command=lambda: open_file()).grid(column=1, row=0, padx=xpad, pady=ypad)
ttk.Label(listen, text="Were we express the deepest keys", justify=LEFT).grid(column=0, row=1, padx=0)
messageString = ttk.Entry(listen, textvariable=ran_var).grid(column=1, row=1, padx=xpad, pady=ypad)
ttk.Label(listen, text="Say the magical keys", justify=RIGHT, anchor="e").grid(column=0, row=2)
messageString = ttk.Entry(listen, textvariable=key_var).grid(column=1, row=2, padx=xpad, pady=ypad)
letsTell = ttk.Button(listen, text="Let's Listen", command=lambda: listening()).grid(column=0, row=3, padx=xpad, pady=ypad)

root.mainloop()
