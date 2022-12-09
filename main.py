import time
from file_ops import read_time, write_time, str_to_date, select_date, sum_time, ConfigureTime, shutdown_handler
from tkinter import *
import os
from datetime import datetime
import atexit

time_file = "c:\\temp\\time.txt"
# maximum allowed time in seconds
max_time = 3900
now = datetime.now()
now_str = str(now)[:-7]
write_time(time_file, now_str)
now_date = now.date()
all_lines = read_time(time_file)
time_lines = str_to_date(all_lines)
day_lines = select_date(time_lines, now_date)
time_per_day = sum_time(day_lines).seconds

# if usage time exceeded, allow only 5 seconds
ct = ConfigureTime(time_per_day, max_time)
ct.add_more_sec(5)
hms = ct.hms()
# time_left = ct.time
h = hms[0]
m = hms[1]
s = hms[2]



# creating Tk window
root = Tk()

# setting geometry of tk window
root.geometry("300x270")

# at shutdown or restart execute shutdown_handler
atexit.register(shutdown_handler(time_file))

# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Masoara timpul")
root.attributes('-disabled', True)
# Declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set(h)
minute.set(m)
second.set(s)

hourEntry = Label(root, width=3, font=("Arial", 18, ""), textvariable=hour)
hourEntry.place(x=50, y=90)
h = Label(root, width=3, font=("Arial", 18, ""), text="h")
h.place(x=85, y=90)

minuteEntry = Label(root, width=3, font=("Arial", 18, ""), textvariable=minute)
minuteEntry.place(x=115, y=90)
m = Label(root, width=3, font=("Arial", 18, ""), text="m")
m.place(x=155, y=90)

secondEntry = Label(root, width=3, font=("Arial", 18, ""), textvariable=second)
secondEntry.place(x=190, y=90)
s = Label(root, width=3, font=("Arial", 18, ""), text="s")
s.place(x=230, y=90)


def make_window():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Negative time error")
    while temp > -1:

        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours = 0
        if mins > 60:
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if temp == 0:
            # pgBar = tkinter.ttk.Progressbar(root, orient = HORIZONTAL, length=300, mode = "Timpul a expirat!")
            # pgBar.place(x=45, y=200)
            # messagebox.showinfo("Missy zice", "Timpul a expirat!")
            # mes = Label(root, width=1, font=("Arial", 18, ""), text="Shutdown")
            # mes.place(x=10, y=200)

            mes = Label(root, text="Timpul a expirat. Laptopul se inchide")
            mes.place(x=10, y=200)

            os.system("shutdown /s /t 2")
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1


# button widget
# btn = Button(root, text='Set Time Countdown', bd='5',
#              command=submit)
# btn.place(x=70, y=120)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
make_window()
root.mainloop()
