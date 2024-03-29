import customtkinter
import tkinter.messagebox
from tictactoe_field import GameField
from config import get_ico


class App(customtkinter.CTk):
    def __init__(self, gamefield):
        super().__init__()

        self.gamefield = gamefield

        self.title("TICTACTOE")
        self.icofile = 'tictactoe.ico'

        self.resizable(False, False)
        self.geometry("+400+70")
        get_ico(self)

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.grid(padx=30, pady=30)

        self.buttons = [[0] * 3 for _ in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c] = customtkinter.CTkButton(master=self.frame,
                                text=self.cell_value((r, c)),
                                width=70,
                                height=70,
                                fg_color=["#DC143C", "#DC143C"],
                                hover_color=["#A50021", "#A50021"],
                                text_color='black',
                                font=('Verdana', 36),
                                command=lambda row=r, column=c: self.go((row, column)))
                self.buttons[r][c].grid(row=r, column=c)

    def cell_value(self, coords: tuple):
        match self.gamefield[coords]:
            case 0: return ''
            case 1: return 'X'
            case 2: return 'O'

    def redraw(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].configure(text=self.cell_value((r, c)))
        self.update()
    
    def go(self, coords: tuple):
        if self.gamefield.human(coords):
            if self.check_win():
                self.gamefield.droid()
                self.check_win()

    def check_win(self):
        self.redraw()
        match self.gamefield.win:
            case 0: return True
            case 1: tkinter.messagebox.showinfo(message='Human WIN!')
            case 2: tkinter.messagebox.showinfo(message='Droid WIN!')
            case 3: tkinter.messagebox.showinfo(message='DRAW!')
        self.restart()

    def restart(self):
        self.gamefield.init()
        self.redraw()


def tictactoe():
    game = GameField()
    game.init()

    app = App(game)
    app.mainloop()


if __name__ == "__main__":
    tictactoe()

