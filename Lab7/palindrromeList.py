# Sibtain Ahmed
# Oct 11, 2025
# Lab 7


def inputStringList():
    str_list = []
    while True:
        s = input("Enter a string (or '*' to finish): ")
        if s == '*':
            break
        str_list.append(s)
    return str_list

def palindromeList(lst):
    for i in range(len(lst) // 2):
        if lst[i] != lst[len(lst) - 1 - i]:
            return False
    return True

def main():
    strings = inputStringList()
    if palindromeList(strings):
        print("The list is a palindrome.")
    else:
        print("The list is not a palindrome.")

if __name__ == "__main__":
    main()