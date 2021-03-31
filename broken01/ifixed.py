#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

# Initilise 2 x float, and 1 x string variables
calc1 = 0.0
calc2 = 0.0
operation = ""

def check_user_input(input):

    try:
        # Convert it into float
        val = float(input)
        print("Input is a float number. Number = ", val)
    except ValueError:
        print("No.. input is not a number. It's a string")
        If val = "q" or val = "Q"
            val = "q"

def main()

    while (calc1 != "q" and calc2 != "q")
        print("\nWhat is the first operator? Or, enter q to quit: ")
        calc1 = raw_input()
        if calc1.lower() == "Q":
            break
        calc1 = float(calc1)
        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = raw_input()
        if calc2 == "q":
            break
        calc2 = float(calc2)
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = raw_input()
        if operation == "+":
            print(\n + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
        ifel operation == '-':
            print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
        else:
            print("\n Not a valid entry. Restarting...")

if __name__ == "__main__":
    main()
