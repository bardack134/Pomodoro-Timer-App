from tkinter import *
# # Importa el módulo tkinter.ttk y sobrescribe automáticamente todos los widgets de tkinter
# from tkinter.ttk import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
RED_SOFT="#FF8E8F"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
#TODO: configuracion de la ventana
# create a tkinter window
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)

#titulo para nuestra ventana
window.title('Pomodoro Timer')


#TODO:usando canvas para cargar una imagen como fondo
#highlightthickness=0 borramos elborde cuadrado de canvas que sale al lado de la foto
#estas medidas las saque del tama;o de la foto, y son el espacio que se necesita para lafoto
canvas=Canvas(window, width=220, height=224, bg=YELLOW, highlightthickness=0) 
filename=PhotoImage(file="tomato.png")
canvas.create_image(110,112, image=filename)
#escribiendo texto en la imagen, y cordenadas de posicion para el texto
canvas.create_text(110,130, text="00:00",  font=(FONT_NAME, 35, "bold")) 
canvas.grid(row=1, column=1)


#TODO: creando botones 'start', 'resert' y label con titulo 'timer'
timer_text=Label(text="TIMER",  bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold" ))
timer_text.grid(row=0, column=1, pady=2)
#boton start
start_button=Button(text="start", relief="groove", bg="white")
start_button.grid(row=3, column=0)
#boton reset
reset_button=Button(text="reset", relief="groove", bg=RED_SOFT)
reset_button.grid(row=3, column=2)


#corre la ventana
window.mainloop()