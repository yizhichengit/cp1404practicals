# We have the Taxi and SilverServiceTaxi classes available to us.
# Let's write the taxi simulator program as described in the provided images.
from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

def display_taxis(taxis):
    """Display available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def main():
    """Main program for taxi simulator."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()
        if choice == 'q':
            break
        elif choice == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == 'd':
            if current_taxi:
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
                print(f"Bill to date: ${total_bill:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

main()  # Start the simulator

