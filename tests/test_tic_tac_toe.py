import pytest
from modulA import create_board
from modulC import check_win

def test_create_board_is_empty():
    """Тест: проверка, что поле создается пустым 3x3"""
    board = create_board()
    assert len(board) == 3
    # Проверяем, что все 9 клеток — это пробелы
    assert all(cell == " " for row in board for cell in row)

def test_check_win_horizontal():
    """Тест: проверка победы по горизонтали для игрока X"""
    board = [
        ["X", "X", "X"],
        [" ", "O", " "],
        [" ", " ", "O"]
    ]
    assert check_win(board, "X") is True

def test_check_win_no_winner():
    """Тест: проверка, что на пустом поле нет победителя"""
    board = create_board()
    assert check_win(board, "X") is False
    assert check_win(board, "O") is False