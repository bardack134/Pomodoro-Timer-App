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
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.2
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- # 
#TODO: AL OPRIMIR EL BOTON RESET SE DEBE RESETEAR EL POMODORO
def reset_timer():
    # Hacemos que las variables 'reps' y 'checkmark' sean globales para poder modificarlas dentro de esta función
    global reps
    global checkmark

    # Configuramos la etiqueta del temporizador para mostrar "TIMER"
    timer_label.config(text="TIMER")

    # Reiniciamos el número de repeticiones a 0
    reps = 1

    # Limpiamos los checkmarks
    checkmark = ""
    checkmark_label.config(text=checkmark)

    # Cancelamos la función programada con 'after'
    window.after_cancel(after_funcion)

    # Restablecemos el texto del temporizador a "00:00"
    canvas.itemconfig(timer_text, text="00:00")

    
    
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
#TODO: FUNCION CON LA LOGICA DEL METODO POMODORO 4 REPS X 25 MITS, Y 5 MINTS BREAK

#variable global que almacena la repeticion actual del pomodoro
reps=1

#funcion que se ejecutara despues de oprimir el boton start
def start_pomodoro():
    # Hacemos que la variable 'reps' sea global para poder modificarla dentro de esta función
    global reps 

    # Convertimos los minutos de trabajo y descanso en segundos
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    
    # Si estamos en un ciclo de trabajo (1, 3, 5, 7)
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        # Configuramos la etiqueta del temporizador para mostrar "WORK"
        timer_label.config(text="WORK", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
        # Iniciamos la cuenta regresiva con el tiempo de trabajo
        countdown(work_seconds)
                   
    # Si estamos en un ciclo de descanso corto (2, 4, 6)
    elif reps == 2 or reps == 4 or reps == 6:
        # Configuramos la etiqueta del temporizador para mostrar "BREAK"
        timer_label.config(text="BREAK", bg=YELLOW, fg=PINK, font=(FONT_NAME, 35, "bold"))
        # Iniciamos la cuenta regresiva con el tiempo de descanso corto
        countdown(short_break_seconds)
    
    # Si estamos en un ciclo de descanso largo (8)
    elif reps == 8:
        # Configuramos la etiqueta del temporizador para mostrar "BREAK"
        timer_label.config(text="BREAK", bg=YELLOW, fg=RED, font=(FONT_NAME, 35, "bold"))
        # Iniciamos la cuenta regresiva con el tiempo de descanso largo
        countdown(long_break_seconds)



#TODO: FUNCION DE CUENTA REGRESIVA, RECIBE COMO PARAMETRO TIEMPO EN SEGUNDOS, YA SEA  TIEMPO DE TRABAJO O DESCANSO 
def countdown(count_seconds):
    # Hacemos que las variables 'reps', 'checkmark' y 'after_funcion' sean globales para poder modificarlas dentro de esta función
    global reps
    global checkmark
    global after_funcion
    
    # el cociente sería el número de minutos completos y el residuo sería el número de segundos restantes
    seconds = count_seconds%60    
       
    #1 minuto tiene 60 segundos, divido los segundos en 60 para saber cuantos minutos hay      
    minutes=math.floor(count_seconds/60)
    
    # Si los segundos son 0, los mostramos como "00"
    if seconds == 0:
        seconds="00"
        canvas.itemconfig(timer_text, text=(f"{minutes}:{seconds}"))
     
    # Si los segundos son menores a 10, añadimos un "0" al principio para mantener el formato de dos dígitos    
    elif seconds < 10:
        seconds=(f"0{seconds}")
        
        # Actualizamos el texto del elemento 'timer_text' en el canvas para mostrar los minutos y segundos
        canvas.itemconfig(timer_text, text=(f"{minutes}:{seconds}"))
    
    #itemconfig ,metodo para cambiar la configuracion de un elemento de canvas, especificando el elemento que se desa cambiar, en este caso
    #deseo cambiar el texto del elemento canvas timer_text
    canvas.itemconfig(timer_text, text=(f"{minutes}:{seconds}"))
    
    #para evitar numeros negativos en nuestra pantalla
    if count_seconds >0:
        # after() se utiliza para programar una función para que se ejecute después de un número específico de milisegundos
        after_funcion=window.after(1000, countdown, count_seconds-1)
        
    
    else:
        # Si estamos en un ciclo de trabajo (es decir es　'reps' es impar), añadimos un checkmark
        if reps%2 !=0:
            checkmark+='✔️'
            checkmark_label.config(text=checkmark,  bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold" ))
        # Incrementamos reps para pasar al siguiente ciclo (trabajo o descanso)
        
        reps+=1
        # Iniciamos el siguiente ciclo (trabajo o descanso)
        start_pomodoro()
        
        
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


#TODO: CREANDO BOTONES 'START', 'RESERT', 'CHECKMARK' Y LABEL CON TITULO 'TIMER'
timer_label=Label(text="TIMER",  bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold" ))
timer_label.grid(row=0, column=1, pady=2)

#boton start
#hemos convertido el tiempo total de trabajo en minutos a segundos
start_button=Button(text="start", relief="groove", bg="white",  command=start_pomodoro)
start_button.grid(row=2, column=0)

#boton reset
reset_button=Button(text="reset", relief="groove", bg=RED_SOFT,  command=reset_timer)
reset_button.grid(row=2, column=2)

#checkmark
checkmark=""
checkmark_label=Label(text=checkmark,  bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold" ))
checkmark_label.grid(row=2, column=1, pady=2)



#corre la ventana
window.mainloop()