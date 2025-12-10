# Sibtain Ahmed
# Lab 9
# Nov-1-2025

import random

def generateComputerMove():
    return random.choice(['rock', 'paper', 'scissors'])


def determineWinner(userMove, computerMove):
    if userMove == computerMove:
        return 'tie'
    elif (userMove == 'rock' and computerMove == 'scissors') or \
         (userMove == 'scissors' and computerMove == 'paper') or \
         (userMove == 'paper' and computerMove == 'rock'):  
        return 'user'
    else:
        return 'computer'


def playRound(userMove):
    
    computerMove = generateComputerMove()
    print(f"Computer chose: {computerMove}")
    winner = determineWinner(userMove, computerMove)
    return winner



def main():
    userScore = 0
    computerScore = 0
    rounds = int(input("Enter (odd) number of rounds to play: "))
    winScore = rounds // 2 + 1
    for _ in range(rounds):
        userMove = input("Enter your move (rock, paper, scissors): ").lower()
        result = playRound(userMove)
        if result == 'user':
            userScore += 1
            print("You win this round!")
        elif result == 'computer':
            computerScore += 1
            print("Computer wins this round!")
        else:
            print("This round is a tie!")
        print(f"Score -> You: {userScore}, Computer: {computerScore}\n")
    
        if userScore >= winScore:
            print("Congratulations! You won the game!")
        elif computerScore >= winScore:
            print("Computer wins the game! Better luck next time.")



if __name__ == "__main__":
    main()