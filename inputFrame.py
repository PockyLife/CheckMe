import tkinter as tk
import tkinter.ttk as ttk
from timeDisplay import TimeDisplay
from daySelect import DaysSelect

class InputFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.alarmName = ttk.Entry(self)
        self.submit = ttk.Button(self, text = "Save Check")
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
        self.freqEntry = ttk.Entry(self.frequencyFrame)
        self.freqLabel.pack(side = tk.LEFT)
        self.freqEntry.pack(side = tk.LEFT)

        self.alarmName.pack(side = tk.TOP, pady = 20)
        self.startEndFrame.pack(side = tk.TOP, pady = 20)
        self.frequencyFrame.pack(side = tk.TOP, pady = 10)
        self.daySelect.pack(side = tk.TOP, pady = 10)
        self.submit.pack(side = tk.TOP)
