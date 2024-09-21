import tkinter as tk
import tkinter.ttk as ttk

class DaysSelect(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.selected = [tk.IntVar(value = 0), tk.IntVar(value = 0), tk.IntVar(value = 0), tk.IntVar(value = 0), tk.IntVar(value = 0), tk.IntVar(value = 0), tk.IntVar(value = 0)]
        
        self.sat = ttk.Checkbutton(self, text = "Sat", variable = self.selected[0])
        self.mon = ttk.Checkbutton(self, text = "Mon", variable = self.selected[1])
        self.tue = ttk.Checkbutton(self, text = "Tue", variable = self.selected[2])
        self.wed = ttk.Checkbutton(self, text = "Wed", variable = self.selected[3])
        self.thu = ttk.Checkbutton(self, text = "Thu", variable = self.selected[4])
        self.fri = ttk.Checkbutton(self, text = "Fri", variable = self.selected[5])
        self.sun = ttk.Checkbutton(self, text = "Sun", variable = self.selected[6])

        self.sat.pack(side = tk.LEFT)
        self.mon.pack(side = tk.LEFT)
        self.tue.pack(side = tk.LEFT)
        self.wed.pack(side = tk.LEFT)
        self.thu.pack(side = tk.LEFT)
        self.fri.pack(side = tk.LEFT)
        self.sun.pack(side = tk.LEFT)
