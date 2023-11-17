# taxi_test.py
from taxi import Taxi

def main():
    """Test Taxi class with various operations."""
    # Create a new taxi object named "Prius 1" with 100 units of fuel
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km
    my_taxi.drive(40)

    # Print the taxi's details and the current fare
    print(my_taxi)

    # Start a new fare and drive the car 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Print the details and the current fare
    print(my_taxi)

if __name__ == '__main__':
    main()