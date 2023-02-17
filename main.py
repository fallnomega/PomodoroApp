import tkinter as tk
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer():
    return


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time_remaining):
    if time_remaining==0:
        return
    min_sec = time.strftime("%M:%S",time.gmtime(time_remaining))
    canvas.itemconfig(timer_testing,text=min_sec)
    window.after(1000, count_down, time_remaining -1 )

def reset_time():
    return 1500

# ---------------------------- UI SETUP ------------------------------- #
#window setup/canvas setup
window = tk.Tk()
window.title("Pomodoro")
window.minsize(width=300, height=350)
window.config(padx=100, pady=50, bg=GREEN)
time_left = 1500

# background setup
bgimg = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=200, height=224, bg=GREEN, highlightthickness=False)
canvas.create_image(100, 112, image=bgimg)
timer_testing = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack()
#timer
timer_label = tk.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=RED, bg=GREEN)
timer_label.place(x=50, y=-55)
#start and reset buttons
start = tk.Button(text="Start", bg=GREEN, borderwidth=0, highlightthickness=0,command=lambda: count_down(time_left))
start.place(x=-50, y=200)
reset = tk.Button(text="Reset", bg=GREEN, borderwidth=0, highlightthickness=0,command=lambda: reset_time(time_left))
reset.place(x=175, y=200)
#session checkmarks to see how many times you have run the timer
sessions = tk.Label(text="√",fg=RED,bg=GREEN)
sessions.place(x=90, y=240)

window.mainloop()
