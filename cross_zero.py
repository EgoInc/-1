def is_int(str):  # Эта фигня нужна для проверки ввода потом
    try:
        int(str)
        return True
    except ValueError:
        return False


class Deck():
    "Доска размером 3х3. Основные методы: рисует доску, показывает расклад игры, проверяет на победу"

    def draw_deck(self):
        """Рисует доску"""
        print("_____________________")
        for i in range(3):
            print(' | ', deck[0 + i * 3], ' | ', deck[1 + i * 3], ' | ', deck[2 + i * 3], '|')
            print('_____________________')

    def if_win(self):
        """Проверяет расклад"""
        win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
        for each in win_comb:
            if deck[each[0]] == deck[each[1]] == deck[each[2]]:
                win = 1
                return win
        return False


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
        deck[int(player_choice) - 1] = self.token


deck = [i for i in range(1, 10)]  # Создание стартого поля

field = Deck()
zero = Player("О")
cross = Player("X")

field.draw_deck()
counter = 0

win = False
while not win:
    if counter % 2 == 0:
        cross.move()
    else:
        zero.move()
    counter += 1
    field.draw_deck()
    if counter > 4:
        check = field.if_win()
        if check:
            print('С победой' + "X" if counter % 2 == 0 else 'С победой ' + "O")
            win = True
            break
    if counter == 9:
        print('Свободных клеток больше нет. Ничья')
        break
