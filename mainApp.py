import tkinter as tk
from alarmList import AlarmList
from inputFrame import InputFrame

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.inputFrame = InputFrame(self)
        self.alarmList = AlarmList(self)

        self.inputFrame.pack(side=tk.LEFT, fill= tk.BOTH, expand = tk.TRUE)
        self.alarmList.pack(side=tk.RIGHT, fill= tk.BOTH, expand = tk.TRUE)