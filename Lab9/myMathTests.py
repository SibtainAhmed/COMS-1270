# Sibtain Ahmed
# Lab 9


from myMath import add, subtract, multiply, divide, power, factorial, gcd
import pytest


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-2, -3) == -5


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(-3, -2) == -1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0
    assert multiply(-2, -3) == 6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 2) == -3
    assert divide(0, 5) == 0
    assert divide(5, 0) == 'Error'


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(-2, 2) == 4
    assert power(3, -1) == 1/3

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(-1) == 'Error'