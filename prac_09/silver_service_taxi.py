from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness

        self.price_per_km = Taxi.price_per_km * self.fanciness

    def get_fare(self):
        """Calculate the total fare including the flagfall."""


        return super().get_fare() + SilverServiceTaxi.flagfall

    def __str__(self):
        """返回 SilverServiceTaxi 的字符串表示，包括起步费。"""
        # 基础每公里车费存储在类变量中
        base_fare = Taxi.price_per_km
        # 实际每公里车费包括豪华程度乘数
        actual_fare = base_fare * self.fanciness
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}, {self.current_fare_distance}km on current fare, ${actual_fare:.2f}/km plus flagfall of ${self.flagfall:.2f}"