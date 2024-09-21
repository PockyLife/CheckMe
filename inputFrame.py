import tkinter as tk
from timeDisplay import timeDisplay

class InputFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.alarmName = tk.Entry(self)
        self.startEndFrame = tk.Frame(self)
        self.submit = tk.Button(self, text = "Save Check")

        self.startFrame = tk.Frame(self.startEndFrame)
        self.startFrame.pack(side = tk.LEFT, padx = 20)
        self.startTime = timeDisplay(self.startFrame)
        self.startLabel = tk.Label(self.startFrame, text = "Start At")
        self.startLabel.pack(side = tk.TOP, pady = 5)
        self.startTime.pack(side = tk.TOP)

        self.endFrame = tk.Frame(self.startEndFrame)
        self.endFrame.pack(side = tk.LEFT, padx = 20)
        self.endTime = timeDisplay(self.endFrame)
        self.endLabel = tk.Label(self.endFrame, text = "End At")
        self.endLabel.pack(side = tk.TOP, pady = 5)
        self.endTime.pack(side = tk.TOP)

        self.alarmName.pack(side = tk.TOP, pady = 20)
        self.startEndFrame.pack(side = tk.TOP, pady = 20)
        self.submit.pack(side = tk.TOP)
