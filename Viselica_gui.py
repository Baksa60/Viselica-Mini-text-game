
import tkinter as tk
from random import choice

stages = [
    '''
    --------
    |      |
    |      O
    |     \|/
    |      |
    |     / \\
    --------
    '''
    ,
    '''
    --------
    |      |
    |      O
    |     \|/
    |      |
    |     /
    --------
    '''
    ,
    '''
    --------
    |      |
    |      O
    |     \|/
    |      |
    |
    --------
    '''
    ,
    '''
    --------
    |      |
    |      O
    |     \|
    |      |
    |
    --------
    '''
    ,
    '''
    --------
    |      |
    |      O
    |      |
    |      |
    |
    --------
    '''
    ,
    '''
    --------
    |      |
    |      O
    |
    |
    |
    --------
    '''
    ,
    '''
    --------
    |      |
    |
    |
    |
    |
    --------
    '''
]

word_list = ['КОРОВА', 'СЛОН', 'НОСОРОГ', 'СОБАКА', 'ЯЩЕРИЦА', 'ЛЯГУШКА', 'ЛОШАДЬ',
    'ЗМЕЯ', 'КОШКА', 'МЕДВЕДЬ', 'КОЗА', 'БЕЛКА', 'ЛОСЬ', 'ОЛЕНЬ', 'БЕГЕМОТ',
    'ЖИРАФ', 'ОБЕЗЬЯНА', 'ЯГУАР', 'ГЕПАРД', 'ВОЛК', 'ЛИСА', 'ЛАМА', 'КАБАН',
    'СВИНЬЯ', 'ЗАЯЦ', 'ПЕСЕЦ', 'СОБОЛЬ', 'ВЫДРА', 'НОРКА', 'ЛЕНИВЕЦ', 'ПАНДА',
    'КОАЛА', 'СУСЛИК', 'БАРСУК', 'ЕНОТ', 'САЛАМАНДРА']

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Виселица')
        self.root.geometry('450x700')
        self.root.resizable(False, False)

        self.stage = 6
        self.guessed_letters = []
        self.hid_word = []
        self.game_over = False

        self.label_stage = tk.Label(root, text=stages[self.stage], font=('Consolas', 14), justify='left')
        self.label_stage.place(x=50, y=20)

        self.label_word = tk.Label(root, text='', font=('Arial', 24))
        self.label_word.place(x=225, y=250, anchor='center')

        self.label_guessed = tk.Label(root, text='Названные буквы: ', font=('Arial', 12), wraplength=350, justify='left', anchor='w')
        self.label_guessed.place(x=50, y=300)

        self.entry = tk.Entry(root, font=('Arial', 14))
        self.entry.place(x=50, y=330, width=350)
        self.entry.bind('<Return>', self.check_letter)

        self.button_restart = tk.Button(root, text='Новая игра', command=self.start_game)
        self.button_restart.place(x=175, y=370)

        self.label_result = tk.Label(root, text='', font=('Arial', 14), wraplength=400, justify='center')
        self.label_result.place(x=50, y=420, width=350)

        self.label_instruction = tk.Label(root, text='Введите одну букву русского алфавита.', font=('Arial', 12))
        self.label_instruction.place(x=225, y=480, anchor='center')

        self.start_game()

    def start_game(self):
        self.gues_word = choice(word_list)
        self.hid_word = ['_'] * len(self.gues_word)
        self.stage = 6
        self.guessed_letters.clear()
        self.label_stage.config(text=stages[self.stage])
        self.label_word.config(text=' '.join(self.hid_word))
        self.label_guessed.config(text='Названные буквы: ')
        self.label_result.config(text='Новая игра началась!')
        self.game_over = False
        self.entry.config(state=tk.NORMAL)

    def check_letter(self, event=None):
        if self.game_over:
            return

        letter = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if len(letter) != 1 or not ('А' <= letter <= 'Я'):
            self.label_result.config(text='Введите одну букву русского алфавита.')
            return

        if letter in self.guessed_letters:
            self.label_result.config(text='Эта буква уже была названа.')
            return

        self.guessed_letters.append(letter)
        if letter in self.gues_word:
            for i in range(len(self.gues_word)):
                if self.gues_word[i] == letter:
                    self.hid_word[i] = letter
            self.label_result.config(text='Верно!')
        else:
            self.stage -= 1
            self.label_result.config(text='Неверно!')

        self.label_stage.config(text=stages[self.stage])
        self.label_word.config(text=' '.join(self.hid_word))
        self.label_guessed.config(text=f'Названные буквы: {" ".join(self.guessed_letters)}')

        if '_' not in self.hid_word:
            self.label_result.config(text=f'Поздравляем! Вы угадали слово:\n{self.gues_word}')
            self.game_over = True
            self.entry.config(state=tk.DISABLED)
        elif self.stage == 0:
            self.label_result.config(text=f'Вы проиграли! Загаданное слово:\n{self.gues_word}')
            self.game_over = True
            self.entry.config(state=tk.DISABLED)

if __name__ == '__main__':
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
