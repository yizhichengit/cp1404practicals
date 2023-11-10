from guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{name} ({year}) : ${cost:.2f} added.")

        name = input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():  # Assuming Guitar class has this method
            vintage_string = "(vintage)"
        print(f"Guitar {i}: {guitar.name:<20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


if __name__ == "__main__":
    main()
