from random import *
stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |л
                   |     /
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                '''
    ]
word_list = [
    'КОРОВА', 'СЛОН', 'НОСОРОГ', 'СОБАКА', 'ЯЩЕРИЦА', 'ЛЯГУШКА', 'ЛОШАДЬ',
    'ЗМЕЯ', 'КОШКА', 'МЕДВЕДЬ', 'КОЗА', 'БЕЛКА', 'ЛОСЬ', 'ОЛЕНЬ', 'БЕГЕМОТ',
    'ЖИРАФ', 'ОБЕЗЬЯНА', 'ЯГУАР', 'ГЕПАРД', 'ВОЛК', 'ЛИСА', 'ЛАМА', 'КАБАН',
    'СВИНЬЯ', 'ЗАЯЦ', 'ПЕСЕЦ', 'СОБОЛЬ', 'ВЫДРА', 'НОРКА', 'ЛЕНИВЕЦ', 'ПАНДА',
    'КОАЛА', 'СУСЛИК', 'БАРСУК', 'ЕНОТ', 'САЛАМАНДРА'
]
game = True
guessed_letters = []
hid_word = []
stage = 6

def zam(c):
    for i in range(len(gues_word)):
        if gues_word[i] == c:
            hid_word[i] = c

def is_valid_input(c):
    return ('а' <= c <= 'я' or 'А' <= c <= 'Я') and len(c) == 1

def char(c):
    global stage
    if is_valid_input(c):
        guessed_letters.append(c)
        if c in gues_word:
            print('Верно!', '\U0001F600')
            print(stages[stage])
            print('Названные буквы:', ' '.join(guessed_letters))
            zam(c)
            return
        else:
            print('К сожалению неудачно', '\U0001F641')
            stage -= 1
            print(stages[stage])
            print('Названные буквы:', ' '.join(guessed_letters))
            return
    else:
        print('Доступны только буквы русского алфавита и только по одной.')
        print('Повторите пожалуйста ввод.')

print('Давайте играть в угадай животное!')
while game:

    def get_word():
        return choice(word_list)
    gues_word = get_word()

    hid_word.extend(len(gues_word) * '_')
    while '_' in hid_word:
        if stage == 0:
            break
        else:
            print(' '.join(hid_word), '(' + str(len(hid_word)) + ')')
            print('Ваша буква?')
            char(input().upper())

    if stage == 0:
        print('К сожалению, вы проиграли \U0001F641')
    else:
        print('Поздравления с победой! \U0001F600')
    print('Попробуем ещё раз?')
    print('Нажмите Enter для продолжения или любую клавишу для выхода.')
    a = input()
    if a == '':
        stage = 6
        hid_word.clear()
        guessed_letters.clear()
        continue
    else:
        print('До скорых встреч! \U0001F44B')
        break
