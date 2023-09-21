def main():
    Menu = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or your function to determine the result from importscore.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""

    choice = ""
    score = None

    while choice != "Q":
        print(Menu)
        choice = input(">>> ").upper()
        if choice == "G":
            score = float(input("Your score: "))
            if score < 0 or score > 100:
                print("Invalid number")
                score = None
        elif choice == "P":
            if score is None:
                print("Please get a valid score first.")
            else:
                result = ask_score(score)
                print(f"Your score is {result}")
        elif choice == "S":
            if score is None:
                print("Please get a valid score first.")
            else:
                print(print_star(score))
        elif choice != "Q":
            print("Invalid option")

    print("Thank you.")


def ask_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score <= 50:
        return "Bad"
    elif score <= 90:
        return "Passable"
    else:
        return "Excellent"


def print_star(score):
    return "*" * int(score)


if __name__ == "__main__":
    main()
