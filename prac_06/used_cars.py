"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""


from prac_06.car import Car

def main():
    my_car = Car(50, "My Car skywalk")
    print(my_car)
    FUEL= int(input("The add Fuel number:"))

    my_car.add_fuel(FUEL)
    print(f"Added {FUEL} units of fuel. Fuel = {my_car.fuel}")

    distance_driven = my_car.drive(115)
    print(f"Distance driven: {distance_driven} km")
    print(my_car)

if __name__ == "__main__":
    main()



