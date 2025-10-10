

def main():
    print("A TA of COMS 1270 is enjoying conducting labs!")
    temp = input("Do you want to hear a story? (yes/no): ")
    if temp == "yes":
        print("Once upon a time, there was a TA named Sibtain.")
        print("Sibtain loved helping students learn programming.")
        temp2 = input("Do you want to hear what happened next? (yes/no): ")
        if temp2 == "yes":
            print("One day, Sibtain discovered a magical bug in the code.")
            print("This bug could make programs run faster and more efficiently!")
            temp3 = input("Do you want to know how Sibtain used the magical bug? (yes/no): ")
            if temp3 == "yes":
                print("Sibtain shared the magical bug with all the students.")
                print("Everyone was amazed and grateful for Sibtain's help.")
                print("And they all coded happily ever after!")
            else:
                print("Okay, maybe next time!")
        else:
            print("Okay, maybe next time!")
    else:
        print("Okay, maybe next time!")
    
    enjoy = input("Did you enjoy the story? (yes/no): ")
    if enjoy == "yes":
        print("I'm glad you enjoyed it!")
    else:
        print("I'm sorry to hear that. I'll try to tell a better story next time!")


if __name__ == "__main__":
    main()