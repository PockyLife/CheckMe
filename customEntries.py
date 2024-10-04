import tkinter as tk
import tkinter.ttk as ttk

class TimeEntry(ttk.Entry):
    def __init__(self, parent, default, *args, **kwargs):
        ttk.Entry.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.insert(0, default)

class AMPMEntry(ttk.Entry):
    def __init__(self, parent, default, *args, **kwargs):
        ttk.Entry.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.insert(0, default)

class PlaceholderEntry(ttk.Entry):
    def __init__(self, parent, placeholder: str, *args, **kwargs):
        ttk.Entry.__init__(self, parent, *args, **kwargs)
        self.empty = True
        
        self.parent = parent
        self.placeholder = placeholder

        self.insert(0, placeholder)
        self.config(foreground = "grey")
        self.bind('<FocusIn>', self.on_entry_click)
        self.bind('<FocusOut>', self.on_focusout)
    
    def on_entry_click(self, event):
        if self.get() == self.placeholder:
            self.delete(0, "end") #delete all the text in the entry
            self.insert(0, "") #Insert blank for user input
            self.config(foreground = "black")
            self.empty = False
    
    def on_focusout(self, event):
        if self.get() == "":
            self.insert(0, self.placeholder)
            self.config(foreground = "grey")
            self.empty = True

    def is_empty(self):
        return self.empty
    
    def load(self, string: str):
        self.delete(0, "end")
        self.insert(0, string)
        self.config(foreground = "black")
        self.empty = False