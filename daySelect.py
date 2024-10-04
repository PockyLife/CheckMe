import tkinter as tk
import tkinter.ttk as ttk

class DaysSelect(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.selected = [tk.IntVar(value = 0), tk.IntVar(value = 0), tk.IntVar(value = 0), tk.IntVar(value = 0), tk.IntVar(value = 0), tk.IntVar(value = 0), tk.IntVar(value = 0)]
        
        self.mon = ttk.Checkbutton(self, text = "Mon", variable = self.selected[0])
        self.tue = ttk.Checkbutton(self, text = "Tue", variable = self.selected[1])
        self.wed = ttk.Checkbutton(self, text = "Wed", variable = self.selected[2])
        self.thu = ttk.Checkbutton(self, text = "Thu", variable = self.selected[3])
        self.fri = ttk.Checkbutton(self, text = "Fri", variable = self.selected[4])
        self.sun = ttk.Checkbutton(self, text = "Sun", variable = self.selected[5])
        self.sat = ttk.Checkbutton(self, text = "Sat", variable = self.selected[6])

        self.mon.pack(side = tk.LEFT)
        self.tue.pack(side = tk.LEFT)
        self.wed.pack(side = tk.LEFT)
        self.thu.pack(side = tk.LEFT)
        self.fri.pack(side = tk.LEFT)
        self.sat.pack(side = tk.LEFT)
        self.sun.pack(side = tk.LEFT)

    def get(self):
        return [x.get() for x in self.selected]

    def load(self, days: list):
        for i in range(len(self.selected)):
            self.selected[i].set(days[i])