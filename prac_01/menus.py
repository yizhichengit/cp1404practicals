

def main():

    name = input("Enter name: ")


    choice = display_menu()


    while choice != 'Q':
        if choice == 'H':
            print(f"Hello {name}")
        elif choice == 'G':
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")


        choice = display_menu()


    print("Finished.")


def display_menu():

    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    return input(">>> ").upper()


if __name__ == "__main__":
    main()


