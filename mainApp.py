import tkinter as tk
from alarmList import AlarmList
from inputFrame import InputFrame
from notifypy import Notify
from datetime import datetime
from scheduler import Scheduler

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.inputFrame = InputFrame(self)
        self.alarmList = AlarmList(self)

        self.inputFrame.pack(side=tk.LEFT, fill= tk.BOTH, expand = tk.TRUE)
        self.alarmList.pack(side=tk.RIGHT, fill= tk.BOTH, expand = tk.TRUE)

        self.notif = Notify(default_notification_title = "Title", default_notification_application_name = "Check Me")

    def send_notification(self):
        self.notif.message = ""
        self.notif.send(block = False)
