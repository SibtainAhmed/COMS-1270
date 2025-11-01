# Sibtain Ahmed
# Lab 9
# Nov-1-2025

from rockPaperScissors import generateComputerMove, determineWinner, playRound
import random

def test_generateComputerMove():
    moves = ['rock', 'paper', 'scissors']
    for _ in range(100):
        assert generateComputerMove() in moves


def test_determineWinner():
    assert determineWinner('rock', 'scissors') == 'user'
    assert determineWinner('scissors', 'paper') == 'user'
    assert determineWinner('paper', 'rock') == 'user'
    assert determineWinner('rock', 'paper') == 'computer'
    assert determineWinner('scissors', 'rock') == 'computer'
    assert determineWinner('paper', 'scissors') == 'computer'
    assert determineWinner('rock', 'rock') == 'tie'
    assert determineWinner('paper', 'paper') == 'tie'
    assert determineWinner('scissors', 'scissors') == 'tie'


def test_playRound(monkeypatch):
    
    results = []
    for _ in range(100):
        result = playRound(random.choice(['rock', 'paper', 'scissors']))
        results.append(result)
    
    assert all(result in ['user', 'computer', 'tie'] for result in results)