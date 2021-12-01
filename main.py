from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_time)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_time)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=70, bg=YELLOW)

# Title Label
title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=210, height=240, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(105, 120, image=tomato_photo)
timer_text = canvas.create_text(110, 140, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Start Button
start_button = Button(text="Start", width=7, font=(FONT_NAME, 12, "bold"), command=start_timer, highlightthickness=0)
start_button['bg'] = RED
start_button['fg'] = 'white'
start_button.grid(column=2, row=2)

# Reset Button
reset_button = Button(text="Stop", width=7, font=(FONT_NAME, 12, "bold"), highlightthickness=0)
reset_button['bg'] = RED
reset_button['fg'] = 'white'
reset_button.grid(column=0, row=2)

# Checkmarks Label
check_marks = Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)

window.mainloop()
