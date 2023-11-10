
from guitar import Guitar

def main():
    guitars = []

    # Assuming the data from the image is stored in a string variable named data
    data = """
    Fender Stratocaster,2014,765.4
    Gibson L-5 CES,1922,16035.4
    Line 6 JTV-59,2010,1512.9
    Martin Grand J12-16GTE,2015,2199
    Taylor PS10ce ,2014,9318
    Gretsch 6120 Chet Atkins,1956,10999.99
    """
    lines = data.strip().split("\n")

    for line in lines:
        parts = line.split(',')
        name = parts[0].strip()
        year = int(parts[1].strip())
        cost = float(parts[2].strip())
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

    print("Guitars:")
    for guitar in guitars:
        print(guitar)

    guitars.sort()
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)

if __name__ == "__main__":
    main()
