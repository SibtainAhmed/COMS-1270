

def findSubStringV1(s, subS):
    return s.find(subS)

def findSubStringV2(s, subS):
    if subS not in s:
        return -1
    return s.index(subS)

def findSubStringV3(s, subS):
    for i in range(len(s) - len(subS) + 1):
        if s[i:i+len(subS)] == subS:
            return i
    return -1

def main():
    user_input = input("Enter the main string: ")
    sub_string = input("Enter the substring to find: ")
    
    index_v1 = findSubStringV1(user_input, sub_string)
    print(f"Index of substring using V1 (find): {index_v1}")
    
    index_v2 = findSubStringV2(user_input, sub_string)
    print(f"Index of substring using V2 (index): {index_v2}")
    
    index_v3 = findSubStringV3(user_input, sub_string)
    print(f"Index of substring using V3 (manual search): {index_v3}")


if __name__ == "__main__":
    main()