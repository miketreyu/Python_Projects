import tkinter as tk
from tkinter import messagebox

# Variables globales
player = 'X'
game_over = False

# Funciones
def check_for_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != ' ':
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != ' ':
            return True
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != ' ':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != ' ':
        return True
    return False

def click(row, col):
    global player, game_over
    if buttons[row][col]['text'] == ' ' and not game_over:
        buttons[row][col]['text'] = player
        buttons[row][col]['bg'] = '#37474F' if player == 'X' else '#455A64'  
        if check_for_winner():
            messagebox.showinfo('Tres En Raya', f'¡Jugador {player} gana!')
            game_over = True
        elif all(buttons[r][c]['text'] != ' ' for r in range(3) for c in range(3)):
            messagebox.showinfo('Tres En Raya', '¡Empate!')
            game_over = True
        else:
            player = 'O' if player == 'X' else 'X'

def reset():
    global player, game_over
    player = 'X'
    game_over = False
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ' '
            buttons[row][col]['bg'] = '#263238'

# Configuración de la ventana principal
root = tk.Tk()
root.title('Tres En Raya')
root.geometry('400x450')
root.configure(bg='#263238')

# Creación del frame central
frame = tk.Frame(root, bg='#263238')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Creación de los botones del tablero
buttons = [[tk.Button(frame, text=' ', font=('normal', 20, 'bold'), width=3, height=2, bg='#263238', fg='white',
                      command=lambda row=row, col=col: click(row, col)) 
            for col in range(3)] for row in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row, column=col, padx=5, pady=5)

# Botón de reinicio
reset_button = tk.Button(root, text='Reiniciar', command=reset, bg='#455A64', fg='white', font=('normal', 12))
reset_button.pack(pady=10)

# Ejecución del bucle principal de la aplicación
root.mainloop()