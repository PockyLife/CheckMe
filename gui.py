from tkinter import *
from alarm import *
#Main Window
root = Tk()
root.title("Check Me")
root.geometry("600x400")

#Left Frame
left_frame = Frame(root)
left_frame.pack(side=LEFT, fill= BOTH, expand = TRUE)

#Right Frame
right_frame = Frame(root)
right_frame.pack(side=RIGHT, fill= BOTH, expand = TRUE)

#Alarm List
alarm_list = Listbox(right_frame)
alarm_list.pack(side = LEFT, fill = BOTH, expand = TRUE)\

#List Scroll
alarm_list_scrollbar = Scrollbar(right_frame)
alarm_list_scrollbar.pack(side = RIGHT, fill = Y)

alarm_list.config(yscrollcommand = alarm_list_scrollbar.set)
alarm_list_scrollbar.config(command = alarm_list.yview)


#Alarm Input
name = Entry(left_frame)

#Alarm Time Display
time_display = Frame(left_frame)

hours_display = Frame(time_display)
colon_one = Label(time_display, text = ":")
mins_display = Frame(time_display)
colon_two = Label(time_display, text = ":")
ampm_display = Frame(time_display)

hours_inc = Button(hours_display, text = "⋀")
hours = Entry(hours_display, width = 2)
hours_dec = Button(hours_display, text = "⋁")
hours_inc.pack(side = TOP)
hours.pack(side = TOP)
hours_dec.pack(side = TOP)

mins_inc = Button(mins_display, text = "⋀")
mins = Entry(mins_display, width = 2)
mins_dec = Button(mins_display, text = "⋁")
mins_inc.pack(side = TOP)
mins.pack(side = TOP)
mins_dec.pack(side = TOP)

ampm_inc = Button(ampm_display, text = "⋀")
ampm = Entry(ampm_display, width = 2)
ampm_dec = Button(ampm_display, text = "⋁")
ampm_inc.pack(side = TOP)
ampm.pack(side = TOP)
ampm_dec.pack(side = TOP)


hours_display.pack(side = LEFT, padx = 2)
colon_one.pack(side = LEFT, padx = 2)
mins_display.pack(side = LEFT, padx = 2)
colon_two.pack(side = LEFT, padx = 2)
ampm_display.pack(side = LEFT, padx = 2)


submit = Button(left_frame, text = "Save")
name.pack(side = TOP, pady = 5)
time_display.pack(side = TOP, pady = 5)
submit.pack(side = TOP, pady = 5)

root.mainloop()