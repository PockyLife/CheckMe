from tkinter import *
#Main Window
root = Tk()
root.title("Check Me")
root.geometry("600x400")

left_frame = Frame(root, width=300, height=400,bg="red")
left_frame.pack(side=LEFT)
right_frame = Frame(root, width=300, height=400,bg="blue")
right_frame.pack(side=RIGHT)

#Alarm List Frame
alarm_list = Frame(right_frame, width=300, height=400, bg="yellow")
alarm_list.grid(row=0, column=1)
#Alarm Details Frame
alarm_details = Frame(left_frame, width=300, height=200, bg="green")
alarm_details.grid(row=0, column=0)
#Alarm Input Frame
alarm_input = Frame(left_frame, width=300, height=200, bg="pink")
alarm_input.grid(row=1, column=0)

root.mainloop()