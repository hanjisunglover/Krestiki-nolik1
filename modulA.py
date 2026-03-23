# modulA.py

def create_board():
    """Создаёт пустое поле 3x3"""
    return [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
    """Выводит поле в консоль"""
    for row in board:
        print("|".join(row))
        print("-" * 5)


# Проверка работы модуля
if __name__ == "__main__":
    board = create_board()
    print_board(board)