import time
from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("50x50")

root.title("Baigan")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(root, width=3, font=("Arial", 18), textvariable=hour)
hourEntry.place(x=0, y=0)

minuteEntry = Entry(root, width=3, font=("Arial", 18), textvariable=minute)
minuteEntry.place(x=40, y=0)

secondEntry = Entry(root, width=3, font=("Arial", 18), textvariable=second)
secondEntry.place(x=80, y=0)


def submit():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the correct values")

    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("Time Countdown", "Time's Up")

        temp = temp - 1


btn = Button(root, text='Start', bd=5, command=submit)
btn.place(x=0, y=30)

root.mainloop()
