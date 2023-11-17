import random
from prac_09.car import Car
class UnreliableCar(Car):
    """Represent an UnreliableCar object, which is a kind of Car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance based on its reliability."""
        random_chance = random.randint(0, 100)
        if random_chance < self.reliability:
            return super().drive(distance)
        else:
            return 0