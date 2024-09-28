import tkinter as tk
import pandas as pd
from alarmClass import Alarm
from alarmList import AlarmList
from inputFrame import InputFrame
from notifypy import Notify
from datetime import datetime
from scheduler import Scheduler

class MainApplication(tk.Frame):
    def __init__(self, parent, schedule: Scheduler, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.inputFrame = InputFrame(self)
        self.alarmList = AlarmList(self)
        self.schedule = schedule

        self.inputFrame.pack(side=tk.LEFT, fill= tk.BOTH, expand = tk.TRUE)
        self.alarmList.pack(side=tk.RIGHT, fill= tk.BOTH, expand = tk.TRUE)

        self.notif = Notify(default_notification_title = "Title", default_notification_application_name = "Check Me")

    def send_notification(self):
        self.notif.message = "Ding"
        self.notif.send(block = False)

    def update_schedule(self, alarm: Alarm):
        times = pd.date_range(alarm.get_start().isoformat(), alarm.get_end().isoformat(), freq = str(alarm.get_frequency())+"min").time
        print(times)
        for time in times:
            self.schedule.daily(time, self.send_notification)
