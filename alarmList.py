import tkinter as tk
import tkinter.ttk as ttk

class AlarmList(tk.Frame):
    def __init__(self, parent, alarmDict: dict = {}, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.alarms = tk.Listbox(self)
        self.scrollbar = ttk.Scrollbar(self)
        self.alarms.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.alarms.yview)

        self.alarms.bind("<<ListboxSelect>>", self.load)
        
        self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        self.alarms.pack(side = tk.LEFT, fill = tk.BOTH, expand = tk.TRUE)

        self.alarmDict = alarmDict
    
    def update(self, alarmName: str, alarm):
        if alarmName in self.alarmDict.keys():
            pass
        else:
            self.alarms.insert(0, alarmName)
        self.alarmDict.update({alarmName: alarm})

    def delete(self, alarmName):
        self.alarmDict.pop(alarmName)
        self.alarms.delete(self.alarms.curselection()[0])

    def load(self, event):
        selected = event.widget.curselection()
        if selected:
            self.parent.inputFrame.load(self.alarmDict[event.widget.get(selected[0])])
        else:
            print("NA")