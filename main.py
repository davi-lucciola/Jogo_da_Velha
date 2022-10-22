from tkinter import *
from tkinter import messagebox
from random import choice


class JogoDaVelha:
    preenchidos = 0
    player_x_or_o = 'X'
    X_COLOR = 'goldenrod'
    O_COLOR = 'purple'
    ACT_COLOR = X_COLOR

    def __init__(self) -> None:
        'Constructor of aplication'
        self.window()
        self.frames()
        self.upper_wigets()
        self.lower_wigets()

    # Building front-end
    def window(self):
        'Create and Configuring the window'
        self.game_window = Tk()
        self.game_window.geometry('550x620+200+200')
        self.game_window.resizable(False, False)
        self.game_window.title('Jogo da Velha')

    def frames(self):
        'Building and Positioning Frames'
        self.upper_frame = Frame(
            master= self.game_window,
            bg='gray',
            height=90,
        )
        self.upper_frame.pack(fill=BOTH)

        self.lower_frame = Frame(
            master= self.game_window,
            bg='white'
        )
        self.lower_frame.pack()

    def upper_wigets(self):
        'Building and Positioning Wigets for upper frame'
        velha_title = Label(
            master=self.upper_frame,
            bg='gray',
            fg='white',
            font=('Rachana Bold Italic', 32, 'bold'),
            text='Jogo da Velha',
        )
        velha_title.place(anchor=NW, x=20, y=15)

        self.current_player = Label(
            master=self.upper_frame,
            bg='gray',
            fg=self.ACT_COLOR,
            font=('Comic Sans MS', 22, 'bold'),
            text= f'Jogador: {self.player_x_or_o}'
        )
        self.current_player.place(anchor=NE, x=530, y=36)

        self.line = Label(
            master=self.upper_frame,
            width=30,
            height=1,
            bg=self.ACT_COLOR
        )
        self.line.place(anchor=NE, x=560, y=80)

    def lower_wigets(self):
        'building and Positioning Wigets for lower frame'
        self.buttons = []
        for _ in range(9):
            btn = Button(
                self.lower_frame, 
                relief='flat',
                font=('Purisa', 34),
                text='',
                width=5,
                height=2,
                bg='lightgray',
            )
            self.buttons.append(btn)
        
        self.buttons[0].config(command= lambda: self.insert_value(self.buttons[0]))
        self.buttons[1].config(command= lambda: self.insert_value(self.buttons[1]))
        self.buttons[2].config(command= lambda: self.insert_value(self.buttons[2]))
        self.buttons[3].config(command= lambda: self.insert_value(self.buttons[3]))
        self.buttons[4].config(command= lambda: self.insert_value(self.buttons[4]))
        self.buttons[5].config(command= lambda: self.insert_value(self.buttons[5]))
        self.buttons[6].config(command= lambda: self.insert_value(self.buttons[6]))
        self.buttons[7].config(command= lambda: self.insert_value(self.buttons[7]))
        self.buttons[8].config(command= lambda: self.insert_value(self.buttons[8]))

        row_increment = 0
        for i in range(3):
            for j in range(3):
                self.buttons[i+j+row_increment].grid(row=i, column=j, padx=13, pady=7)
            if i != 2:
                row_increment += 2
            else:
                continue
        
    # Game Logic
    def insert_value(self, button):
        'Inserting values (X or O) in button'
        if (button['text'] != ''): return

        button['text'] = self.player_x_or_o
        if self.player_x_or_o == 'X':
            button['fg'] = self.X_COLOR
            next_player = 'O'
            self.ACT_COLOR = self.O_COLOR
        else:
            button['fg'] = self.O_COLOR
            next_player = 'X'
            self.ACT_COLOR = self.X_COLOR

        self.preenchidos += 1
        venceu = self.check_victory()
        if venceu == 'nao_venceu':
            self.player_x_or_o = next_player
            self.current_player['text'] = f'Jogador: {self.player_x_or_o}'
            self.current_player['fg'] = self.ACT_COLOR
            self.line['bg'] = self.ACT_COLOR
        elif venceu == 'venceu': 
            messagebox.showinfo('Velha!', f'O player "{self.player_x_or_o}" venceu!')
            self.reset()
        elif venceu == 'empatou':
            messagebox.showinfo('Empate!', 'Parabéns! Vocês empataram!')
            self.reset()
        
    def check_victory(self):
        'Checking Victory or Draw'
        # Rows
        increment = 0
        for i in range(3):
            if self.buttons[increment+i]['text'] == self.buttons[increment+i+1]['text'] == self.buttons[increment+i+2]['text'] and self.buttons[increment+i]['text'] != '':
                return 'venceu'
            increment += 2
        
        # Coluns
        for j in range(3):
            if self.buttons[j]['text'] == self.buttons[j+3]['text'] == self.buttons[j+6]['text'] and self.buttons[j]['text'] != '':
                return 'venceu'
        
        # Diagonais
        if self.buttons[0]['text'] == self.buttons[4]['text'] == self.buttons[8]['text'] and self.buttons[4]['text'] != '':
            return 'venceu'
        if self.buttons[2]['text'] == self.buttons[4]['text'] == self.buttons[6]['text'] and self.buttons[4]['text'] != '':
            return 'venceu'

        # Verificando Empate
        if self.preenchidos == 9:
            return 'empatou'

        return 'nao_venceu'
    
    def reset(self):
        'Cleaning the game'
        for button in self.buttons:
            button['text'] = ''
        
        self.preenchidos = 0

        self.player_x_or_o = choice(('X', 'O'))
        if self.player_x_or_o == 'X':
            self.ACT_COLOR = self.X_COLOR    
        else:
            self.ACT_COLOR = self.O_COLOR
        self.current_player['text'] = f'Jogador: {self.player_x_or_o}'
        self.current_player['fg'] = self.ACT_COLOR
        self.line['bg'] = self.ACT_COLOR


velha = JogoDaVelha()
if __name__ == '__main__':
    velha.game_window.mainloop()
