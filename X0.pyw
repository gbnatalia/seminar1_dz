'''
Игра крестики-нолики
'''
import tkinter as tk

class App(tk.Tk):

    text_state = [
        'Ходит игрок 1',
        'Ходит игрок 2',
        'Игра завершена.\nНичья',
        'Игра завершена.\nВыиграл 1 игрок',
        'Игра завершена.\nВыиграл 2 игрок'
    ]
    num_state = 0
    cnt_step = 0
    btn = []

    def next(self, sym, row, col):
        self.btn[3 * row + col]['text'] = sym
        win_state = 3 + self.num_state
        next_state = 1 - self.num_state

        # проверка горизонтали
        self.num_state = win_state
        for c in range(3):
            if self.btn[3 * row + c]['text'] != sym:
                self.num_state = next_state
                break

        # проверка вертикали
        if self.num_state != win_state:
            self.num_state = win_state
            for r in range(3):
                if self.btn[3 * r + col]['text'] != sym:
                    self.num_state = next_state
                    break

        # проверка диагонали 1
        if self.num_state != win_state:
            if (row == 0 and col == 0) or (row == 1 and col == 1) or (row == 2 and col == 2):
                self.num_state = win_state
                for i in range(3):
                    if self.btn[4 * i]['text'] != sym:
                        self.num_state = next_state
                        break

        # проверка диагонали 2
        if self.num_state != win_state:
            if (row == 0 and col == 2) or (row == 1 and col == 1) or (row == 2 and col == 0):
                self.num_state = win_state
                for i in range(3):
                    if self.btn[3 * i + 2 - i]['text'] != sym:
                        self.num_state = next_state
                        break

        if self.num_state != win_state and self.cnt_step == 9:
            self.num_state = 2

        self.l['text'] = self.text_state[self.num_state]

    def btn_click(self, row, col):
        self.cnt_step += 1
        if self.cnt_step == 9:
            for i in range(9):
                self.btn[i]['state'] = 'disabled'
        else:
            self.btn[3 * row + col]['state'] = 'disabled'

        if self.num_state == 0:
            self.next('X', row, col)
        elif self.num_state == 1:
            self.next('0', row, col)

    def __init__(self):
        super().__init__()
        self.title("X-O")
        self.geometry('180x200+600+300')
        self['bg'] = "blue"

        # табло состояния
        f_state = tk.Frame(self)
        f_state.pack(side=tk.TOP, pady=5, padx=5, expand=0, fill='x')

        self.l = tk.Label(f_state, bg="green", text=self.text_state[self.num_state], font=12)
        self.l.pack(fill='x')

        # поле игры
        f_game = tk.Frame(self)
        f_game.pack(side=tk.TOP, pady=10, padx=12, expand=0, fill='x')
        for irow in range(3):
            for icol in range(3):
                self.btn.append(tk.Button(f_game, text='-', width=6, height=2, command=lambda r=irow, c=icol: self.btn_click(r, c)))
                self.btn[irow * 3 + icol].grid(row=irow, column=icol, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
