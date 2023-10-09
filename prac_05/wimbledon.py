import  csv

def read_csv(filename):
    champions = {}  # Dictionary to store champions and their wins
    countries = set()  # Set to store unique countries

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.DictReader(in_file)  # Use DictReader to handle headers
        for row in reader:
            champion = row["Champion"]
            country = row["Country"]
            if champion in champions:
                champions[champion] += 1
            else:
                champions[champion] = 1
            countries.add(country)

    return champions, sorted(countries)

def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

def display_countries(countries):
    print("\nThese countries have won Wimbledon:")
    countries_str = ", ".join(countries)
    print(countries_str)

def main():
    filename = "wimbledon.csv"
    champions, countries = read_csv(filename)
    display_champions(champions)
    display_countries(countries)

if __name__ == "__main__":
    main()

