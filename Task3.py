# Создайте программу для игры в ""Крестики-нолики"".
# Пример интерфейса:
#
#   |   | 0
#-----------    
#   |   |
#-----------
#   | X |
#Ввод можно реализовать через введение двух чисел (номеров строки и столбца).

import random

board = range(1,10)


def draw_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def start_game():
    symbol = ''
    while not symbol == "X" or symbol == "O":
        print('Вы будет играть Х или О?')
        symbol = input().upper() 
    if symbol == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def first_player():
    if random.randint(0, 1) == 0:
        return "компьютер "
    else:
        return "игрок "


def move_on_board(board, symbol, move):
    board[move] = symbol


def win(board, symbol):
    return ((board[7] == symbol and board[8] == symbol and board[9] == symbol)) or \
            (board[4] == symbol and board[5] == symbol and board[6] == symbol) or \
            (board[1] == symbol and board[2] == symbol and board[3] == symbol) or \
            (board[7] == symbol and board[4] == symbol and board[1] == symbol) or \
            (board[8] == symbol and board[5] == symbol and board[2] == symbol) or \
            (board[9] == symbol and board[6] == symbol and board[3] == symbol) or \
            (board[9] == symbol and board[5] == symbol and board[1] == symbol) or \
            (board[7] == symbol and board[5] == symbol and board[3] == symbol)


def get_board_copy(board):
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def place_free(board, move):
    return board[move] == ''


def get_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9 '.split() or not place_free(board, int(move)):
        print("Какой Ваш следующий ход? от 1 до 9")
        move = input()
    return int(move)


def choose_move(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if place_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def computer_move(board, computer_symbol):
    if computer_symbol == "X":
        player_symbol = "O"
    else:
        player_symbol = "X"

    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if place_free(board_copy, i):
            move_on_board(board_copy, computer_symbol, i)
            if win(board_copy, computer_symbol):
                return i
    
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if place_free(board_copy, i):
            move_on_board(board_copy, player_symbol, i)
            if win(board_copy, player_symbol):
                return i

    move = choose_move(board, [1, 3, 7, 9])
    if move != None:
        return move
    if place_free(board, 5):
        return 5
    return choose_move(board, [2, 4, 6, 8])


def board_full(board):
    for i in range(1,10):
        if place_free(board, i):
            return False
        return True

print("Игра крестики-нолики") 


while True:
    the_board = [' '] * 10
    player_symbol, computer_symbol = start_game()
    turn = first_player()
    print(' ' + turn + " ходит первым ")
    play_game = True

    while play_game:
        if turn == "игрок ":
            draw_board(the_board)
            move = get_move(the_board)
            move_on_board(the_board, player_symbol, move)

        if win (the_board, player_symbol):
                draw_board(the_board)
                print("Вы выиграли!")
                play_game = False
        else:
                move = computer_move(the_board, computer_symbol)
                move_on_board(the_board, computer_symbol, move)
            
        if win (the_board, computer_symbol):
                draw_board(the_board)
                print("Выиграл компьютер!")
                
                play_game = False
        else: 
            if board_full(the_board):
                draw_board(the_board)
                print("Ничья!")
                break
            else:
                    turn = "игрок "
          
        print('Сыграем еще раз? (да или нет)')
        if not input().lower().startswith('д'):
            break