import tkinter as tk
import tkinter.ttk as ttk

class AlarmList(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.alarmList = tk.Listbox(self)
        self.scrollbar = ttk.Scrollbar(self)
        self.alarmList.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.alarmList.yview)
        
        self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        self.alarmList.pack(side = tk.LEFT, fill = tk.BOTH, expand = tk.TRUE)
