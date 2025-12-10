from myMath import add, subtract, multiply, divide
from test2 import generateComputerMove

def test_add():
    assert add(100, 101) == 201
    assert add(-2, 1) == -1
    assert add(0, 0) == 0


def generateComputerMove_test():
    allChoices = ['rock', 'paper', 'scissors']
    for _ in range(100):
        assert generateComputerMove() in allChoices