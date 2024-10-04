import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from alarmClass import Alarm
from timeDisplay import TimeDisplay
from daySelect import DaysSelect
from customEntries import PlaceholderEntry

class InputFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.alarmName = PlaceholderEntry(self, "Enter check name ...")
        self.savedel = tk.Frame(self)
        self.submit = ttk.Button(self.savedel, text = "Save Check", command = self.save)
        self.deletebtn = ttk.Button(self.savedel, text = "Delete Check", command = self.delete)
        self.daySelect = DaysSelect(self)
        self.startEndFrame = tk.Frame(self)

        self.startFrame = tk.Frame(self.startEndFrame)
        self.startFrame.pack(side = tk.LEFT, padx = 20)
        self.startTime = TimeDisplay(self.startFrame)
        self.startLabel = ttk.Label(self.startFrame, text = "Start At")
        self.startLabel.pack(side = tk.TOP, pady = 5)
        self.startTime.pack(side = tk.TOP)

        self.endFrame = tk.Frame(self.startEndFrame)
        self.endFrame.pack(side = tk.LEFT, padx = 20)
        self.endTime = TimeDisplay(self.endFrame)
        self.endLabel = ttk.Label(self.endFrame, text = "End At")
        self.endLabel.pack(side = tk.TOP, pady = 5)
        self.endTime.pack(side = tk.TOP)

        self.frequencyFrame = tk.Frame(self)
        self.freqLabel = ttk.Label(self.frequencyFrame, text = "How many minutes between checks")
        self.freqEntry = PlaceholderEntry(self.frequencyFrame, "Enter minutes ...")
        self.freqLabel.pack(side = tk.LEFT)
        self.freqEntry.pack(side = tk.LEFT)

        self.alarmName.pack(side = tk.TOP, pady = 20)
        self.startEndFrame.pack(side = tk.TOP, pady = 20)
        self.frequencyFrame.pack(side = tk.TOP, pady = 10)
        self.daySelect.pack(side = tk.TOP, pady = 10)
        self.savedel.pack(side = tk.TOP)
        self.submit.pack(side = tk.LEFT, padx = 10)
        self.deletebtn.pack(side = tk.LEFT, padx = 10)

    def save(self): #if selected update selected
        if self.alarmName.is_empty():
            tk.messagebox.showerror("Empty name", "Please enter a check name") 
        elif self.freqEntry.is_empty():
            tk.messagebox.showerror("Empty frequency", "Please enter a frequency")
        elif self.startTime.get() > self.endTime.get():
            tk.messagebox.showerror("Invalid Time", "Start time must be before end time")
        else:
            savedAlarm = Alarm(self.alarmName.get(), self.startTime.get(), self.endTime.get(), int(self.freqEntry.get()), self.daySelect.get())
            self.parent.alarmList.update(str(savedAlarm), savedAlarm)
        
    def delete(self):
        self.parent.alarmList.delete(self.alarmName.get())
    
    def load(self, alarm: Alarm):
        self.alarmName.load(alarm.get_name())

        self.freqEntry.load(alarm.get_frequency())

        self.startTime.load(alarm.get_start())
        
        self.endTime.load(alarm.get_end())

        self.daySelect.load(alarm.get_days())