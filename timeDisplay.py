import tkinter as tk

class timeDisplay(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.hours_display = tk.Frame(self)
        self.colon_one = tk.Label(self, text = ":")
        self.mins_display = tk.Frame(self)
        self.colon_two = tk.Label(self, text = ":")
        self.ampm_display = tk.Frame(self)

        self.hours_inc = tk.Button(self.hours_display, text = "⋀")
        self.hours = tk.Entry(self.hours_display, width = 2)
        self.hours_dec = tk.Button(self.hours_display, text = "⋁")
        self.hours_inc.pack(side = tk.TOP)
        self.hours.pack(side = tk.TOP)
        self.hours_dec.pack(side = tk.TOP)

        self.mins_inc = tk.Button(self.mins_display, text = "⋀")
        self.mins = tk.Entry(self.mins_display, width = 2)
        self.mins_dec = tk.Button(self.mins_display, text = "⋁")
        self.mins_inc.pack(side = tk.TOP)
        self.mins.pack(side = tk.TOP)
        self.mins_dec.pack(side = tk.TOP)

        self.ampm_inc = tk.Button(self.ampm_display, text = "⋀")
        self.ampm = tk.Entry(self.ampm_display, width = 2)
        self.ampm_dec = tk.Button(self.ampm_display, text = "⋁")
        self.ampm_inc.pack(side = tk.TOP)
        self.ampm.pack(side = tk.TOP)
        self.ampm_dec.pack(side = tk.TOP)

        self.hours_display.pack(side = tk.LEFT, padx = 2)
        self.colon_one.pack(side = tk.LEFT, padx = 2)
        self.mins_display.pack(side = tk.LEFT, padx = 2)
        self.colon_two.pack(side = tk.LEFT, padx = 2)
        self.ampm_display.pack(side = tk.LEFT, padx = 2)
