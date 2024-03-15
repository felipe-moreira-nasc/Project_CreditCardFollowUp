# %% Import definitions

import pandas as pd
from tkinter import *
from tkinter import ttk

# %% Funções
def openFile():
    '''
    Opens a file selection dialog and returns the chosen file path.

    Returns:
        str: The selected file path or None if no file was selected.
    '''
    openTkFrame

def openTkFrame():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
#
# %% Main

openTkFrame()


# %%
