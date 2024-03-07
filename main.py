from tkinter import *

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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# create a tkinter window
window = Tk()
window.config(padx=100, pady=50)

#titulo para nuestra ventana
window.title('Pomodoro Timer')

#usando canvas para cargar una imagen como fondo
canvas=Canvas(window, width=200, height=224)
filename=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=filename)
canvas.pack()

#corre la ventana
window.mainloop()