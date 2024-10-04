import tkinter as tk
import tkinter.ttk as ttk
import pickle
import os

class AlarmList(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.alarms = tk.Listbox(self, exportselection = False)
        self.scrollbar = ttk.Scrollbar(self)
        self.alarms.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.alarms.yview)

        self.alarms.bind("<<ListboxSelect>>", self.click_load)
        
        self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        self.alarms.pack(side = tk.LEFT, fill = tk.BOTH, expand = tk.TRUE)
        
        self.alarmDict = dict()
    
    def update(self, alarmName: str, alarm):
        if alarmName in self.alarmDict.keys():
            self.parent.delete_old_jobs(alarmName)
            self.parent.update_schedule(alarm)
        else:
            self.alarms.insert(0, alarmName)
            self.parent.update_schedule(alarm)
        self.alarmDict.update({alarmName: alarm})
        self.save_data()

    def delete(self, alarmName):
        if alarmName in self.alarmDict:
            self.parent.delete_old_jobs(alarmName)
            self.alarmDict.pop(alarmName)
            self.alarms.delete(self.alarms.curselection()[0])
            self.save_data()

    def click_load(self, event):
        selected = event.widget.curselection()
        if selected:
            self.parent.inputFrame.load(self.alarmDict[event.widget.get(selected[0])])
        else:
            pass

    def get(self):
        return self.alarmDict
    
    def save_data(self):
        with open("alarm_data.pkl", "wb") as outp:
            pickle.dump(self.alarmDict, outp, pickle.HIGHEST_PROTOCOL)

    def load_data(self):
        if os.path.exists("alarm_data.pkl"):
            with open("alarm_data.pkl", "rb") as inp:
                self.alarmDict = pickle.load(inp)
            for key in self.alarmDict.keys():
                self.alarms.insert(0, key)
