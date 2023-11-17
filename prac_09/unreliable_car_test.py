from unreliable_car import UnreliableCar

def unreliable_car_test():
    """Test function for UnreliableCar class."""
    dodgy_car = UnreliableCar("Dodgy", 100, 50)
    distance_driven = dodgy_car.drive(40)
    print(f"Attempted to drive 40km; drove {distance_driven}km")
    print(dodgy_car)

    distance_driven += dodgy_car.drive(50)
    print(f"Attempted to drive another 50km; drove {distance_driven}km total")
    print(dodgy_car)

if __name__ == '__main__':
    unreliable_car_test()