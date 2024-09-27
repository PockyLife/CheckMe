import tkinter as tk
from mainApp import MainApplication
from scheduler import Scheduler

def main():
    root = tk.Tk()
    root.title("Check Me")
    root.geometry("600x400")
    schedule = Scheduler()
    def run_schedule():
        schedule.exec_jobs()
        root.after(10000, run_schedule)
    MainApplication(root).pack(side=tk.TOP, fill = tk.BOTH, expand = True)
    root.after(10000, run_schedule) 
    root.mainloop()

if __name__ == "__main__":
    main()