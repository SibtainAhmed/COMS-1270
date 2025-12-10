# Sibtain Ahmed
# Lab 9
# Nov-1-2025




from fourInSequence import checkWinner, checkDraw, checkAdjacent, checkForNextMoveWin

def test_checkWinner_horizontal():
    board = [
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        ["X", "X", "X", "X", ".", ".", "."],
    ]
    assert checkWinner(board, 1) == True


def test_checkWinner_vertical():
    board = [
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        ["X", ".", ".", ".", ".", ".", "."],
        ["X", ".", ".", ".", ".", ".", "."],
        ["X", ".", ".", ".", ".", ".", "."],
        ["X", ".", ".", ".", ".", ".", "."],
    ]
    assert checkWinner(board, 1) == True


def test_checkWinner_no_winner():
    board = [["." for _ in range(7)] for _ in range(6)]
    assert checkWinner(board, 1) == False



def test_checkDraw_full_board():
    board = [["X", "O", "X", "O", "X", "O", "X"] for _ in range(6)]
    assert checkDraw(board) == True


def test_checkDraw_not_full():
    board = [["X", "O", "X", ".", "X", "O", "X"] for _ in range(6)]
    assert checkDraw(board) == False




def test_checkForNextMoveWin_true_case():
    board = [
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        ["X", "X", "X", ".", ".", ".", "."],
    ]
    assert checkForNextMoveWin(board, 1) == 3



def test_checkAdjacent_two_horizontal():
    board = [
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", "X", "X", ".", ".", ".", "."],
    ]
    assert checkAdjacent(board, 5, 1, "X") >= 2
