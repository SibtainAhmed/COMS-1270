
def reverseStringV1(s):
    return s[::-1]


def reverseStringV2(s):
    return reversed(s)


def reverseStringV3(s):
    res = ""
    for i in range(len(s)-1, -1, -1):
        res += s[i]
    return res

def reverseStringV4(s):
    res = ''
    for char in s:
        res = char + res
    return res


def reverseStringV5(s):
    res = ''
    i = len(s) - 1
    while i >= 0:
        res += s[i]
        i -= 1
    return res


def main():
    user_input = input("Enter a string to reverse: ")
    reversed_stringV1 = reverseStringV1(user_input)
    print("Reversed string v1:", reversed_stringV1) 
    reversed_stringV2 = reverseStringV2(user_input)
    print("Reversed string v2:", ''.join(reversed_stringV2))
    reversed_stringV3 = reverseStringV3(user_input)
    print("Reversed string v3:", reversed_stringV3)
    reversed_stringV4 = reverseStringV4(user_input)
    print("Reversed string v4:", reversed_stringV4)
    reversed_stringV5 = reverseStringV5(user_input)
    print("Reversed string v5:", reversed_stringV5)

if __name__ == "__main__":
    main()