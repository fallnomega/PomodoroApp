import tkinter as tk
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_SEC = 1500
# SHORT_BREAK_SEC = 300
# LONG_BREAK_SEC = 1200

# TESTING TIMERS BELOW
WORK_SEC = 5
SHORT_BREAK_SEC = 10
LONG_BREAK_SEC = 60
reps = 1


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    odds = (1, 3, 5, 7)
    evens = (2, 4, 6)
    if reps in odds:
        timer_label.config(text="WORK", fg="green")
        count_down(WORK_SEC)
        reps += 1
    elif reps in evens:
        timer_label.config(text="BREAK", fg=PINK)
        count_down(SHORT_BREAK_SEC)
        reps += 1
    elif reps == 8:
        timer_label.config(text="BREAK", fg=RED)
        count_down(LONG_BREAK_SEC)
        reps += 1
    else:
        return


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time_remaining):
    min_sec = time.strftime("%M:%S", time.gmtime(time_remaining))
    canvas.itemconfig(timer_testing, text=min_sec)

    if time_remaining == 0:
        start_timer()
        sessions = tk.Label(text="√", fg=YELLOW, bg=GREEN)
        sessions.place(x=90, y=240)
        return
    window.after(1000, count_down, time_remaining - 1)


def reset_time(time_to_reset):
    time_to_reset = 5
    return time_to_reset


# ---------------------------- UI SETUP ------------------------------- #
# window setup/canvas setup
window = tk.Tk()
window.title("Pomodoro")
window.minsize(width=300, height=350)
window.config(padx=100, pady=50, bg=GREEN)
# background setup
bgimg = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=200, height=224, bg=GREEN, highlightthickness=False)
canvas.create_image(100, 112, image=bgimg)
timer_testing = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack()
# timer
timer_label = tk.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=RED, bg=GREEN)
timer_label.place(x=50, y=-55)
# start and reset buttons
start = tk.Button(text="Start", bg=GREEN, borderwidth=0, highlightthickness=0, command=start_timer)
start.place(x=-50, y=200)
reset = tk.Button(text="Reset", bg=GREEN, borderwidth=0, highlightthickness=0)
reset.place(x=175, y=200)
# session checkmarks to see how many times you have run the timer


window.mainloop()
