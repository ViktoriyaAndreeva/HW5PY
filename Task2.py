# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше положенного или больше чем имеется в куче.
# b) Подумайте как наделить бота ""интеллектом"". Напоминаю, если перед пользователем будет лежать 29 конфет, то он, однозначно, проиграет. 
# Достаточно довести игру до такой ситуации.

import random

# игра игроков
def player_move(left, current_player):
    print(f"Ход делает игрок № {current_player + 1}...")

    while True:
        amount = input(f"Введите количество конфет, которое Вы хотите взять:")
        if not amount.isnumeric():
            print("Ошибка! Введите число!")
            continue
        
        amount = int(amount)
        if amount <= 0 or amount >= 29:
            print("Ошибка! Число должно быть в промежутке от 1..28!")
            continue

        if amount > left:
            print("Ошибка! Недостаточно конфет!")
            continue
        return amount

# игра бота
def bot_move(left):
    print("Ходит бот...")
    if left <= 57 and left > 29:
        amount = left -  29
        return amount
    elif left < 29:
        amount = left
        return amount
    else:
        amount = random.randint(1,28)
        return amount


sweets = 2021
opponent = input("Если играем с ботом, введите 'bot', если с игроком - любые символы: ")
game_end = False

# 0 - Игрок
# 1 - Оппонент
current_player = random.choice([0, 1])
left = sweets

# подсчет остатка и переход хода
while True:
    print(f"Осталось на столе конфет: {left}")
    amount = bot_move(left) if opponent == "bot" and current_player == 1 else player_move(left, current_player)
    print(f"Взято конфет: {amount}")
    left -= amount
    if left == 0:
        break
    current_player = 1 - current_player 

# определение выигрыша
if opponent == "bot" and current_player == 1:
    print("Выиграл бот!")
else:
    print(f"Выиграл игрок №{current_player + 1}!")

print("Сыграем еще раз? (yes or no?)")   

if not input().lower().startswith('y'):
    print("До следующих встреч!")
else:
    print("Запускайте и продолжим!")
