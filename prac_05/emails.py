def extract_name(email):

    parts = email.split('@')
    name = parts[0].replace('.', ' ').title()
    return name


def main():
    email_dict = {}

    while True:
        email = input("Email: ")
        if email == "":
            break

        name = extract_name(email)


        confirm_name = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm_name == '' or confirm_name == 'y':
            email_dict[email] = name
        else:
            name = input("Name: ")
            email_dict[email] = name

    print("\nOutput:")
    for email, name in email_dict.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()


