# Sibtain Ahmed
# Oct 25, 2025

import random


def main():
    input_sentence = input("Enter a sentence: ")
    words = input_sentence.split()
    swapped_dict = {}
    for w in words:
        swapped_dict[w] = random.choice(words)
    print(swapped_dict)

if __name__ == "__main__":
    main()