def main():
    password = int(input("password: "))
    print(get_password(password))


def get_password(password):
    return "*" * password

if __name__ == "__main__":
    main()