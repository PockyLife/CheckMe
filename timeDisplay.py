import tkinter as tk
import tkinter.ttk as ttk

class TimeDisplay(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.hours_display = tk.Frame(self)
        self.colon_one = ttk.Label(self, text = ":")
        self.mins_display = tk.Frame(self)
        self.colon_two = ttk.Label(self, text = ":")
        self.ampm_display = tk.Frame(self)

        self.hours_inc = ttk.Button(self.hours_display, text = "⋀", width = 5)
        self.hours = ttk.Entry(self.hours_display, width = 5)
        self.hours_dec = ttk.Button(self.hours_display, text = "⋁", width = 5)
        self.hours_inc.pack(side = tk.TOP)
        self.hours.pack(side = tk.TOP)
        self.hours_dec.pack(side = tk.TOP)

        self.mins_inc = ttk.Button(self.mins_display, text = "⋀", width = 5)
        self.mins = ttk.Entry(self.mins_display, width = 5)
        self.mins_dec = ttk.Button(self.mins_display, text = "⋁", width = 5)
        self.mins_inc.pack(side = tk.TOP)
        self.mins.pack(side = tk.TOP)
        self.mins_dec.pack(side = tk.TOP)

        self.ampm_inc = ttk.Button(self.ampm_display, text = "⋀", width = 5)
        self.ampm = ttk.Entry(self.ampm_display, width = 5)
        self.ampm_dec = ttk.Button(self.ampm_display, text = "⋁", width = 5)
        self.ampm_inc.pack(side = tk.TOP)
        self.ampm.pack(side = tk.TOP)
        self.ampm_dec.pack(side = tk.TOP)

        self.hours_display.pack(side = tk.LEFT, padx = 2)
        self.colon_one.pack(side = tk.LEFT, padx = 2)
        self.mins_display.pack(side = tk.LEFT, padx = 2)
        self.colon_two.pack(side = tk.LEFT, padx = 2)
        self.ampm_display.pack(side = tk.LEFT, padx = 2)
