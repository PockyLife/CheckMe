import tkinter as tk
import tkinter.ttk as ttk
import datetime
from customEntries import TimeEntry, AMPMEntry

class TimeDisplay(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.hours_display = tk.Frame(self)
        self.colon_one = ttk.Label(self, text = ":")
        self.mins_display = tk.Frame(self)
        self.colon_two = ttk.Label(self, text = ":")
        self.ampm_display = tk.Frame(self)

        self.hours_inc = ttk.Button(self.hours_display, text = "⋀", width = 5, command = self._inc_hour)
        self.hours = TimeEntry(self.hours_display, 12, width = 5)
        self.hours_dec = ttk.Button(self.hours_display, text = "⋁", width = 5, command = self._dec_hour)
        self.hours_inc.pack(side = tk.TOP)
        self.hours.pack(side = tk.TOP)
        self.hours_dec.pack(side = tk.TOP)

        self.mins_inc = ttk.Button(self.mins_display, text = "⋀", width = 5, command = self._inc_min)
        self.mins = TimeEntry(self.mins_display, 30, width = 5)
        self.mins_dec = ttk.Button(self.mins_display, text = "⋁", width = 5, command = self._dec_min)
        self.mins_inc.pack(side = tk.TOP)
        self.mins.pack(side = tk.TOP)
        self.mins_dec.pack(side = tk.TOP)

        self.ampm_inc = ttk.Button(self.ampm_display, text = "⋀", width = 5, command = self._swap_ampm)
        self.ampm = AMPMEntry(self.ampm_display, "PM", width = 5)
        self.ampm_dec = ttk.Button(self.ampm_display, text = "⋁", width = 5, command = self._swap_ampm)
        self.ampm_inc.pack(side = tk.TOP)
        self.ampm.pack(side = tk.TOP)
        self.ampm_dec.pack(side = tk.TOP)

        self.hours_display.pack(side = tk.LEFT, padx = 2)
        self.colon_one.pack(side = tk.LEFT, padx = 2)
        self.mins_display.pack(side = tk.LEFT, padx = 2)
        self.colon_two.pack(side = tk.LEFT, padx = 2)
        self.ampm_display.pack(side = tk.LEFT, padx = 2)

    def get(self):
        if self.ampm.get() == "AM":
            if self.hours.get() == "12":
                return datetime.time(0, int(self.mins.get()))
            return datetime.time(int(self.hours.get()), int(self.mins.get()))
        else:
            if self.hours.get() == "12":
                return datetime.time(12, int(self.mins.get()))
            return datetime.time(int(self.hours.get())+12, int(self.mins.get()))
        
    def load(self, time: datetime.time): #possible error when exactly 12:00, or 12:01 etc
        hour = time.hour
        minute = time.minute
        if time >= datetime.time(12,0):
            if time.hour > 12:
                self.hours.delete(0, "end")
                self.hours.insert(0, f"{hour-12}")
            else:
                self.hours.delete(0, "end")
                self.hours.insert(0, "12")
            
            self.mins.delete(0, "end")
            self.mins.insert(0,f"{minute:02d}")
            
            self.ampm.delete(0, "end")
            self.ampm.insert(0, "PM")
        else:
            if time.hour > 0:
                self.hours.delete(0, "end")
                self.hours.insert(0, f"{hour}")
            else:
                self.hours.delete(0, "end")
                self.hours.insert(0, f"{12}")
            
            self.mins.delete(0, "end")
            self.mins.insert(0, f"{minute:02d}")
            
            self.ampm.delete(0, "end")
            self.ampm.insert(0, "AM")
        
    def _swap_ampm(self):
        if self.ampm.get() == "AM":
            self.ampm.delete(0, "end")
            self.ampm.insert(0, "PM")
        else:
            self.ampm.delete(0, "end")
            self.ampm.insert(0, "AM")

    def _inc_min(self):
        if self.mins.get() == "59":
            self.mins.delete(0, "end")
            self.mins.insert(0, "00")
        else:
            newMin = int(self.mins.get()) + 1
            self.mins.delete(0, "end")
            self.mins.insert(0, f"{newMin:02d}")

    def _dec_min(self):
        if self.mins.get() == "00":
            self.mins.delete(0, "end")
            self.mins.insert(0, "59")
        else:
            newMin = int(self.mins.get()) - 1
            self.mins.delete(0, "end")
            self.mins.insert(0, f"{newMin:02d}")

    def _inc_hour(self):
        if self.hours.get() == "12":
            self.hours.delete(0, "end")
            self.hours.insert(0, "1")
        else:
            newHour = int(self.hours.get()) + 1
            self.hours.delete(0, "end")
            self.hours.insert(0, newHour)

    def _dec_hour(self):
        if self.hours.get() == "1":
            self.hours.delete(0, "end")
            self.hours.insert(0, "12")
        else:
            newHour = int(self.hours.get()) - 1
            self.hours.delete(0, "end")
            self.hours.insert(0, newHour)
