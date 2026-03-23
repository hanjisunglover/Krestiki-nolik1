# modulC.py

def check_win(board, player):
    """Проверяет, победил ли игрок"""

    # Проверка строк
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Проверка столбцов
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Проверка диагоналей
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False