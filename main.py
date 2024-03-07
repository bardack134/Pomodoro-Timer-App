import math
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



#TODO: FUNCION DE CUENTA REGRESIVA DESDE 25 MINUTOS
#funciona llamar despues de el tiempo especificado en widnw.after()
def countdown(count_seconds):
    # el cociente sería el número de minutos completos y el residuo sería el número de segundos restantes
    seconds = (count_seconds%60)    
       
    #1 minuto tiene 60 segundos, divido los segundos en 60 para saber cuantos minutos hay      
    minutes=math.floor(count_seconds/60)
    
    if seconds == 0:
        seconds="00"
        canvas.itemconfig(timer_text, text=(f"{minutes}:{seconds}"))
    
    #itemconfig ,metodo para cambiar la configuracion de un elemento de canvas, especificando el elemento que se desa cambiar, en este caso
    #deseo cambiar el texto del elemento canvas timer_text
    canvas.itemconfig(timer_text, text=(f"{minutes}:{seconds}"))
    
    if count_seconds >0:
        window.after(1000, countdown, count_seconds-1)
    

# ---------------------------- UI SETUP ------------------------------- #
#TODO: CONFIGURACION GENERAL DE LA VENTANA
# create a tkinter window
window = Tk()

window.config(padx=100, pady=50, bg=YELLOW)

#titulo para nuestra ventana
window.title('Pomodoro Timer')

# after() se utiliza para programar una función para que se ejecute después de un número específico de milisegundos
# window.after(1000, countdown, )
 

#TODO:USANDO CANVAS PARA CARGAR UNA IMAGEN COMO FONDO
canvas=Canvas(window, width=220, height=224, bg=YELLOW, highlightthickness=0) 
#highlightthickness=0 borramos elborde cuadrado de canvas que sale al lado de la foto
#estas medidas las saque del tama;o de la foto, y son el espacio que se necesita para lafoto

filename=PhotoImage(file="tomato.png")

#carga el archivo imagen y la ubica en las cordenadas especificadas, en este caso el centro
canvas.create_image(110,112, image=filename)

#escribiendo texto en la imagen, y cordenadas de posicion para el texto dentro de la imagen
timer_text=canvas.create_text(110,130, text="00:00 ",  font=(FONT_NAME, 35, "bold")) 

canvas.grid(row=1, column=1)


#TODO: CREANDO BOTONES 'START', 'RESERT' Y LABEL CON TITULO 'TIMER'
timer_label=Label(text="TIMER",  bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold" ))
timer_label.grid(row=0, column=1, pady=2)

#boton start
#convirtiendo el tiempo total de trabajo en minutos a segundos

start_button=Button(text="start", relief="groove", bg="white", command=lambda:countdown(WORK_MIN*60))
start_button.grid(row=2, column=0)

#boton reset
reset_button=Button(text="reset", relief="groove", bg=RED_SOFT)
reset_button.grid(row=2, column=2)

#checkmark
checkmark="✔"
checkmark_label=Label(text=checkmark,  bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold" ))
checkmark_label.grid(row=2, column=1, pady=2)

#corre la ventana
window.mainloop()