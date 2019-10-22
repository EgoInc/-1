import graphics as gr
from graphics import *


def is_int(str):
    """Какая-то фигня, которая мне потом гипер понадобится"""
    try:
        int(str)
        return True
    except ValueError:
        return False


def draw_cross(x, y):
    """Функция, рисующая крестик в заданном поле"""
    gr.Line(gr.Point(x + 25, y + 25), gr.Point(x - 25, y - 25)).draw(window)
    gr.Line(gr.Point(x + 25, y - 25), gr.Point(x - 25, y + 25)).draw(window)



def draw_zero(x, y):
    """Функция, рисующая нолик в заданном поле"""
    gr.Circle(gr.Point(x, y), 20).draw(window)


class Player():
    "Ходит либо крестиками, либо ноликами, ставя их на пустую клетку"

    def __init__(self, token):
        self.token = token

    def move(self):
        check = False
        while not check:
            player_choice = input('Выберете куда поставить ' + self.token + '?')
            while player_choice.isalpha():
                print('Вы ввели не число')
                player_choice = input('Выберете куда поставить ' + self.token + '?')
            if (int(player_choice) <= 9 and int(player_choice) >= 1 and is_int(deck[int(player_choice) - 1])):
                check = True
        deck[int(player_choice) - 1] = self.token  # Заполняем массив

        centers_of_cells = ((50, 50), (150, 50), (250, 50), (50, 150), (150, 150), (250, 150), (50, 250), (150, 250),
                            (250, 250))  # кортеж, содержащий координаты центра клеток для рисования в них
        x, y = centers_of_cells[int(player_choice) - 1]  # Рисуем
        if self.token == "X":
            draw_cross(x, y)
        else:
            draw_zero(x, y)


class Deck():
    "Доска размером 3х3. Основные методы: проверяет игру на победу"

    def __init__(self):
        for M, N in ((100, 0), (100, 300)), ((200, 0), (200, 300)), ((0, 100), (300, 100)), ((0, 200), (300, 200)):
            gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)  # нарисовали границы каждой клетки
        k = 1
        for m in (10,10), (110,10), (210, 10), (10,110),(110,110),(210,110),(10,210),(110,210),(210,210):
            gr.Text(Point(*m), k).draw(window)
            k+=1

    def if_win (self):
        """Проверяет на победу"""
        win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
        for each in win_comb:
            if deck[each[0]] == deck[each[1]] == deck[each[2]]:
                win = 1
                return win
        return False


window = gr.GraphWin("Cross-Zero", 300, 300)

deck = [i for i in range(1, 10)]  # Создание стартого поля

field = Deck()
zero = Player("О")
cross = Player("X")

counter = 0

win = False
while not win:
    if counter % 2 == 0:
        cross.move()
    else:
        zero.move()
    counter += 1
    if counter > 4:
        check = field.if_win()
        if check:
            print('С победой' + "X" if counter % 2 == 0 else 'С победой' + "O")
            win = True
            break
    if counter == 9:
        print('Свободных клеток больше нет. Ничья')
        break

window.getMouse()
window.close()
