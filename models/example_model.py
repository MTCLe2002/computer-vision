from re import S
import sys

from click import style

sys.path.append("src/features")
# sys.path.append("src/data")
# sys.path.append("src/models")
# sys.path.append("src/visualization")

import window_features
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
window_features.CenterOnScreen(root=root, root_width=1000, root_height=600)

window_features.iconChange(
    root=root,
    link_folder_icon="C:/Users/mtcle/OneDrive/WorkSpace/computer-vision/data/external/image/icon.ico",
)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=5)


t = tk.Frame(root, width=1000, height=100, borderwidth=2, relief="solid")
t.grid(row=0, column=0, sticky=tk.N)
b = tk.Frame(root, width=1000, height=100, borderwidth=2, relief="solid")
b.grid(row=1, column=0)

b.columnconfigure(0, weight=1)
b.columnconfigure(1, weight=1)
d = tk.Frame(b, width=500, height=500, borderwidth=2, relief="solid")
d.grid(row=0, column=0)
e = tk.Frame(b, width=500, height=500, borderwidth=2, relief="solid")
e.grid(row=0, column=1)

root.mainloop()
