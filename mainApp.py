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

        self.load_jobs()


    def send_notification(self, message):
        self.notif.message = message
        self.notif.send(block = False)

    def update_schedule(self, alarm: Alarm):
        times = pd.date_range(alarm.get_start().isoformat(), alarm.get_end().isoformat(), freq = str(alarm.get_frequency())+"min").time
        print(times)
        for time in times:
            self.schedule.daily(time, self.send_notification, tags = {alarm.get_name()}, args = (alarm.get_name(),))

    def delete_old_jobs(self, tag):
        self.schedule.delete_jobs(tags = {tag})

    def load_jobs(self):
        self.alarmList.load_data()
        for name, alarm in self.alarmList.get().items():
            if alarm.get_days()[datetime.today().weekday()]:
                self.update_schedule(alarm)
