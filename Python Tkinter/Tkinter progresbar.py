from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import time

def start(tasks):
    current_task = 0
    while current_task < tasks:
        time.sleep(1)
        current_task += 1
        progress = ((current_task/tasks)*100)
        formatted_progress = "{:.1f} %".format(progress)
        bar["value"] = progress
        percent.set(f"{formatted_progress}")
        text.set(f"{current_task}/{tasks} tasks completed")
        window.update_idletasks()

    msg = "All tasks completed successfully!"
    messagebox.showinfo("Info", msg)
    # Close "main" window after messagebox
    window.destroy()

window = Tk()
window.geometry("350x200")

percent = StringVar()
text = StringVar()

bar = Progressbar(window,
                orient=HORIZONTAL,
                length=300,
                mode="determinate"
                )
bar.pack(pady=10)

percent_label = Label(window,
                    textvariable= percent)
percent_label.pack()
task_label = Label(window,
                    textvariable= text)
task_label.pack()

num_tasks = Label(window, text="Select the number of tasks:")
num_tasks.pack(pady= 10)

var = IntVar()
var.set(10)
spin_box = Spinbox(window, width= 5, from_=1, to=20, textvariable=var)
spin_box.pack(pady= 10)

start_button = Button(window,
                text="Start",
                compound= "center",
                command=lambda: start(var.get()),
                )
start_button.pack()

window.mainloop()