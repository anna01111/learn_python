from tkinter import *

sec = 0


def update_clock1():
    global sec
    global pause
    label2.configure(text=sec)
    if not pause:
        sec -= 1
        if sec >= 0:
            root.after(1000, update_clock1)
        else:
            pause_button["state"] = "disabled"


def show_message():
    global sec
    sec = int(message.get())
    pause_button["state"] = "normal"
    update_clock1()


pause = False


def pause_timer():
    global pause
    # if pause:
    #     pause = False
    # else:
    #     pause = True
    pause = False if pause else True
    if not pause:
        pause_button["text"] = "pause"
        update_clock1()
    else:
        pause_button["text"] = "resume"


root = Tk()
root.title("Timer")
root.geometry("300x250")


label1 = Label(text="Please enter time in seconds", fg="#eee", bg="#333")
label1.place(relx=.175, rely=.2)

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

message_button = Button(text="start", command=show_message)
message_button.place(relx=.5, rely=.5, anchor="c")


pause_button = Button(text="pause", command=pause_timer)
pause_button.place(relx=.5, rely=.8, anchor="c")


label2 = Label(text="", fg="#eee", bg="#333")
label2.place(relx=.175, rely=.3)

root.mainloop()
