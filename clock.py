from tkinter import *
import time

#time-on-your-system
get_time = time.strftime("%H:%M:%S")

root = Tk()

#changer-time
def live_time():
    get_time = time.strftime("%H:%M:%S")
    show_time.config(text=get_time)
    show_time.after(1000, live_time)

#show-time
show_time = Label(root, text=get_time, border=4, bg='gray', fg='yellow', font=('arial', 64, ''))
show_time.pack()

show_time.after(1000, live_time)

root.mainloop()
