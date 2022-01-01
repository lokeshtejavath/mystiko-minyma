import tkinter
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo

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


tabControl.add(tell, text="légo")
tabControl.add(listen, text="akoúo")
tabControl.pack(expand=1, fill="both")
ttk.Label(tell, text="here we express the deepest secrets").grid(column=0, row=0, padx=200, pady=200)
ttk.Label(listen, text="here lies ones deepest secrects").grid(column=0, row=0, padx=200, pady=200)

root.mainloop()
