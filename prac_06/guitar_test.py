from guitar import Guitar

def main():
    # Create sample guitars
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1299.99)

    # Test get_age()
    print("{} get_age() - Expected {}. Got {}".format(gibson.name, 100, gibson.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another_guitar.name, 9, another_guitar.get_age()))

    # Test is_vintage()
    print("{} is_vintage() - Expected {}. Got {}".format(gibson.name, True, gibson.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name, False, another_guitar.is_vintage()))

    # Example of a method that may have been implemented incorrectly
    # For demonstration purposes
    fifty_year_old_guitar = Guitar("50-year old guitar", 1972, 2000)
    print("{} is_vintage() - Expected {}. Got {}".format(fifty_year_old_guitar.name, True, fifty_year_old_guitar.is_vintage()))

if __name__ == "__main__":
    main()
