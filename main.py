import tkinter as tk
from mainApp import MainApplication
def main():
    root = tk.Tk()
    root.title("Check Me")
    root.geometry("600x400")
    app = MainApplication(root).pack(side=tk.TOP, fill = tk.BOTH, expand = True)
    root.mainloop()
if __name__ == "__main__":
    main()