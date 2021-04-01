#!/usr/bin/python3

def main():

    # 1. print name of game to screen
    gamename = "Welcome to the Boogie Monster BasherGame!!!\n***********************************\n"
    print(gamename)

    # 2. ask user multiple choice question
    user_input = input("Which Boogie Monster would you like to bash today? \n Choices: Pinky, Donald, Kim\n")
    if user_input.lower() == "pinky":
        print("Let's go bash the Pinky Boogie Monster!")
    elif user_input.lower() == "donald":
        print("Let's go bash the Donald Boogie Monster!")
    elif user_input.lower() == "kim":
        print("Let's go bash the Kim Boogie Monster!")
    else:
        print("I do not know this Boogie Monster! Game over...")

if __name__ == "__main__":
    main()
