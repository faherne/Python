#!/usr/bin/python3

def main():

    # 1. print name of game to screen
    gamename = "Welcome to the Boogie Monster BasherGame!!!\n***********************************\n"
    print(gamename)

    # 2. ask user multiple choice question
    user_input = input("Which Boogie Monster would you like to bash today? \n [Choices: Pinky, Donald, Kim]\nPress Q or q to exit\n")

    boogiemonsters = ['pinky','donald','kim']
    
    validmonster = "false"
    while validmonster == "false" and user_input.lower() != "q": 
        if user_input.lower() in boogiemonsters:
            print("\nLet's go bash the Boogie Monster!\n")
            print("KAPOW!\n")
            print("The Boogie Monster has been bashed")
            validmonster = "true"
        else:
            print("Choose a valid Boogie Monster!\n")
            validmonster = "false"
    print("Exiting prgram...")

if __name__ == "__main__":
    main()
