import tkinter as tk

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
def count_down():
    return


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.minsize(width=300, height=350)
window.config(padx=100, pady=50, bg=GREEN)

# background setup
bgimg = tk.PhotoImage(file="tomato.png")
# bg = tk.Label(image=bgimg)
# # bg.place(x=0,y=0)
# bg.pack()
canvas = tk.Canvas(width=200, height=224,bg=GREEN, highlightthickness=False)
canvas.create_image(103, 112, image=bgimg)
canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack()

window.mainloop()
