# main.py
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modulA import create_board, print_board
from modulB import player_move
from modulC import check_win


def main():
    board = create_board()
    current_player = "X"

    while True:
        print_board(board)
        player_move(board, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"Игрок {current_player} победил!")
            break

        # Проверка ничьи
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("Ничья!")
            break

        # Меняем игрока
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
