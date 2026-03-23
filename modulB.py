# modulB.py

def player_move(board, player):
    """Обрабатывает ход игрока и ставит X или O на поле"""
    while True:
        try:
            row = int(input(f"Игрок {player}, введите строку (0-2): "))
            col = int(input(f"Игрок {player}, введите столбец (0-2): "))

            if row not in range(3) or col not in range(3):
                print("Координаты должны быть 0, 1 или 2!")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Клетка занята, выберите другую!")
        except ValueError:
            print("Введите число от 0 до 2!")