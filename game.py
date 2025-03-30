import time
import random


def display_board(board):
    print('\n' * 100)
    print(board[0] + "|" + board[1] + "|" + board[2] + "\n" + board[3] + "|" + board[4] + "|" + board[5] + "\n" + board[
        6] + "|" + board[7] + "|" + board[8])


def player_input():  # setup
    player1 = ""
    while player1 != "X" or player1 != "O":
        player1 = input("Player 1 podaj czy chcesz być X czy O: ")
        if player1 not in ["X", "O"]:
            print("Wybrany przez Ciebie znak nie może uczestniczyć w grze, spróbuj ponownie")
        else:
            if player1 == "X":
                player2 = "O"

            else:
                player2 = "X"
            print("Player 1 wybrał {}, więc Player 2 otrzymuje {} ".format(player1, player2))
            return player1


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, mark):
    win = "WIN WIN WIN"
    if board[0] == mark and board[1] == mark and board[2] == mark:
        return win
    if board[3] == mark and board[4] == mark and board[5] == mark:
        return win
    if board[6] == mark and board[7] == mark and board[8] == mark:
        return win
    if board[0] == mark and board[3] == mark and board[6] == mark:
        return win
    if board[1] == mark and board[4] == mark and board[7] == mark:
        return win
    if board[2] == mark and board[5] == mark and board[8] == mark:
        return win
    if board[0] == mark and board[4] == mark and board[8] == mark:
        return win
    if board[2] == mark and board[4] == mark and board[6] == mark:
        return win


def choose_first():  # setup
    gofirst = random.randint(1, 2)
    print("Przypiszcie do siebie litery A i B")
    print("Macie na to 10 sekund")
    time.sleep(10)
    if gofirst == 1:
        return "Player A ma playera 1"
    else:
        return "Player B ma playera 1"


def space_check(board, position):
    if board[position] == " ":
        return True
    else:
        return False


def full_board_check(board):
    counter = 0
    for position in board:
        if position != " ":
            counter += 1
    if counter == 9:
        return True
    else:
        return False


def player_choice(board):
    while True:
        newposition = input("Podaj następną pozycję, którą chcesz zająć: ")
        if not newposition.isdigit():
            print("Podana pozycja nie jest liczbą")
            continue

        newposition = int(newposition)
        if newposition not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            print("Wpisana liczba nie odpowiada żadnej pozycji, spróbuj ponownie")
            continue
        if space_check(board, newposition):
            return newposition
        else:
            print("ta pozycja jest już zajęta, spróbuj inną")
            continue


def replay():  # repeat
    while True:
        again = input("Czy chcesz zagrać jeszcze raz? (Y/N): ")
        if again == "Y":
            return True
        else:
            return False


gametime = True
gameon = True
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
board2 = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
marker = [' ', ' ']

while gametime:
    print("Welcome to Tic Tac Toe!")
    print(choose_first())
    choosenmarkerbyplayer = player_input()
    if choosenmarkerbyplayer == "X":
        marker = ['X', 'O']

    else:
        marker = ['O', 'X']

    while gameon:
        for mark in marker:
            if win_check(board, mark):
                print("Zwyciężył: {}".format(mark))
                gameon = False
                break
            if full_board_check(board):
                print("Gra skończona - remis")
                gameon = False
                break

            display_board(board)
            print("{} teraz twój ruch".format(mark))
            newstep = player_choice(board)
            place_marker(board, mark, newstep)

    if not gameon:
        if replay():
            continue
        else:
            print("Dziękuję za gre!")
