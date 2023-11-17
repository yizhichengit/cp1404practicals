from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50  # Additional charge for each new fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on the Taxi class."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness  # Adjust price per km by the fanciness level

    def get_fare(self):
        """Calculate the fare, including the flagfall and per km cost."""
        return super().get_fare() + SilverServiceTaxi.flagfall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi, including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"