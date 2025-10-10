from reverseString import reverseStringV1

def palindromeCheckV1(s):
    return s == reverseStringV1(s)

def palindromeCheckV2(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def main():
    user_input = input("Enter a string to check if it's a palindrome: ")
    if palindromeCheckV1(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')
    
    if palindromeCheckV2(user_input):
        print(f'"{user_input}" is a palindrome (using V2).')
    else:
        print(f'"{user_input}" is not a palindrome (using V2).')

if __name__ == "__main__":
    main()